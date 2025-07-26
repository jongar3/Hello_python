import requests
URL= "http://api.open-notify.org/iss-now.json"
response = requests.get(URL)
response.raise_for_status()  # Check for request errors
data_json = response.json()
print(data_json)