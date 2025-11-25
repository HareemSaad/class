## Running the app

Follow these steps from the project root to create a local virtual environment and start the FastAPI server.

```bash
# Create a virtual environment and install dependencies (script included)
./create_venv.sh

# Activate the venv (zsh/bash)
source .venv/bin/activate

# Start the server (uvicorn)
.venv/bin/python -m uvicorn server:app --host 127.0.0.1 --port 8000
```

Notes:

- If you prefer to create the venv manually, run:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  ```
- The app uses the OpenWeather API. `server.py` currently contains a hard-coded key; for safety consider setting an environment variable instead and updating the code to read it (e.g. `OPENWEATHER_API_KEY`).

## POST Request

Use the following example to call the `/weather` endpoint (replace coordinates as needed):

```bash
curl -X POST http://localhost:8000/weather \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Sample City",
    "location": "Test Location",
    "longitude": -118.2437,
    "latitude": 34.0522
  }'
```

The endpoint will append a new entry to `log.json` with the request input and the OpenWeather response.
