import plotly.express as px

def plot_anomalies(df, shock_df, drift_df):
    fig = px.line(df, x='timestamp', y='acceleration_g', title='Acceleration Over Time')
    fig.add_scatter(x=shock_df['timestamp'], y=shock_df['acceleration_g'],
                    mode='markers', name='Shock Events', marker=dict(color='red'))
    fig.show()

    fig2 = px.line(df, x='timestamp', y='temperature_C', title='Temperature Over Time')
    fig2.add_scatter(x=drift_df['timestamp'], y=drift_df['temperature_C'],
                     mode='markers', name='Thermal Drift', marker=dict(color='orange'))
    fig2.show()
