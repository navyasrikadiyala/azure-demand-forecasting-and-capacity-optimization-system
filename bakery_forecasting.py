import pandas as pd

# Load processed dataset
df = pd.read_csv("clean_bakery_demand.csv")

print("Dataset Preview:")
print(df.head())

# Simple forecast using moving average
forecast = df["Demand"].rolling(window=7).mean()

print("\nForecast (Last values):")
print(forecast.tail())
