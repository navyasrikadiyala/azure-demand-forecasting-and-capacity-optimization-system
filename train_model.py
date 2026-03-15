import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# load dataset
data = pd.read_csv("clean_bakery_demand.csv")

print("Dataset Preview:")
print(data.head())

# convert date
data["Date"] = pd.to_datetime(data["Date"])

# create features
data["day"] = data["Date"].dt.day
data["month"] = data["Date"].dt.month

# features and target
X = data[["day","month"]]
y = data["Demand"]

# split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training model...")

# train model
model = LinearRegression()
model.fit(X_train, y_train)

# predictions
pred = model.predict(X_test)

# evaluation
mae = mean_absolute_error(y_test, pred)
rmse = np.sqrt(mean_squared_error(y_test, pred))

print("MAE:", mae)
print("RMSE:", rmse)
from sklearn.ensemble import RandomForestRegressor

# Train Random Forest model
rf = RandomForestRegressor(n_estimators=100)

rf.fit(X_train, y_train)

# Predict using Random Forest
rf_pred = rf.predict(X_test)

# Evaluate Random Forest
rf_mae = mean_absolute_error(y_test, rf_pred)
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))

print("\nRandom Forest Results")
print("MAE:", rf_mae)
print("RMSE:", rf_rmse)
import joblib

joblib.dump(rf, "bakery_model.pkl")
print("Model saved successfully")