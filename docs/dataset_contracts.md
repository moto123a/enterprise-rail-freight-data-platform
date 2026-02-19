# Dataset Contracts (Schema + Rules)

## Contract: freight_events (stream)
**Topic / Stream:** `freight_events`

### Required Fields
- shipment_id (string)
- origin (string)
- destination (string)
- distance_km (int)
- weight_tons (int)
- event_timestamp (ISO timestamp)

### Rules
- shipment_id must match `SHP-[0-9]+`
- distance_km: 1 to 5000
- weight_tons: 1 to 500
- origin and destination cannot be the same
- event_timestamp must be present and parseable

---

## Contract: telemetry_events (stream)
**Topic / Stream:** `telemetry_events`

### Required Fields
- shipment_id (string)
- speed_kph (int)
- temperature_c (double)
- status (string)
- latitude (double)
- longitude (double)
- event_timestamp (ISO timestamp)

### Rules
- speed_kph: 0 to 200
- temperature_c: -40 to 80
- latitude: -90 to 90
- longitude: -180 to 180
- status in {In Transit, Delayed, Delivered, At Warehouse}

