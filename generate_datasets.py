import pandas as pd
import random

# Number of entries
num_entries = 5000

# Define possible values for weather and road conditions
weather_conditions = ["sunny", "rainy", "snowy", "cloudy", "stormy", "foggy"]
road_conditions = ["dry", "wet", "icy", "damaged", "gravel"]
risk_levels = ["low", "medium", "high"]

# Generate road dataset
road_data = {
    "latitude": [round(random.uniform(-90, 90), 6) for _ in range(num_entries)],
    "longitude": [round(random.uniform(-180, 180), 6) for _ in range(num_entries)],
    "road_condition": [random.choice(road_conditions) for _ in range(num_entries)],
    "risk_level": [random.choice(risk_levels) for _ in range(num_entries)]
}

road_df = pd.DataFrame(road_data)
road_df.to_csv("datasets/road_data.csv", index=False)

# Generate weather dataset
weather_data = {
    "latitude": road_data["latitude"],  # Matching latitudes for merging
    "longitude": road_data["longitude"],  # Matching longitudes for merging
    "weather_condition": [random.choice(weather_conditions) for _ in range(num_entries)]
}

weather_df = pd.DataFrame(weather_data)
weather_df.to_csv("datasets/weather_data.csv", index=False)

print("Datasets generated successfully!")
