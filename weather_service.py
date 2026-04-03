import requests
from config import API_KEY

def get_weather(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"

    response = requests.get(url)
    data = response.json()

    # 🔥 DEBUG (optional)
    print(data)

    # ✅ SAFE CHECK (IMPORTANT)
    if "weather" not in data:
        return "clear"

    weather_main = data["weather"][0]["main"].lower()

    if "rain" in weather_main:
        return "rain"
    elif "storm" in weather_main or "thunderstorm" in weather_main:
        return "storm"
    else:
        return "clear"