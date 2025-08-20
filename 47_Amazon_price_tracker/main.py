import requests
from bs4 import BeautifulSoup
import lxml

def send_email():
    print("Send and email. Just copy the code of the day 32")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',  # Define el idioma de la solicitud (en este caso, inglés)
    'Accept-Encoding': 'gzip, deflate, br',  # Para compresión de la respuesta
    'Connection': 'keep-alive'
}

response = requests.get("https://www.amazon.es/Cecotec-Multifunci%C3%B3n-Funciones-Recetario-Integrado/dp/B0BGSRV33C/ref=sr_1_1_sspa?crid=1T2PAAJE2HGDJ&dib=eyJ2IjoiMSJ9.cIBOs0sD0tkesJa4w_BQYdvijrFgWTW95HUEPViFFb6I7HMBF7KSvdkdkP01VWmsezR7DuOFhvhiMfhgVndw9EHt7XTG_JK996g7ZnCOhFHpyJGnVwf38udXD9I6mU1ImdKq4a842X9Xyltsj9gaqrPikWvGPiLDIlWv0CQEQsqz-zAB7PTaSjr3-nkAYo0EDsGcBcZCfGOwVRq6bldFDnaQhIKgYpjwXus582NrQRZhN9Qa-OTSm8Q4ZPM_S_i2R2SeugFFzIj1uuIOo1sy26e-SVccXzTUDEzm6DmU2O8.1aIx4gSUYhP1_jhMLEf0v0ewk01OPX5mWGgTa0k0O18&dib_tag=se&keywords=thermomix&qid=1755679777&sprefix=thermo%2Caps%2C117&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1", headers=headers)
response.raise_for_status()  # Check if the request was successful

soup = BeautifulSoup(response.content, 'lxml')

price= soup.select_one("span.a-price-whole")
price_fraction = soup.select_one("span.a-price-fraction")

print(f"Price: {price.text[:-1]}.{price_fraction.text}" if price and price_fraction else "Price not found")

if int(price.text[:-1])<325:
    print("The price is below 325 euros.")
    send_email()

