# 🚆 Real-Time Rail Logistics Shipment Tracking Pipeline (Enterprise Data Platform)

## Overview
This repository demonstrates an enterprise-style **real-time data engineering platform** for rail freight shipment tracking. It ingests streaming shipment + telemetry events, applies **streaming ETL**, publishes **certified datasets (Gold)**, and serves analytics through **Trino SQL** and a **Redshift star schema**.

This project is intentionally structured to mirror real-world data platform patterns:
- **Bronze / Silver / Gold** lakehouse layers  
- **Certified datasets** + dataset contracts  
- **Streaming + batch compatibility**  
- **Warehouse marts (star schema)** for BI  

---

## Architecture
**Kafka (freight_events, telemetry_events)**  
→ **Spark Structured Streaming** (parse, standardize, validate)  
→ **Lakehouse layers (Bronze/Silver/Gold)**  
→ **Trino** (KPI analytics queries)  
→ **Redshift** (dimensional marts / star schema)  
→ **Airflow** (Bronze→Silver→Gold→Warehouse orchestration)

---

## Tech Stack
- **Streaming:** Kafka, Spark Structured Streaming (Spark)
- **Orchestration:** Apache Airflow (Bronze/Silver/Gold)
- **Lakehouse Concepts:** Delta Lake, Apache Iceberg (architecture/governance)
- **Query Engine:** Trino (KPI queries)
- **Warehouse:** AWS Redshift (star schema + marts)
- **Languages:** Python, SQL
- **Geospatial Concepts:** Haversine distance + route classification (basic)

---

## Repo Structure

kafka-ingestion/ # Producers for freight + telemetry streams
spark-stream-processing/ # Spark streaming consumer / transformations
airflow-orchestration/ # Airflow DAG for Bronze→Silver→Gold→Warehouse
warehouse/ # Star schema (dims/facts) + BI mart view
trino-query/ # KPI queries (SQL) for analytics
docs/ # Architecture + dataset contracts documentation
governance/ # Certified datasets definitions
geospatial/ # Route logic + anomaly helper functions


---

## What This Platform Produces (Gold / Certified)
- **gold_shipment_lifecycle:** shipment events standardized for reporting
- **gold_hub_dwell_time:** dwell-time KPI outputs by hub/terminal (concept)
- **gold_on_time_performance:** on-time / delivered-ratio KPIs by corridor (concept)

---

## Data Governance
- **Dataset contracts:** required fields + validation rules  
  See: `docs/dataset_contracts.md`
- **Certified datasets definitions:** Gold layer expectations  
  See: `governance/certified_datasets.md`

---

## KPI Queries (Trino)
Sample queries included:
- Shipment volume by corridor  
- Delivered ratio / on-time proxy by corridor  
- Delay hotspots by hub  
- Telemetry anomaly scan (speed/status/temp rules)  

See: `trino-query/analytics_queries.sql`

---

## Redshift Dimensional Model (Star Schema)
- `dim_date`, `dim_location`, `dim_status`
- `fact_shipment_events`
- `mart_on_time_summary` view

See: `warehouse/star_schema.sql`

---

## Why This Looks “Enterprise” (Not a Toy)
- Clean separation of ingestion, processing, orchestration, governance, and marts  
- Bronze/Silver/Gold layering + certified datasets  
- Streaming + batch compatible modeling  
- Query + warehouse patterns used in production data platforms  

---

## Author
**Pavan Krishna**  
Software Engineer | Data & Streaming Systems  
pavankrishna310@gmail.com
