import requests
import os

def fetch_ip_address():
  data = requests.get("https://ifconfig.me")
  print(f"Your router IP address is : {data.text}")

def getPictureOfTheDay():
    data = requests.get(f"https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
    print("Votre image du jour est disponible :", data.json()['url'])

fetch_ip_address()
getPictureOfTheDay()
