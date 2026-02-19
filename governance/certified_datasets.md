# Certified Datasets (Gold Layer)

## What "Certified" Means
A dataset is certified when it is:
- validated against the contract
- deduplicated and standardized
- monitored via quality checks
- documented for downstream consumers

---

## Gold Dataset 1: gold_shipment_lifecycle
### Purpose
One row per shipment event stage for lifecycle analytics.

### Key Fields
- shipment_id
- origin
- destination
- status
- event_timestamp
- distance_km
- weight_tons

### Consumers
- operations reporting
- on-time performance dashboards

---

## Gold Dataset 2: gold_hub_dwell_time
### Purpose
Measure dwell time at hubs (yard/terminal delays).

### KPI Outputs
- avg_dwell_minutes by hub
- top delay hubs per day

---

## Gold Dataset 3: gold_on_time_performance
### Purpose
On-time delivery metrics per corridor.

### KPI Outputs
- on_time_pct
- avg_delay_minutes

