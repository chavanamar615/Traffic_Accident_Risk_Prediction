from django.shortcuts import render
import pandas as pd
import numpy as np
import joblib
import os
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def predict(request):
    if request.method == 'POST':
        # Getting data from the form
        latitude = float(request.POST.get('latitude', 0))
        longitude = float(request.POST.get('longitude', 0))
        weather_condition = request.POST.get('weather_condition', '')

        try:
            # Load the trained model
            model_path = os.path.join(settings.BASE_DIR, 'main', 'prediction_model', 'accident_model.pkl')
            model = joblib.load(model_path)

            # Encode weather condition (example for three types)
            weather_encoded = {
                'Clear': [1, 0, 0],
                'Fog': [0, 1, 0],
                'Rainy': [0, 0, 1]
            }.get(weather_condition, [0, 0, 0])

            # Create a DataFrame with the input data
            input_data = pd.DataFrame([[latitude, longitude] + weather_encoded],
                                      columns=['latitude', 'longitude', 
                                               'weather_condition_Clear', 
                                               'weather_condition_Fog', 
                                               'weather_condition_Rainy'])

            # Make the prediction
            prediction = model.predict(input_data)[0]
            result = "High Risk" if prediction == 1 else "Low Risk"
        except Exception as e:
            result = f"Error: {str(e)}"

        return render(request, 'predict.html', {'result': result})

    return render(request, 'predict.html')
