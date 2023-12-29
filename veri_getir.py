import requests
from bs4 import BeautifulSoup

url = "https://tabanpuanlari.net"

def getir(value):
    url2 = url + f"/{value}"
    istek = requests.get(url2)
    html_icerik = istek.content
    soup = BeautifulSoup(html_icerik, "html.parser")
    sorgu = soup.find("tbody")
    cities = []
    for j in sorgu:
        ifade = str(j.text).replace("\n", "")
        if len(ifade) > 2:
            cities.append(ifade)

    return cities









