import requests
from plyer import notification

# Ask the user to enter any city name
city = input("Enter a city name: ")

# Use Open-Meteo geocoding API to convert the city name into latitude and longitude
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_params = {"name": city, "count": 1}
geo_res = requests.get(geo_url, params=geo_params).json()

# If the city is found, get coordinates and fetch weather
if "results" in geo_res:
    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    # Request current weather for the found coordinates
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": lat,
        "longitude": lon,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "precipitation",
            "rain",
            "snowfall",
            "surface_pressure",
            "cloud_cover",
            "wind_speed_10m",
            "wind_direction_10m",
            "uv_index",
            "visibility"
        ]
    }

    weather_res = requests.get(weather_url, params=weather_params).json()

    # If weather data is available
    if "current" in weather_res:
        cw = weather_res["current"]

        temp = cw["temperature_2m"]
        humidity = cw["relative_humidity_2m"]
        precip = cw["precipitation"]
        rain = cw["rain"]
        snow = cw["snowfall"]
        pressure = cw["surface_pressure"]
        clouds = cw["cloud_cover"]
        wind_speed = cw["wind_speed_10m"]
        wind_dir = cw["wind_direction_10m"]
        uv = cw["uv_index"]
        visibility = cw["visibility"]

        # Format the weather info
        weather_info = (
            f"{city} Weather:\n"
            f"Temperature: {temp}°C\n"
            f"Humidity: {humidity}%\n"
            f"Precipitation: {precip} mm\n"
            f"Rain: {rain} mm\n"
            f"Snowfall: {snow} cm\n"
            f"Pressure: {pressure} hPa\n"
            f"Cloud Cover: {clouds}%\n"
            f"Wind: {wind_speed} km/h ({wind_dir}°)\n"
            f"UV Index: {uv}\n"
            f"Visibility: {visibility} m"
        )

        print(weather_info)

        # Show a desktop notification with the weather details
        notification.notify(
            title="Weather Update",
            message=weather_info,
            timeout=5
        )

    else:
        print("Weather data not found")

else:
    print("City not found")
