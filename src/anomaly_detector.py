def detect_shock(df, threshold=5.0):
    return df[df['acceleration_g'] > threshold]

def detect_thermal_drift(df, threshold=3.0, baseline=25.0):
    drift = df[abs(df['temperature_C'] - baseline) > threshold]
    return drift
