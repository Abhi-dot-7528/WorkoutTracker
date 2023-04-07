import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables


# =============Nutritionix API=============

API_ID = os.getenv("NUTRITIONIX_API_ID")
API_KEY = os.getenv("NUTRITIONIX_API_KEY")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = YOUR_GENDER  # Your Gender (str)
WEIGHT_KG = YOUR_WEGHT  # Your Weight in Kg (int)
HEIGHT_CM = YOUR_HEIGHT  # Your Height in cm (int)
AGE = YOUR_AGE  # Your age (int)

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

exercise_input = input("Tell me which exercise you did today: ")
user_params = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=user_params, headers=headers)
result = response.json()


# =============Sheety API=============

SHEETY_ENDPOINT = "https://api.sheety.co/"
USERNAME = os.getenv("SHEETY_USERNAME")
PROJECT_NAME = "myWorkouts"
SHEET_NAME = "workouts"
sheety_endurl = f"{SHEETY_ENDPOINT}/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"

today = datetime.now()

for e in result["exercises"]:
    data = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%I:%M:%S %p"),
            "exercise": e["name"].title(),
            "duration": e["duration_min"],
            "calories": e["nf_calories"]
        }
    }

    headers = {
        "Authorization": f"Bearer {os.environ.get('SHEETY_TOKEN')}"
    }
    sheety_response = requests.post(url=sheety_endurl, json=data, headers=headers)
    # print(sheety_response.text)
