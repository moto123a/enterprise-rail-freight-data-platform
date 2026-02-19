from kafka import KafkaProducer
import json
import random
import time
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

origins = ["Chicago Yard", "Dallas Hub", "Denver Terminal", "Houston Port"]
destinations = ["Atlanta Freight", "Seattle Terminal", "Phoenix Yard", "Miami Dock"]
statuses = ["In Transit", "Delayed", "Delivered", "At Warehouse"]

def random_coords_for_city(city: str):
    # Rough dummy coordinates to make geospatial believable
    mapping = {
        "Chicago Yard": (41.8781, -87.6298),
        "Dallas Hub": (32.7767, -96.7970),
        "Denver Terminal": (39.7392, -104.9903),
        "Houston Port": (29.7604, -95.3698),
        "Atlanta Freight": (33.7490, -84.3880),
        "Seattle Terminal": (47.6062, -122.3321),
        "Phoenix Yard": (33.4484, -112.0740),
        "Miami Dock": (25.7617, -80.1918),
    }
    base = mapping.get(city, (40.0, -90.0))
    # add small noise
    return (base[0] + random.uniform(-0.05, 0.05), base[1] + random.uniform(-0.05, 0.05))

while True:
    shipment_id = f"SHP-{random.randint(10000, 99999)}"
    origin = random.choice(origins)
    destination = random.choice(destinations)

    freight_event = {
        "shipment_id": shipment_id,
        "origin": origin,
        "destination": destination,
        "distance_km": random.randint(200, 3000),
        "weight_tons": random.randint(5, 120),
        "event_timestamp": datetime.utcnow().isoformat()
    }

    # Telemetry event for same shipment_id
    lat, lon = random_coords_for_city(origin)
    telemetry_event = {
        "shipment_id": shipment_id,
        "speed_kph": random.randint(0, 120),
        "temperature_c": round(random.uniform(-10, 45), 2),
        "status": random.choice(statuses),
        "latitude": round(lat, 6),
        "longitude": round(lon, 6),
        "event_timestamp": datetime.utcnow().isoformat()
    }

    producer.send("freight_events", freight_event)
    producer.send("telemetry_events", telemetry_event)

    print("[Kafka] freight_events:", freight_event)
    print("[Kafka] telemetry_events:", telemetry_event)

    time.sleep(2)
