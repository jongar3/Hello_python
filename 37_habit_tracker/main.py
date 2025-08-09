import requests
import json
import pathlib
import datetime as dt
TODAY = dt.datetime.now() - dt.timedelta(days=4)  # Pixela uses the next day for the current date
formated_today = TODAY.strftime("%Y%m%d")
CURRENT_DIR = pathlib.Path(__file__).parent
pixela_endpoint = "https://pixe.la/v1/users"

try:
     with open(CURRENT_DIR / "data.json", "r") as file:
        user_params = json.load(file)
except FileNotFoundError:
    print("User parameters file not found. Please create 'data.json' with user details.")
    raise FileNotFoundError("User parameters file not found.")
print(user_params)

##1. Create a user

# response=requests.post(pixela_endpoint, json=user_params)
# print(response.text)

##2. Create a graph
graph_endpoint = f"{pixela_endpoint}/{user_params["username"]}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Habit",
    "unit": "hours",
    "type": "float",
    "color": "ichou",}

headers = {
    "X-USER-TOKEN": user_params["token"]}   

response = requests.post(graph_endpoint, json=graph_config, headers=headers)
print(response.text) 

##3. Post a pixel
amount= (input("How many hours did you code today? "))
post_pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"
pixel_data = {
    "date": formated_today,
    "quantity": amount
}

response = requests.post(post_pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)