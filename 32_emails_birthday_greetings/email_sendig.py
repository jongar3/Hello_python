import smtplib
import pathlib
import random
FILE_PATH = pathlib.Path(__file__).parent / "quotes.txt"
PASSWORD= "XXX"  # Replace with your actual password
with open(FILE_PATH) as f:
    frases= f.read().splitlines()

my_email_gmail= "jongarcicuevas@gmail.com"
my_email_yahoo= "jongarcicuevas@yahoo.com"

connection= smtplib.SMTP("smtp.gmail.com", 587) #for yahoo host= smtp.mail.yahoo.com and for gmail smtp.gmail.com
connection.starttls() #"securing the email"
connection.login(user= my_email_gmail, password= PASSWORD)
connection.sendmail(from_addr=my_email_gmail, to_addrs=my_email_yahoo, msg= "Subject: Hello Python! \n\n" + random.choice(frases))

connection.close()


