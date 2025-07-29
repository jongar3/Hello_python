import requests
import datetime
import time 
# You can do it with twilio API, with an sms, in this case I going to just send an email
import smtplib
from email.message import EmailMessage
my_email_gmail = "jongarcicuevas@gmail.com"
my_password = "oirb ohgq ixrc gaxs "
KEY= "e69432f9972cb16e451fb37ac06ae87f"
LON, LAT= -1.97499, 43.31283

URL=f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={KEY}&units=metric"
URL2=f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={KEY}&units=metric"
URL2+= "&exclude=daily,minutely,current"

def mainloop():
    now_hour = datetime.datetime.now().hour
    if now_hour==7:
        response = requests.get(URL2)
        response.raise_for_status()
        weather_data = response.json()
        rain_today = False
        for weather_3hours_step in weather_data["list"][0:5]:
            if weather_3hours_step["weather"][0]["id"] < 700:
                rain_today = True
                break

        if rain_today:
            msg = EmailMessage()
            msg["Subject"] = "Take an umbrella!"
            msg["From"] = my_email_gmail
            msg["To"] = my_email_gmail
            msg.set_content("It is going to rain today, take an umbrella!")
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
                connection.login(my_email_gmail, my_password)
                connection.send_message(msg)
                print("Email sent successfully.")
   
    print("wait an hour")
    time.sleep(60*60)  # Wait 23 houres before checking again     
    mainloop()


mainloop()