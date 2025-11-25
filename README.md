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

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Environment variables / .env

The app will read `OPENWEATHER_API_KEY` from the environment if present. To store the key in the project and load it before running the server:

1. Copy the example:

   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and put your real API key on the `OPENWEATHER_API_KEY=` line.

3. Export the variables into your shell session before starting the server:

   ```bash
   # POSIX (bash/zsh)
   set -a
   source .env
   set +a
   ```

Alternatively, set the env var directly:

```bash
export OPENWEATHER_API_KEY=your_real_key_here
```

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
