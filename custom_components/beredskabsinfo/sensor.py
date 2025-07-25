import feedparser
from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.helpers.entity import Entity
from homeassistant.components.sensor import SensorEntity
from .const import *

async def async_setup_entry(hass, entry, async_add_entities):
    name = "beredskabsinfo_112"
    beredskabsid = entry.data[CONF_BEREDSKABSID]
    station = entry.data[CONF_STATION]
    events = entry.data[CONF_EVENTS]
    interval = entry.data[CONF_SCAN_INTERVAL]

    feed_url = f"http://www.odin.dk/RSS/RSS.aspx?beredskabsID={beredskabsid}"

    async def async_update_data():
        feed = feedparser.parse(feed_url)
        if not feed.entries:
            raise UpdateFailed("No entries in feed")
        return feed.entries[:events]

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name="BeredskabsInfo Feed",
        update_method=async_update_data,
        update_interval=timedelta(minutes=interval),
    )

    await coordinator.async_config_entry_first_refresh()
    async_add_entities([BeredskabsInfoSensor(coordinator, name)], True)

class BeredskabsInfoSensor(SensorEntity):
    def __init__(self, coordinator, name):
        self._coordinator = coordinator
        self._attr_name = name
        self._attr_unique_id = name

    @property
    def native_value(self):
        summaries = [entry.get("summary", "") for entry in self._coordinator.data]
        return " | ".join(summaries)

    @property
    def extra_state_attributes(self):
        return {
            "entries": [
                {"title": e.get("title"), "summary": e.get("summary")}
                for e in self._coordinator.data
            ]
        }

    async def async_update(self):
        await self._coordinator.async_request_refresh()