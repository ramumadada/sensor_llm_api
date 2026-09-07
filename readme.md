# Sensor LLM API

## Overview

This project simulates sensor readings, stores them in a local SQLite database, exposes the data through a Flask REST API, and uses the Gemini LLM API to generate a short plain-English insight from the sensor data.

The project demonstrates a simple backend workflow that can later be adapted for real sensor or Edge AI applications.

## Architecture

```text
Fake Sensor
     ↓
SQLite Database
     ↓
Flask REST API
     ↓
Python Statistics
     ↓
Gemini LLM
     ↓
Plain-English Insight
     ↓
JSON Response
```

## Technologies

* Python
* Flask
* SQLite
* Google Gemini API
* python-dotenv
* REST API
* Git

## Project Structure

```text
sensor_llm_api/
│
├── app.py              # Flask REST API
├── sensor.py           # Generates fake sensor readings
├── database.py         # SQLite database operations
├── llm.py              # Gemini LLM integration
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
├── .gitignore          # Files excluded from Git
├── README.md           # Project documentation
│
└── data/
    └── sensor.db       # Local SQLite database
```

## How to Run

### 1. Create and activate the virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the Gemini API key

Create a `.env` file:

```text
GEMINI_API_KEY=your_api_key_here
```

The `.env` file is intentionally excluded from Git so the API key is not committed.

### 4. Start the Flask application

```bash
python app.py
```

The API will run at:

```text
http://127.0.0.1:5000
```

## API Endpoints

### GET `/readings`

Returns the sensor readings stored in SQLite.

Example:

```bash
curl http://127.0.0.1:5000/readings
```

Response:

```json
{
  "count": 10,
  "readings": [
    {
      "id": 1,
      "timestamp": "2026-09-07T09:30:00",
      "temperature": 28.42,
      "weight": 51.37
    }
  ]
}
```

### GET `/insight`

Calculates basic statistics from the stored sensor readings and sends them to Gemini to generate a plain-English explanation.

Example:

```bash
curl http://127.0.0.1:5000/insight
```

Response:

```json
{
  "statistics": {
    "temperature_avg": 28.85,
    "temperature_min": 25.1,
    "temperature_max": 33.52,
    "weight_avg": 49.46,
    "weight_min": 45.86,
    "weight_max": 56.36
  },
  "insight": "The temperature and weight readings show moderate variability rather than remaining perfectly stable."
}
```

## Why This Was Built

The project combines several backend concepts into one practical workflow:

* Generating sensor-like data
* Persisting data using SQLite
* Building REST API endpoints with Flask
* Performing basic data analysis
* Integrating an LLM API
* Managing API keys using environment variables
* Using Git for version control

This provides a foundation for connecting real sensor data to backend services and AI-based analysis.



## Project Status

Completed as a backend/LLM integration mini-project demonstrating sensor simulation, SQLite storage, REST API development, and Gemini-based data insights.
