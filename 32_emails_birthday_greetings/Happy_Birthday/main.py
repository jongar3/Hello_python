import smtplib
import datetime as dt
import random
import pandas as pd
import pathlib
from email.message import EmailMessage
MY_EMAIL="jongarcicuevas@gmail.com"
PASSWORD= "XXX" # Replace with your actual password

PROJECT_DIR = pathlib.Path(__file__).parent
day= dt.datetime.now().day
month= dt.datetime.now().month
today = (month, day)

with open(PROJECT_DIR / "birthdays.csv") as file:
    data = pd.read_csv(file)
    birthdays_today=data[(data.month == month) & (data.day == day)]
    print(birthdays_today)

if birthdays_today.empty:
    print("No birthdays today.")
else:
    with open(PROJECT_DIR / "letter_templates" / f"letter_{random.randint(1, 3)}.txt") as file:
        letter_template = file.read()
        print(letter_template)

    for index, row in birthdays_today.iterrows():
        letter = letter_template.replace("[NAME]", row["name"])
        recipient_email = row["email"]
        
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            msg = EmailMessage()
            msg["Subject"] = "Happy Birthday! "+ row["name"]
            msg["From"] = MY_EMAIL
            msg["To"] = recipient_email
            msg.set_content(letter)
            connection.send_message(msg)
        print(f"Email sent to {recipient_email}!")

    