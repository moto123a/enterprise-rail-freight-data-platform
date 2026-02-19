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
