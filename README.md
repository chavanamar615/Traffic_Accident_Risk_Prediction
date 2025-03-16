Traffic Accident Risk Prediction 🚦
This project predicts the risk of traffic accidents (High Risk or Low Risk) based on geographical coordinates and weather conditions using a machine learning model (Random Forest).

Features:-
Predicts traffic accident risk using latitude, longitude, and weather conditions.
Utilizes a trained Random Forest model for accurate predictions.
Web interface built with Django.
Model trained on historical traffic and weather data.
Project Structure:-
main/: Django app containing views and templates.
prediction_model/: Folder containing the trained model (accident_model.pkl).
templates/: HTML files for the frontend.
static/: CSS for styling the web pages.
dataset/: Folder with road and weather datasets used for training.
How to Run
Clone the repository:
bash
Copy
Edit
git clone https://github.com/username/traffic_accident_prediction.git
cd traffic_accident_prediction
Install dependencies:
nginx
Copy
Edit
pip install -r requirements.txt
Run the server:
nginx
Copy
Edit
python manage.py runserver
Open in your browser:
cpp
Copy
Edit
http://127.0.0.1:8000/
Usage:-
Enter the latitude, longitude, and weather condition in the form.
Click on Predict to get the accident risk level.
