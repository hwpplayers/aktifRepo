import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

def nobetciSpatula(il, ilce):
    url = f"https://www.eczaneler.gen.tr/nobetci-{il}-{ilce}"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    istek = requests.get(url, kimlik)
    soup = BeautifulSoup(istek.text, "lxml")

    sozluk = {"nobetciEczaneler": []}

    for table in soup.findAll("table", {"class": "table table-striped mt-2"}):
        #print(table)
        #print(table.tr.text)
        eczane_adi = table.findAll("td", {"style": "width:20%"})
        eczane_adresi = table.findAll("td", {"style": "width:50%"})
        eczane_telefon = table.findAll("td", {"style": "width:30%"})

        for adet in range(len(eczane_adi)):
            sozluk["nobetciEczaneler"].append({"Eczane Adı": eczane_adi[adet].text})
            sozluk["nobetciEczaneler"][adet]["Eczane Adresi"] = eczane_adresi[adet].text
            sozluk["nobetciEczaneler"][adet]["Eczane Telefonu"] = eczane_telefon[adet].text

    return sozluk

dataFrame = lambda il, ilce: pd.DataFrame(data=nobetciSpatula(il, ilce)['nobetciEczaneler'])
#print(dataFrame('canakkale','merkez'))

import json
eczaneJson = lambda il, ilce: json.loads(dataFrame(il, ilce).to_json(orient='records'))
#print(eczaneJson('canakkale','merkez'))

from tabulate import tabulate
gorselVeri = lambda il, ilce: tabulate(dataFrame(il, ilce), headers='keys', tablefmt='psql')
#print(gorselVeri('canakkale', 'merkez'))