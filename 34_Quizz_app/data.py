""""Get question data from the quiz API."""

import requests
URL= "https://opentdb.com/api.php?amount=10&type=boolean"
response = requests.get(URL)
response.raise_for_status()  # Check for request errors
question_data= response.json()
