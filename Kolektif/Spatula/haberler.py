import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate

url = "https://www.ntv.com.tr/son-dakika"
kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
istek = requests.get(url, kimlik)
soup = BeautifulSoup(istek.text, "lxml")

haberVerisi = []

for table in soup.findAll("ul", class_="gallery-page-video-list-items"):
    # print(table)
    # print(table.tr.text)
    haberManset = table.findAll("div", class_="card-text-wrapper")

    for adet in range(len(haberManset)):
        haberVerisi.append({
            "Haber" : haberManset[adet].p.text.strip().replace('SON DAKİKA HABERİ:',''),
            "Link" : "https://www.ntv.com.tr" + haberManset[adet].a['href']
        })

#print(haberVerisi)