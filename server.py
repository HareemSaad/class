from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import json
import os

app = FastAPI()

OPENWEATHER_API_KEY = "9b967ab787083f654e877c37835d363a"

class WeatherRequest(BaseModel):
    name: str
    location: str
    longitude: float
    latitude: float

@app.post("/weather")
async def get_weather(body: WeatherRequest):

    # 1. Call OpenWeather API
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?lat={body.latitude}&lon={body.longitude}&appid={OPENWEATHER_API_KEY}"
    )

    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error contacting OpenWeather: {e}")

    if res.status_code != 200:
        raise HTTPException(status_code=res.status_code, detail=res.text)

    weather_data = res.json()

    # 2. Build log entry
    log_entry = {
        "input": body.dict(),
        "output": weather_data
    }

    # 3. Append to log.json
    log_filename = "log.json"

    # If file exists, load list; otherwise create new list
    if os.path.exists(log_filename):
        with open(log_filename, "r") as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []
    else:
        logs = []

    logs.append(log_entry)

    # Write back to file
    with open(log_filename, "w") as f:
        json.dump(logs, f, indent=4)

    return {"status": "logged", "data": weather_data}