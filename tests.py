import requests
import time

BASE_URL = "http://localhost:8000"

# Send first request (Medium priority)
resp1 = requests.post(f"{BASE_URL}/ingest", json={"ids": list(range(1, 6)), "priority": "MEDIUM"})
id1 = resp1.json()["ingestion_id"]

# Wait 4 sec and send High priority
time.sleep(4)
resp2 = requests.post(f"{BASE_URL}/ingest", json={"ids": list(range(6, 10)), "priority": "HIGH"})
id2 = resp2.json()["ingestion_id"]

# Check status periodically
for _ in range(6):
    print("Status:", requests.get(f"{BASE_URL}/status/{id1}").json())
    print("Status:", requests.get(f"{BASE_URL}/status/{id2}").json())
    time.sleep(5)
