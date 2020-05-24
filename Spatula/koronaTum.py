import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate

istek = requests.get("https://www.worldometers.info/coronavirus/")
corba = BeautifulSoup(istek.content, 'lxml')
tablo = corba.find('table', id='main_table_countries_today')

pandaVeri = pd.read_html(str(tablo))[0].rename(
    columns={
        'Country,Other'     : 'Ülkeler',
        'TotalCases'        : 'Toplam Vaka',
        'NewCases'          : 'Yeni Vaka',
        'TotalDeaths'       : 'Toplam Ölüm',
        'NewDeaths'         : 'Yeni Ölüm',
        'TotalRecovered'    : 'Toplam Taburcu',
        'ActiveCases'       : 'Aktif Vaka',
        'Serious,Critical'  : 'Kritik Vaka',
        'Tot Cases/1M pop'  : 'Vaka/Nüfus Oranı',
        'Deaths/1M pop'     : 'Ölüm/Nüfus Oranı',
        'TotalTests'        : 'Toplam Test',
        'Tests/ 1M pop'     : 'Test/Nüfus Oranı'
    }
)

gorselVeri = tabulate(pandaVeri, headers='keys', tablefmt='psql')
#print(gorselVeri)

import json

sozluk = {
    "Veri Kaynağı": "https://www.worldometers.info/coronavirus/",
    "Veri Sağlayıcısı": "@keyiflerolsun",
    "Veri" : json.loads(pandaVeri.to_json(orient='records'))
}

jsonVeri = json.dumps(sozluk, indent=2, sort_keys=False, ensure_ascii=False)

#print(jsonVeri)

#with open("koronaVeri.json", "w+") as dosya: dosya.write(jsonVeri)







def dene(ulke):
    for veri in range(len(sozluk['Veri'])):
        ara = sozluk['Veri'][veri]['Country,Other']
        if ara == ulke: return print(sozluk['Veri'][veri])

def bakalim(ulke):
    veri = [sozluk['Veri'][veri] for veri in range(len(sozluk['Veri'])) if sozluk['Veri'][veri]['Country,Other'] == ulke]
    return print(veri[0])

#dene('Turkey')
#bakalim('Turkey')

"""
https://pythonprogramminglanguage.com/web-scraping-with-pandas-and-beautifulsoup/
https://sarahleejane.github.io/learning/python/2015/08/09/simple-tables-in-webapps-using-flask-and-pandas-with-python.html
https://cmdlinetips.com/2018/03/how-to-filter-a-pandas-dataframe-based-on-null-values-of-a-column/
https://github.com/danisaleem/Web-Scraping-BeautifulSoup-Python/blob/master/BeautifulSoup-Python.ipynb
"""