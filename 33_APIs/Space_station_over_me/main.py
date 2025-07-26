import requests
from datetime import datetime
import smtplib
from email.message import EmailMessage
import time

my_email_gmail= "jongarcicuevas@gmail.com"
PASSWORD="xxx"

MY_LAT = 43.31283 # Your latitude
MY_LONG = -1.97499 # Your longitude

def is_dark():
    return not (time_now.hour <= sunset and time_now.hour >= sunrise)
        
def is_close():
    return (abs(iss_latitude - MY_LAT) <= 5) and (abs(iss_longitude-MY_LONG) <= 5)
    

while True:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.


    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if is_dark() and is_close:
        msg = EmailMessage()
        msg["Subject"] = "LOOK UP"
        msg["From"] = my_email_gmail
        msg["To"] = my_email_gmail
        msg.set_content("Look up! \nThe Space station is over you.")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(my_email_gmail, PASSWORD)
            connection.send_message(msg)
        print("email sended!")
    print(f"ISS position: {iss_latitude}, {iss_longitude}")
    print(f"Sunrise: {sunrise}, Sunset: {sunset}")
    time.sleep(60)
