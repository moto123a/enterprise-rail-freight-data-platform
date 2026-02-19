CREATE TABLE freight_lakehouse.shipment_events (
shipment_id STRING,
origin STRING,
destination STRING,
distance_km INT,
weight_tons INT,
event_timestamp TIMESTAMP
)
USING ICEBERG;

