# telemetry-anomaly-detector
A time-series analysis pipeline that detects anomalies in sensor data, visualizes them, and flags potential requalification needs.
# Telemetry Anomaly Detector

This project detects shock and thermal drift anomalies in time-series telemetry data from manufacturing tools.

## Features
- Shock detection (>5g)
- Thermal drift detection (>±3℃)
- Interactive dashboard using Dash

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run dashboard: `python dashboard/app.py`

## Sample Data
Located in `data/sample_telemetry.csv`
