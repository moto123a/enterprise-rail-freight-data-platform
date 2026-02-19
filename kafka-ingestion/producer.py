from kafka import KafkaProducer
import json
import random
import time
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

locations = ["Chicago Yard", "Dallas Hub", "Denver Terminal", "Houston Port"]
destinations = ["Atlanta Freight", "Seattle Terminal", "Phoenix Yard", "Miami Dock"]

while True:
    shipment_event = {
        "shipment_id": f"SHP-{random.randint(10000,99999)}",
        "origin": random.choice(locations),
        "destination": random.choice(destinations),
        "distance_km": random.randint(200,3000),
        "weight_tons": random.randint(5,120),
        "event_timestamp": datetime.utcnow().isoformat()
    }

    producer.send("freight_events", shipment_event)
    print("[Kafka] Sent:", shipment_event)
    time.sleep(2)

