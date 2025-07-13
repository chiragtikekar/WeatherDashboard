import time
import requests
from config import WEATHER_SERVICE_URL, ALERT_TEMPERATURE, ALERT_WIND_SPEED, ALERT_KEYWORDS

def fetch_weather_data():
    try:
        response = requests.get(WEATHER_SERVICE_URL)
        if response.status_code == 200:
            return response.json()
        else:
            print("⚠️ Error fetching weather data.")
            return []
    except Exception as e:
        print("❌ Exception:", e)
        return []

def check_for_alerts(weather_data):
    print("🔎 Checking for alerts...")
    for data in weather_data:
        if "error" in data:
            print(f"❌ Skipping {data['city']} – No data")
            continue

        city = data["city"]
        temp = data["temperature"]
        desc = data["description"].lower()
        wind = data["wind_speed"]

        alerts = []

        if temp > ALERT_TEMPERATURE:
            alerts.append(f"🔥 High Temperature: {temp}°C")
        if wind > ALERT_WIND_SPEED:
            alerts.append(f"💨 High Wind Speed: {wind} m/s")
        if any(keyword in desc for keyword in ALERT_KEYWORDS):
            alerts.append(f"🌧️ Weather Alert: {desc}")

        if alerts:
            print(f"\n🚨 ALERT for {city}:")
            for alert in alerts:
                print(f" - {alert}")
        else:
            print(f"✅ {city}: Weather is normal.")

def start_alert_service(interval=60):
    while True:
        weather_data = fetch_weather_data()
        check_for_alerts(weather_data)
        time.sleep(interval)

if __name__ == "__main__":
    print("🚨 Starting Alert Service...")
    start_alert_service(interval=300)  # Check every 5 minutes
