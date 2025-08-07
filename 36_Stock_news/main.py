import requests
import pyperclip
import datetime as dt
print("HOLA")
TODAY = dt.datetime.now().date()
YESTERDAY = TODAY - dt.timedelta(days=1)
DAY_BEFORE_YESTERDAY = YESTERDAY - dt.timedelta(days=1)
print(DAY_BEFORE_YESTERDAY)
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_STOCK_KEY = "xxx"
API_NEWS_KEY= "xxx"


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={API_STOCK_KEY}"

r = requests.get(url)
stock_data = r.json()
try:
    pyperclip.copy(stock_data)
    yesterday_close_price = float(stock_data["Time Series (Daily)"][str(YESTERDAY)]["4. close"])
    day_before_yesterday_close_price= float(stock_data["Time Series (Daily)"][str(DAY_BEFORE_YESTERDAY)]["4. close"])

except KeyError:
    print("There is not data for yesterday please try again later")
else:
    difference = (yesterday_close_price - day_before_yesterday_close_price)
    relative_difference = (difference / yesterday_close_price) * 100
    print(relative_difference)

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator

news_params= {"apiKey": API_NEWS_KEY,
              "language": "en",
              "qInTitle": COMPANY_NAME,
              }

response=requests.get(NEWS_ENDPOINT, params=news_params)
response.raise_for_status()
articles= response.json()["articles"]
print(articles)
first_articles = articles[:3]


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.

formatted_messages= [f"Headline: {article['title']}\nBrief: {article['description']}" for article in first_articles]

import smtplib
from email.message import EmailMessage

title= f"TESLA 🔺{round(relative_difference)}%" if relative_difference>=0 else f"TESLA 🔻{round(-relative_difference)}%"
my_email_gmail = "email@email.com"
my_password = "xxx"

for message in formatted_messages:
    msg = EmailMessage()
    msg["Subject"] = title
    msg["From"] = my_email_gmail
    msg["To"] = my_email_gmail
    msg.set_content(message)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(my_email_gmail, my_password)
        connection.send_message(msg)

    del msg




#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

