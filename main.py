# App build using Nutritionix and Sheety.

import requests
from datetime import datetime

API_ID = "CREATE YOUR OWN ID IN NUTRITIOXIX"
API_KEY = "CREATE YOUR OWN KEY IN NUTRITIONIX"
WEIGHT = 71
HEIGHT = 180
AGE = 26
GENDER = "enter gender here"

today = datetime.now()

# Endpoints for nutritionix and sheety
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/272e03a70a2fd3c69b412dc7790c7964/client'sWorkouts/workouts"

# Parameters needed for nutritionix
exercise_params = {
    "query": input("What exercises did you do today?"),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

# Authentication header
headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

# Send your query to nutritionix NLP
response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
workouts = response.json()


today_date = today.strftime("%d/%m/%Y")
now_time = today.strftime("%X")

for answer in workouts:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": answer['exercises'][0]['name'].title(),
            "duration": answer['exercises'][0]['duration_min'],
            "calories":answer['exercises'][0]['nf_calories']
        }
    }

    response_sheet = requests.post(url=sheety_endpoint, json=sheet_input)

    print(response_sheet.text)