import requests
from bs4 import BeautifulSoup

url = "https://tabanpuanlari.net"

def getir(value):
    url2 = url + f"/{value}"
    istek = requests.get(url2)
    html_icerik = istek.content
    soup = BeautifulSoup(html_icerik, "html.parser")
    sorgu = soup.find("table").find_all("a")

    cities = []
    for j in sorgu:
        ifade = str(j.text).replace("\n", "")
        if len(ifade) > 2:
            cities.append(ifade)

    return cities

def getir2(sinav_turu, alan,part):
    alan2 = str(alan).lower().replace(" ", "-")
    url3 = f"{url}/{str(sinav_turu)}/{str(part)}/{str(alan2)}"
    url2 = url +"/"+str(sinav_turu)+"/"+str(part)+"/"+str(alan2)
    print(str(url3))
    istek = requests.get(url2)
    html_icerik = istek.content
    soup = BeautifulSoup(html_icerik, "html.parser")

    if sinav_turu != "dus":
        sorgu = soup.find("table").find_all("a")

        uni = []
        for i in sorgu:
            uni.append(i.text)
        return uni[::2]
    else:
        sorgu = soup.find("tbody").find_all("tr")
        liste = []
        for i in sorgu:
            liste.append(str(i.text).split("\n")[2])
        return liste

def find(sinav_turu, alan, part):
    alan2 = str(alan).lower().replace(" ", "-").replace(",","")
    url3 = f"{url}/{str(sinav_turu)}/{str(part)}/{str(alan2)}"
    url2 = url + "/" + str(sinav_turu) + "/" + str(part) + "/" + str(alan2)
    print(str(url3))
    istek = requests.get(url2)
    html_icerik = istek.content
    soup = BeautifulSoup(html_icerik, "html.parser")

    print(url3)
    sorgu = soup.find("tbody").find_all("tr")
    liste = []
    for i in sorgu:
        liste.append(str(i.text).split("\n"))
    print(liste)

    return liste



    """
    bolum = []
    print(sorgu[1])

    for j in sorgu:
        ifade = str(j.text).replace("\n", "")
        print(ifade)
        if len(ifade) > 2:
            bolum.append(ifade)

    print(bolum)"""







