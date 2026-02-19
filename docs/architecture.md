# Enterprise Rail Freight Data Platform — Architecture

## Goal
Convert high-volume real-time freight shipment + telemetry events into certified, analytics-ready datasets for reporting and decision support.

## High-Level Flow
Sources → Streaming Ingestion → Stream Processing → Lakehouse (Bronze/Silver/Gold) → Warehouse Marts → BI/Analytics

### Streaming Ingestion
- Kafka topic(s): `freight_events`, `telemetry_events`
- Optional cloud ingestion: Kinesis stream for managed ingestion paths

### Stream Processing
- Spark Structured Streaming: parsing, enrichment, dedup, standardization
- Flink: low-latency event-time processing (watermarks / late events) — conceptual module

### Storage Layers
**Bronze (Raw)**
- Append-only raw JSON events
- Minimal validation, schema-on-read

**Silver (Cleaned)**
- Standardized types, deduplicated, basic quality checks
- Normalized location and status fields

**Gold (Certified)**
- Business-ready datasets:
  - On-time performance
  - Dwell time by hub
  - Delay reasons summary
  - Shipment lifecycle fact table

### Query + Warehouse
- Trino for interactive SQL on lakehouse tables
- Redshift for dimensional marts (star schema) powering BI dashboards

## Governance
- Dataset contracts (schema + required fields)
- Certified dataset definitions (Gold)
- Data quality checks (nulls, ranges, referential integrity)

## Security + Compliance (high level)
- Principle of least privilege for data access
- PII exclusion and masking strategies (if applicable)
- Audit-ready logging and lineage concepts
