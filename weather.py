# skills/weather.py

import requests
from config import WEATHER_API_KEY, DEFAULT_CITY

def handle(_: str) -> str:
    url = (
        f"http://api.openweathermap.org/data/2.5/weather"
        f"?q={DEFAULT_CITY}&appid={WEATHER_API_KEY}&units=metric"
    )
    try:
        resp = requests.get(url, timeout=10)
        data = resp.json()
    except requests.RequestException as e:
        return f"Error: could not reach weather service ({e})"

    # Check for API errors
    if resp.status_code != 200 or "main" not in data:
        # OpenWeatherMap returns a JSON like {"cod":"404","message":"city not found"}
        err = data.get("message", "unknown error")
        return f"Could not fetch weather data: {err}"

    # Safe to extract now
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    return f"In {DEFAULT_CITY}, it’s {temp}°C with {desc}."

