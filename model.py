# Importing Required Libraries
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectFromModel
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.metrics import r2_score

# Load the Dataset
train = pd.read_excel(r'G:\working project\Flight-Fare-Prediction-Web-App-master\Flight-Fare-Prediction-Web-App-master\Data_Train.xlsx', engine='openpyxl')
sample = pd.read_excel(r'G:\working project\Flight-Fare-Prediction-Web-App-master\Flight-Fare-Prediction-Web-App-master\Sample_submission.xlsx', engine='openpyxl')
test = pd.read_excel(r'G:\working project\Flight-Fare-Prediction-Web-App-master\Flight-Fare-Prediction-Web-App-master\Test_set.xlsx', engine='openpyxl')

# Merge Test set with Sample submission
test = pd.concat([test, sample], axis=1)
df = pd.concat([train, test])

# Data Cleaning and Feature Engineering
df.drop(labels=['Route', 'Arrival_Time', 'Duration', 'Additional_Info'], axis=1, inplace=True)
df.dropna(inplace=True)

# Date and Time Feature Extraction
df['Day'] = df['Date_of_Journey'].str.split('/').str[0].astype(int)
df['Month'] = df['Date_of_Journey'].str.split('/').str[1].astype(int)
df['Year'] = df['Date_of_Journey'].str.split('/').str[2].astype(int)
df['Total_Stops'] = df['Total_Stops'].str.replace('non-', '0 ').str.split().str[0].astype(int)
df['Departure_Hour'] = df['Dep_Time'].str.split(':').str[0].astype(int)
df['Departure_Minute'] = df['Dep_Time'].str.split(':').str[1].astype(int)

df.drop(['Date_of_Journey', 'Dep_Time', 'Total_Stops'], axis=1, inplace=True)

# Label Encoding for Categorical Variables
le = LabelEncoder()
df['Airline_Encoded'] = le.fit_transform(df['Airline'].values)
df['Source_Encoded'] = le.fit_transform(df['Source'].values)
df['Destination_Encoded'] = le.fit_transform(df['Destination'].values)

# Drop original categorical columns
df = df.drop(['Airline', 'Source', 'Destination'], axis=1)

# Splitting Data into Train and Test Sets
df_train = df[0:10600]
df_test = df[10600:]
X = df_train.drop(['Price'], axis=1)
y = df_train.Price
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Feature Selection using Lasso Regression
lasso = SelectFromModel(Lasso(alpha=0.005, random_state=0))
lasso.fit(X_train, y_train)
selected_features = X_train.columns[lasso.get_support()]
X_train = X_train[selected_features]
X_test = X_test[selected_features]

# 1. Linear Regression
lr = LinearRegression().fit(X_train, y_train)

# 2. Random Forest Regressor
rf = RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    random_state=42
).fit(X_train, y_train)

# 3. XGBoost
xgb = XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=7,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
).fit(X_train, y_train)

# 4. LightGBM
lgb = LGBMRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=7,
    random_state=42
).fit(X_train, y_train)

# 5. Neural Network (Deep Learning Model)
nn = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=[X_train.shape[1]]),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
])
nn.compile(optimizer='adam', loss='mean_squared_error')
nn.fit(X_train, y_train, epochs=100, batch_size=32, verbose=0)

# Predictions and R² Scores
y_pred_nn = nn.predict(X_test).flatten()

model_performance = {
    'Linear Regression': lr.score(X_test, y_test),
    'Random Forest': rf.score(X_test, y_test),
    'XGBoost': xgb.score(X_test, y_test),
    'LightGBM': lgb.score(X_test, y_test),
    'Neural Network': r2_score(y_test, y_pred_nn)
}

# Display Model Performance
print("Model Performance (R² Scores):")
for model, score in model_performance.items():
    print(f"{model}: {score}")

# Identify Best Model
best_model_name = max(model_performance, key=model_performance.get)
print(f"\nBest Model: {best_model_name}")

# Save Best Model
best_model = {
    'Linear Regression': lr,
    'Random Forest': rf,
    'XGBoost': xgb,
    'LightGBM': lgb,
    'Neural Network': nn
}[best_model_name]

with open('best_model.pkl', 'wb') as file:
    pickle.dump(best_model, file)
