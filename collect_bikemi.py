import requests
import pandas as pd
from datetime import datetime
import os

STATUS_URL = "https://gbfs.urbansharing.com/bikemi.com/station_status.json"

headers = {
    "Client-Identifier": "student-bikemi-research"
}

OUTPUT_FILE = "bikemi_data.csv"

timestamp = datetime.utcnow()

response = requests.get(STATUS_URL, headers=headers, timeout=20)
data = response.json()

stations = data["data"]["stations"]

rows = []
for s in stations:
    rows.append({
        "timestamp": timestamp,
        "station_id": s["station_id"],
        "num_bikes_available": s.get("num_bikes_available"),
        "num_docks_available": s.get("num_docks_available")
    })

df = pd.DataFrame(rows)

if os.path.exists(OUTPUT_FILE):
    df.to_csv(OUTPUT_FILE, mode="a", header=False, index=False)
else:
    df.to_csv(OUTPUT_FILE, index=False)
