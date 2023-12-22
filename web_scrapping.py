import requests
from bs4 import BeautifulSoup

# print(help(requests))
url = "https://tabanpuanlari.net"
istek = requests.get(url)
html_icerik = istek.content;
soup = BeautifulSoup(html_icerik, "html.parser");
# print(soup);

sorgu = soup.findAll("a", {"class":"btn btn-primary my-2"});
clean_list = ["LGS","YKS","DGS","TUS","DUS","MSÜ"]
alan = "Yks"
uniler = []
for i in sorgu:
    if(alan.upper() == str(i.text).split(" ")[0]):
        print(i.text,url+i["href"])

        if(str(i.text).find("Puan")>0):
           continue


        url2 = url+i["href"]
        istek2 = requests.get(url2)
        html_icerik2 = istek2.content
        soup2 = BeautifulSoup(html_icerik2,"html.parser")
        sorgu2 = soup2.find("tbody")

        for j in sorgu2:
            ifade = str(j.text).replace("\n","")
            if len(ifade)>2:
                uniler.append(ifade)


print(uniler)











