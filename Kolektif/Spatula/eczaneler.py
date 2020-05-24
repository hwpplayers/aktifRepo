import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
import json

def nobetciSpatula(il, ilce):
    url = f"https://www.eczaneler.gen.tr/nobetci-{il}-{ilce}"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    istek = requests.get(url, kimlik)
    corba = BeautifulSoup(istek.content, "lxml")
    tablo = corba.find('div', id='nav-bugun')
    #print(tablo.text)

    return tablo
#print(nobetciSpatula("canakkale", "merkez"))

pandaVeri = lambda il, ilce: pd.read_html(str(nobetciSpatula(il, ilce)))[0]
#print(pandaVeri("canakkale", "merkez"))

jsonVeri = lambda il, ilce: json.loads(pandaVeri(il, ilce).to_json(orient='records'))
#print(jsonVeri("canakkale", "merkez"))

jsonCikti = lambda il, ilce: json.dumps(jsonVeri(il, ilce), indent=2, sort_keys=False, ensure_ascii=False)
#print(jsonCikti("canakkale", "merkez"))

gorselVeri = lambda il, ilce: tabulate(pandaVeri(il, ilce), headers='keys', tablefmt='psql')
#print(gorselVeri("canakkale", "merkez"))


anahtarlar = lambda il, ilce: [anahtar for anahtar in jsonVeri(il, ilce)[0].keys()]
#print(anahtarlar('canakkale', 'merkez'))

eczaneAdlari = lambda il, ilce: [tablo['Eczane'] for tablo in jsonVeri(il, ilce)]
#print(eczaneAdlari('canakkale', 'merkez'))

eczaneAdresleri = lambda il, ilce: [tablo['Adresi'] for tablo in jsonVeri(il, ilce)]
#print(eczaneAdresleri('canakkale', 'merkez'))

eczaneTelefonlari = lambda il, ilce: [tablo['Telefonu'] for tablo in jsonVeri(il, ilce)]
#print(eczaneTelefonlari('canakkale', 'merkez'))