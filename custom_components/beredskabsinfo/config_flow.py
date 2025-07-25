import voluptuous as vol
from homeassistant import config_entries
from .const import *

STATIONS = ["Station A", "Station B", "Station C"]
BEREDSKABS_IDS = ["1212", "1313", "1414"]

class BeredskabsInfoConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="BeredskabsInfo", data=user_input)

        schema = vol.Schema({
            vol.Required(CONF_BEREDSKABSID): vol.In(BEREDSKABS_IDS),
            vol.Required(CONF_STATION): vol.In(STATIONS),
            vol.Required(CONF_EVENTS, default=5): vol.All(vol.Coerce(int), vol.Range(min=1, max=20)),
            vol.Required(CONF_SCAN_INTERVAL, default=30): vol.All(vol.Coerce(int), vol.Range(min=1, max=30)),
        })

        return self.async_show_form(step_id="user", data_schema=schema)