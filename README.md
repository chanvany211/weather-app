#  Weather Fetcher & Desktop Notifier 

A Python script that fetches **real‑time weather data** for any city using the **Open‑Meteo API** and displays it both in the console and as a **desktop notification**.  
This project demonstrates API usage, JSON parsing, geocoding, and system notifications.

## What This App Does

- Asks the user for a **city name**
- Converts the city into **latitude & longitude** using Open‑Meteo’s geocoding API
- Fetches **current weather data**, including:
  - Temperature  
  - Humidity  
  - Precipitation  
  - Rain  
  - Snowfall  
  - Pressure  
  - Cloud cover  
  - Wind speed & direction  
  - UV index  
  - Visibility  
- Prints the weather details in the terminal
- Sends a **desktop notification** with the same information

##  Features

- 🌍 **City name → coordinates** via geocoding  
- ☁️ **Live weather data** from Open‑Meteo  
- 🔔 **Desktop notification** using `plyer`  
- 🧪 Clean JSON parsing  
- ⚡ No API key required  
- 🧱 Beginner‑friendly structure  

