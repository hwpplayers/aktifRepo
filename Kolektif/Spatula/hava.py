import requests
from bs4 import BeautifulSoup

def havaDurumu(sehir):
    url = f"https://www.google.com/search?&q={sehir}+hava+durumu" + "&lr=lang_tr&hl=tr"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    istek = requests.get(url, kimlik)
    corba = BeautifulSoup(istek.text, "lxml")

    gun_durum = corba.findAll('div', class_='BNeawe')
    gun, durum = gun_durum[3].text.strip().split('\n')
    derece = corba.find('div', class_='BNeawe').text

    liste = []
    sozluk = {
        'sehir'     : sehir.capitalize(),
        'gun'       : gun,
        'derece'    : f'{durum} {derece}',
    }

    liste.append(sozluk)

    return liste

# print(havaDurumu('Çanakkale Merkez'))

import json

jsonGorsel = lambda sehir: json.dumps(havaDurumu(sehir), indent=2, sort_keys=False, ensure_ascii=False)
# print(havaDurumu('Çanakkale Merkez'))

anahtarlar = lambda sehir: [anahtar for anahtar in havaDurumu(sehir)[0].keys()]
# print(anahtarlar('Çanakkale Merkez'))