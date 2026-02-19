-- =========================
-- STAR SCHEMA (WAREHOUSE)
-- =========================

-- Dimensions
CREATE TABLE dim_date (
  date_id       INT PRIMARY KEY,
  full_date     DATE,
  year          INT,
  month         INT,
  day           INT
);

CREATE TABLE dim_location (
  location_id   INT IDENTITY(1,1) PRIMARY KEY,
  location_name VARCHAR(120)
);

CREATE TABLE dim_status (
  status_id     INT IDENTITY(1,1) PRIMARY KEY,
  status_name   VARCHAR(50)
);

-- Facts
CREATE TABLE fact_shipment_events (
  shipment_event_id BIGINT IDENTITY(1,1) PRIMARY KEY,
  shipment_id       VARCHAR(50),
  origin_id         INT REFERENCES dim_location(location_id),
  destination_id    INT REFERENCES dim_location(location_id),
  status_id         INT REFERENCES dim_status(status_id),
  date_id           INT REFERENCES dim_date(date_id),
  distance_km       INT,
  weight_tons       INT,
  event_ts          TIMESTAMP
);

-- Example Mart View (BI-ready)
CREATE VIEW mart_on_time_summary AS
SELECT
  d.full_date,
  o.location_name AS origin,
  dest.location_name AS destination,
  COUNT(*) AS total_events,
  SUM(CASE WHEN s.status_name = 'Delivered' THEN 1 ELSE 0 END) AS delivered_events
FROM fact_shipment_events f
JOIN dim_date d ON f.date_id = d.date_id
JOIN dim_location o ON f.origin_id = o.location_id
JOIN dim_location dest ON f.destination_id = dest.location_id
JOIN dim_status s ON f.status_id = s.status_id
GROUP BY d.full_date, o.location_name, dest.location_name;
