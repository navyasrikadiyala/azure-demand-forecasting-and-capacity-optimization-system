import pandas as pd

# 1. Load your dataset
df = pd.read_csv("bread basket.csv")

# 2. Convert date_time to real date format
df["date_time"] = pd.to_datetime(df["date_time"])

# 3. Take only the date (remove time)
df["Date"] = df["date_time"].dt.date

# 4. Count how many items sold each day
daily_demand = df.groupby("Date").size().reset_index(name="Demand")

# 5. Show result
print(daily_demand.head())

# 6. Save new clean file
daily_demand.to_csv("clean_bakery_demand.csv", index=False)
