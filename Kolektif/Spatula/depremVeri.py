import requests
from bs4 import BeautifulSoup

class Spatula:
    def __init__(self, link):
        super().__init__()
        self.link = link
        self.istek = requests.get(self.link)
    
    def veri(self):
        if not self.istek.ok: return f'Server Yanıtı {self.istek.status_code}'
        
        self.corba = BeautifulSoup(self.istek.content, 'lxml')
        
        return self.corba

sonDepremler = lambda : Spatula('http://www.afet.gen.tr/son-depremler.php').veri()

import pandas as pd
tablo = sonDepremler().find('table', width="100%")
pandaVeri = pd.read_html(str(tablo))[0].rename(
    columns={
        0   : 'Tarih',
        1   : 'Saat',
        2   : 'Enlem(N)',
        3   : 'Boylam(E)',
        4   : 'Derinlik(km)',
        5   : 'MD',
        6   : 'ML',
        7   : 'MS',
        8   : 'Yer'
    }
)

pandaVeri = pd.DataFrame(pandaVeri).drop([0], axis=0)
# print(pandaVeri)


from tabulate import tabulate
gorselVeri = tabulate(pandaVeri, headers='keys', tablefmt='psql')
# print(gorselVeri)


import json
jsonVeri = json.loads(pandaVeri.to_json(orient='records'))
# print(jsonVeri)

jsonCikti = json.dumps(jsonVeri, indent=2, sort_keys=False, ensure_ascii=False)
# print(jsonCikti)

anahtarlar = [anahtar for anahtar in jsonVeri[0].keys()]
# print(anahtarlar)