import requests
import pandas as pd

INFO_URL = "https://gbfs.urbansharing.com/bikemi.com/station_information.json"

headers = {
    "Client-Identifier": "student-bikemi-research"
}

response = requests.get(INFO_URL, headers=headers)
data = response.json()

stations = data["data"]["stations"]

rows = []
for s in stations:
    rows.append({
        "station_id": s["station_id"],
        "name": s["name"],
        "lat": s["lat"],
        "lon": s["lon"],
        "capacity": s["capacity"]
    })

df = pd.DataFrame(rows)
df.to_csv("bikemi_stations.csv", index=False)

print("Station data saved")
