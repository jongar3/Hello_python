from dotenv import load_dotenv
import os
import pathlib
import requests
import pyperclip
import datetime
LOCAL_DIR = pathlib.Path(__file__).parent
NOW_TIME= datetime.datetime.now().strftime("%H:%M:%S")
TODAY = datetime.datetime.now().strftime("%d/%m/%Y")

load_dotenv()  # Load environment variables from .env file 

nutritionix_api_key = os.getenv("API_KEY")
nutritionix_application_id = os.getenv("APLICATION_ID")

if not nutritionix_api_key or not nutritionix_application_id:
    raise ValueError("API_KEY and APLICATION_ID must be set in the .env file")

nutririonix_endpoint= "/v2/natural/exercise"
nutritionix_header= {
    "x-app-id": nutritionix_application_id,
    "x-app-key": nutritionix_api_key,}

excercise_text = input("Tell me which exercise you did: ")


nutritionix_params = {
    "query": excercise_text,
    "weight_kg": 70,
    "height_cm": 179,
    "age": 21
    }
nutritionix_response = requests.post(
    url=f"https://trackapi.nutritionix.com{nutririonix_endpoint}",
    json=nutritionix_params,
    headers=nutritionix_header)

nutritionix_response.raise_for_status()  # Raise an error for bad responses
new_excercises= nutritionix_response.json()["exercises"]
print(new_excercises)
pyperclip.copy(str(nutritionix_response.json()))

SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_AUTH = os.getenv("SHEETY_AUTH")

sheety_header= {"Authorization": SHEETY_AUTH}
sheety_response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_header)
sheety_response.raise_for_status()  # Raise an error for bad responses

id= sheety_response.json()["workouts"][-1]["id"] # Get the last ID from the Sheety response

for exercise in new_excercises:
    upload = {"date": TODAY, "time": str(NOW_TIME), "exercise": exercise["name"], "duration": exercise["duration_min"], "calories": exercise["nf_calories"]}
    sheety_response = requests.post(
        url=SHEETY_ENDPOINT,
        json={"workout": upload},
        headers=sheety_header)
    
    print(sheety_response.text)


print("\nSheety Response:")
print(sheety_response.json())
