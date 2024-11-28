import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_ip_address():
  data = requests.get(os.environ['IF_CONFIG_URL'])
  print(f"Your router IP address is : {data.text}")

def getPictureOfTheDay():
    data = requests.get(f"{os.environ['APOD_URL']}?api_key={os.environ.get('APOD_KEY', 'DEMO_KEY')}")
    print(
      "Votre image du jour est disponible :", data.json()['url'])

fetch_ip_address()
getPictureOfTheDay()
