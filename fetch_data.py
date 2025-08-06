import os
import requests
import csv
from datetime import datetime

API_KEY = os.getenv("TWELVE_DATA_API_KEY")
SYMBOL = "SPY"
TYPE = "ETF"
INTERVAL = "1min"
OUTPUT_FILE = "data/spy_data.csv"
START_DATE = "2024-01-01 00:00:00"
END_DATE = datetime.now()

url = f"https://api.twelvedata.com/time_series"
params = {
    "symbol": SYMBOL,
    "type": TYPE,
    "interval": INTERVAL,
    "apikey": API_KEY,
    "start_date": START_DATE,
    "end_date": END_DATE
}

response = requests.get(url, params=params)
data = response.json()

# Dodaj to przed zapisaniem pliku
os.makedirs("data", exist_ok=True)

# Zapisz dane do CSV
with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["datetime", "open", "high", "low", "close", "volume"])
    print(data)  # <--- dodaj to!

    for entry in data["values"]:
        writer.writerow([
            entry["datetime"],
            entry["open"],
            entry["high"],
            entry["low"],
            entry["close"],
            entry["volume"]
        ])

print(f"[{datetime.now()}] Zapisano dane do {OUTPUT_FILE}")
