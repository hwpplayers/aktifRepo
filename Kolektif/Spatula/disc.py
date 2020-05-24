import requests
from bs4 import BeautifulSoup

def udemySpatula(kategori):
    link = f"https://www.discudemy.com/s-r/{kategori}.jsf"
    istek = requests.get(link)
    corba = BeautifulSoup(istek.content, 'lxml')

    udemy = []

    for tek in corba.findAll('section', class_="card"):
        dil = tek.find('label', class_='ui green disc-fee label')
        if dil.text.lower() == 'ads':
            continue

        baslik = tek.find('div', class_='header')

        discLink = requests.get('https://www.discudemy.com/go/' + baslik.a['href'].split('/')[-1])
        discCorba = BeautifulSoup(discLink.content, 'lxml')
        baglanti = discCorba.select('body > div.ui.container.mt10 > div:nth-child(3) > div > a')[0]['href']

        udemy.append({
            'dil': dil.text,
            'baslik': baslik.text.strip(),
            'baglanti': baglanti
        })

    return udemy

import json
jsonCikti = lambda kategori: json.dumps(udemySpatula(kategori), indent=2, sort_keys=False, ensure_ascii=False)
# print(jsonCikti('python'))

import pandas as pd
pandaVeri = lambda kategori: pd.DataFrame(udemySpatula(kategori))
# print(pandaVeri('python'))

from tabulate import tabulate
gorselVeri = lambda kategori: tabulate(pandaVeri(kategori), headers='keys', tablefmt='psql')
# print(gorselVeri('python'))