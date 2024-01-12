import pandas as pd
import requests
from bs4 import BeautifulSoup


istek = requests.get("https://tabanpuanlari.net/dus/hastane/adiyaman-universitesi")
html_icerik = istek.content

soup = BeautifulSoup(html_icerik, 'html.parser')

sorgu = soup.find("tbody").find_all("tr")
liste = []
for i in sorgu:
    liste.append(str(i.text).split("\n")[2])
print(liste)