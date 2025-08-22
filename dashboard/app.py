import dash
from dash import dcc, html
import pandas as pd
from src.data_loader import load_data
from src.anomaly_detector import detect_shock, detect_thermal_drift

app = dash.Dash(__name__)
df = load_data('data/sample_telemetry.csv')
shock_df = detect_shock(df)
drift_df = detect_thermal_drift(df)

app.layout = html.Div([
    html.H1("Telemetry Anomaly Dashboard"),
    dcc.Graph(
        figure={
            'data': [
                {'x': df['timestamp'], 'y': df['acceleration_g'], 'type': 'line', 'name': 'Acceleration'},
                {'x': shock_df['timestamp'], 'y': shock_df['acceleration_g'], 'type': 'scatter', 'name': 'Shock', 'marker': {'color': 'red'}}
            ],
            'layout': {'title': 'Acceleration Over Time'}
        }
    ),
    dcc.Graph(
        figure={
            'data': [
                {'x': df['timestamp'], 'y': df['temperature_C'], 'type': 'line', 'name': 'Temperature'},
                {'x': drift_df['timestamp'], 'y': drift_df['temperature_C'], 'type': 'scatter', 'name': 'Drift', 'marker': {'color': 'orange'}}
            ],
            'layout': {'title': 'Temperature Over Time'}
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
