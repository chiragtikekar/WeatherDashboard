# 🌤️ WEATHER DASHBOARD – Microservices-Based Real-Time Weather Monitoring System

A modular weather dashboard built using microservices architecture, providing real-time weather data, location management, and alerts for extreme weather conditions.

---

## 🧠 Project Overview

**WEATHER DASHBOARD** is a microservices-based system that offers real-time weather monitoring. The application features independently running services for location management, real-time weather fetching, and weather alert generation. Using FastAPI and REST APIs, this system is scalable, modular, and easy to extend.

---

## 🛠️ Tech Stack

- **Python**  
- **FastAPI** – for building fast and efficient APIs  
- **OpenWeatherMap API** – for fetching real-time weather data  
- **SQLite** – for lightweight data storage  
- **Requests** – for HTTP requests to external APIs  

---

## 🚀 Features

- 🌍 **Location Management**: Stores cities and location details.  
- 🌦️ **Real-Time Weather Fetching**: Fetches current weather data from OpenWeatherMap API.  
- ⚠️ **Alert Generation**: Triggers notifications based on extreme weather conditions (e.g., storms, heavy rain).  
- 🖥️ **Modular Microservices**: Independent services for each functionality with REST API communication.  
- 🛠️ **Swagger UI**: Auto-generated UI for API testing and exploration.

---

## 📷 How It Works

1. **Location Service**: Manages a list of cities and their associated weather information.
2. **Weather Service**: Fetches real-time weather data from OpenWeatherMap API for the selected city.
3. **Alert Service**: Monitors extreme weather conditions and triggers alerts when necessary.

Each service communicates via REST APIs, ensuring loose coupling and modularity.
