# BeredskabsInfo

**BeredskabsInfo** er en brugerdefineret integration til Home Assistant, der henter hændelser fra ODIN.dk baseret på `beredskabsID`. Den opretter en sensor, der viser opsummering (summary) af de seneste hændelser.

---

## 🔧 Funktioner

- GUI-konfiguration via Home Assistant
- Vælg:
  - BeredskabsID (eks. 1212, 1313...)
  - Station
  - Antal hændelser (1–20)
  - Opdateringsinterval (1–30 minutter)
- Opretter én sensor: `sensor.beredskabsinfo_112`
- Viser `summary` for seneste hændelser

---

## 📦 Installation

1. Hent [ZIP-filen her](https://github.com/dkduck/beredskabsinfo) eller kopiér `custom_components/beredskabsinfo/` til din Home Assistant installation:
   ```
   /config/custom_components/beredskabsinfo/
   ```
2. Genstart Home Assistant.
3. Gå til **Indstillinger → Enheder & Tjenester → Tilføj integration**, og vælg *BeredskabsInfo*.

---

## 📄 Eksempel på sensor-output

```yaml
sensor:
  - platform: beredskabsinfo
    name: beredskabsinfo_112
```

Sensoren viser hændelser som én tekststreng med opsummeringer adskilt af `|` og ekstra attributter med `title` og `summary`.

---

## 🧪 Eksempler på data

```json
sensor.beredskabsinfo_112:
  value: "Brand i lejlighed | Redning på motorvej"
  attributes:
    entries:
      - title: "Brand i lejlighed"
        summary: "Branden opstod i stuen – ingen tilskadekomne."
      - title: "Redning på motorvej"
        summary: "Bil forulykket – 1 person kørt til hospital."
```

---

## 🤝 Bidrag

Pull requests og forslag er velkomne! Dette projekt er open source under MIT-licensen.

---

## 👤 Vedligeholdes af

**[dkduck](https://github.com/dkduck)**