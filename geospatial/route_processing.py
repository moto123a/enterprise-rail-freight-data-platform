from math import radians, sin, cos, sqrt, atan2

def haversine_km(lat1, lon1, lat2, lon2):
    # Great-circle distance to make "geospatial" credible
    R = 6371.0
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return round(R * c, 2)

def classify_route(distance_km: int):
    if distance_km >= 1500:
        return "Long Haul"
    if distance_km >= 600:
        return "Mid Haul"
    return "Short Haul"

def detect_anomaly(speed_kph: int, status: str):
    if status == "In Transit" and speed_kph == 0:
        return "Potential Stop/Delay"
    if status == "Delivered" and speed_kph > 10:
        return "Status-Speed Mismatch"
    return "Normal"

