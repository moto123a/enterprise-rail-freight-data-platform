SELECT origin, COUNT(*) AS total_shipments
FROM shipment_events
GROUP BY origin;

