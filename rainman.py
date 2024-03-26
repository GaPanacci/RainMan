import pandas as pd

# This function calculates the chance of rainfall based on meteorological data
def calculate_rainfall_chance(df):

    # Calculate raw rainfall chance score using weighted sums of various meteorological parameters
    df['rainfall_chance'] = (
            0.3 * df['Relative_Humidity(%)'] +
            0.2 * df['DPT(℃)'] +
            -0.1 * df['VPD(kPa)'] +
            0.1 * df['Abs Humidity(g/m³)'] +
            0.05 * df['Temperature_Celsius(℃)']).round(2)

    # Normalize the rainfall chance scores to a percentage scale, making it easier to interpret
    df['rainfall_chance_percent'] = (
            (df['rainfall_chance'] - df['rainfall_chance'].min()) /
            (df['rainfall_chance'].max() - df['rainfall_chance'].min()) * 100).round(2)

# Checks if the values in a Pandas Series are increasing or at least plateauing (not decreasing).
def is_increasing(series):

    return all(series.iloc[i] <= series.iloc[i + 1] for i in range(len(series) - 1))

# Scans the DataFrame for periods where the 'rainfall_chance_percent' is increasing
# and exceeds a specified threshold, indicating a significant chance of rain.
def rain_alert(df, period=30, threshold=85):
    alerts = []
    for end_index in range(period, len(df) + 1):
        window = df.iloc[end_index - period:end_index]
        if is_increasing(window['rainfall_chance_percent']) and window['rainfall_chance_percent'].iloc[-1] > threshold:
            start_time = window.iloc[0]['Date']
            alerts.append(start_time)

    if alerts:
        summarized_alerts = summarize_alerts(alerts)
        for start, end in summarized_alerts:
            print(f"Rain alert: Significant chance of rain detected from {start} to {end}.")
    else:
        print("No significant chance of rain detected.")

# Takes a list of datetime strings indicating when rainfall alerts were issued and
# summarizes them into start-end ranges if they are consecutively within 60 seconds of each other.
def summarize_alerts(alerts):

    if not alerts:
        return []
    summarized = [[alerts[0], alerts[0]]]
    for alert in alerts[1:]:
        if (pd.to_datetime(alert) - pd.to_datetime(summarized[-1][1])).total_seconds() <= 60:
            summarized[-1][1] = alert
        else:
            summarized.append([alert, alert])
    return summarized

# Example usage
file_path = r'Enter the location of your CSV data file here'
df = pd.read_csv(file_path)

calculate_rainfall_chance(df)
rain_alert(df)
