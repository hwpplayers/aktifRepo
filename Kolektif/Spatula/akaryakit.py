import requests
from bs4 import BeautifulSoup

def akaryakitFiyat():
    url = f"https://finans.haberler.com/akaryakit/"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    istek = requests.get(url, kimlik)
    corba = BeautifulSoup(istek.text, "lxml")

    son_guncellenme = corba.select('body > div > div.hbMain.stickyNo > div:nth-child(3) > div > div.col696 > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2)')[0].text
    yakit_turu = []
    fiyati = []

    cerceve = corba.find('div', class_='hbTableContent piyasa')

    for tablo in cerceve:
        for tur in cerceve.findAll('td', {'width' : '50%'}):
            yakit_turu.append(tur.text.replace(' TL',' -- TL'))
        
        for fiyat in cerceve.findAll('td', {'width' : '16%'}):
            fiyati.append(fiyat.text)
        break    

    liste = []
    liste.append({
        'veri_saglayici': '@keyiflerolsun',
        'son_guncellenme': son_guncellenme
        })
        
    for adet in range(0, len(yakit_turu)):
        sozluk = {}
        sozluk['yakit_turu'] = yakit_turu[adet]
        sozluk['fiyati'] = fiyati[adet]
        liste.append(sozluk)

    return liste

# print(akaryakitFiyat())

import json

jsonGorsel = json.dumps(akaryakitFiyat(), indent=2, sort_keys=False, ensure_ascii=False)
# print(jsonGorsel)