import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load and merge datasets
road_data = pd.read_csv('dataset/road_data.csv')
weather_data = pd.read_csv('dataset/weather_data.csv')

# Merge datasets on latitude and longitude
data = pd.merge(road_data, weather_data, on=['latitude', 'longitude'])

# Exploratory Data Analysis (EDA)
def perform_eda(data):
    print('Data Info:')
    print(data.info())
    print('\nMissing Values:')
    print(data.isnull().sum())
    print('\nData Description:')
    print(data.describe())

perform_eda(data)

# Feature Engineering
features = data.drop(['accident_severity'], axis=1)
features = pd.get_dummies(features, columns=['weather_condition'])  # Encode categorical data
target = data['accident_severity']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Model Training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'prediction_model/accident_model.pkl')

# Model Evaluation
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f'\nModel Accuracy: {accuracy * 100:.2f}%')
print('\nClassification Report:')
print(classification_report(y_test, predictions))

print("\nModel training and evaluation completed successfully!")
