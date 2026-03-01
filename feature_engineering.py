import pandas as pd

# Load clean dataset (Milestone 1 output)
df = pd.read_csv
# Create lag features
df["Lag1"] = df["Demand"].shift(1)
df["Lag7"] = df["Demand"].shift(7)
("clean_bakery_demand.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Create seasonality features
df["DayOfWeek"] = df["Date"].dt.dayofweek
df["Month"] = df["Date"].dt.month
df["IsWeekend"] = df["DayOfWeek"].isin([5, 6]).astype(int)

# Create trend features
df["RollingMean7"] = df["Demand"].rolling(7).mean()
df["RollingStd7"] = df["Demand"].rolling(7).std()

# Detect demand spikes
df["Spike"] = (
    df["Demand"] > df["Demand"].mean() + df["Demand"].std()
).astype(int)

# Remove missing values
df = df.dropna()

# Save model-ready dataset
df.to_csv("model_ready_bakery_data.csv", index=False)

print("Milestone 2 completed successfully ✅")