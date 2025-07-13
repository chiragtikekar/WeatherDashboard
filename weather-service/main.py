from fastapi import FastAPI, HTTPException
import requests
from config import API_KEY, LOCATION_SERVICE_URL

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Weather Service is running"}

@app.get("/weather/{city}")
def get_weather_for_city(city: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="City not found or API error")

    data = response.json()
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }

@app.get("/weather/all")
def get_weather_for_all_cities():
    # Get city list from location-service
    response = requests.get(LOCATION_SERVICE_URL)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error fetching cities from location-service")

    cities = response.json()
    weather_data = []

    for city_obj in cities:
        city = city_obj["city"]
        try:
            weather = get_weather_for_city(city)
            weather_data.append(weather)
        except:
            weather_data.append({"city": city, "error": "Could not fetch weather."})

    return weather_data
