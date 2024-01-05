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

def getir2(sinav_turu, alan):
    alan2 = str(alan).lower().replace(" ", "-")
    url2 = url + f"/{sinav_turu}/bolum/{alan2}"
    print(url2)
    istek = requests.get(url2)
    html_icerik = istek.content
    soup = BeautifulSoup(html_icerik, "html.parser")
    sorgu = soup.find("tbody").find_all("tr")
    bolum = []
    print(sorgu[1])

    for j in sorgu:
        ifade = str(j.text).replace("\n", "")
        print(ifade)
        if len(ifade) > 2:
            bolum.append(ifade)

    print(bolum)







