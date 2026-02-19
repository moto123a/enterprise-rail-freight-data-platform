-- =========================
-- KPI QUERIES (TRINO)
-- =========================

-- 1) Shipment volume by corridor
SELECT origin, destination, COUNT(*) AS shipment_events
FROM gold_shipment_lifecycle
GROUP BY origin, destination
ORDER BY shipment_events DESC;

-- 2) On-time performance proxy (delivered vs total)
SELECT
  origin,
  destination,
  CAST(SUM(CASE WHEN status = 'Delivered' THEN 1 ELSE 0 END) AS DOUBLE) / COUNT(*) AS delivered_ratio
FROM gold_shipment_lifecycle
GROUP BY origin, destination
ORDER BY delivered_ratio DESC;

-- 3) Delay hotspots by hub (if status exists in dataset)
SELECT
  origin AS hub,
  COUNT(*) AS delayed_events
FROM gold_shipment_lifecycle
WHERE status = 'Delayed'
GROUP BY origin
ORDER BY delayed_events DESC;

-- 4) Telemetry anomaly scan example
SELECT
  shipment_id,
  status,
  speed_kph,
  temperature_c,
  event_timestamp
FROM telemetry_events
WHERE (status = 'In Transit' AND speed_kph = 0)
   OR (temperature_c > 60 OR temperature_c < -30)
ORDER BY event_timestamp DESC;
