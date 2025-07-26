import requests
URL_space_station = "http://api.open-notify.org/iss-now.json"

result_space_station = requests.get(URL_space_station)
result_space_station.raise_for_status()
position_space_station = result_space_station.json()["iss_position"]
latitude, longitud = position_space_station["latitude"], position_space_station["longitude"]

station_position = {"lat": latitude, "lng": longitud}

#URL_sunrise= f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitud}" we can put the parameters directly in the URL or use a dictionary
URL_sunrise = "https://api.sunrise-sunset.org/json"
result_sunrise = requests.get(URL_sunrise, params= station_position )
result_sunrise.raise_for_status()
sunrise_sunset_data = result_sunrise.json()

print(f"The sunset at the actual position of the space station is at {sunrise_sunset_data['results']['sunset']}")