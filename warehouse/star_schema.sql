CREATE TABLE dim_location(
location_id INT,
location_name VARCHAR(100)
);

CREATE TABLE fact_shipments(
shipment_id VARCHAR(50),
origin_id INT,
destination_id INT,
distance_km INT,
weight_tons INT
);

