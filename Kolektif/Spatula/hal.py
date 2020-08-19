import requests
from bs4 import BeautifulSoup
import pytz, datetime
import pandas as pd
import json

def yerliMeyve():
    yil_ay = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%Y-%m")
    gun = int(datetime.datetime.now(pytz.timezone("Turkey")).strftime("%d")) - 1
    halZaman = f"{yil_ay}-{gun}"
    
    url = f"https://gida.ibb.istanbul/inc/halfiyatlari/gunluk_fiyatlar.asp?tarih={halZaman}&kategori=5&tUsr=M3yV353bZe&tPas=LA74sBcXERpdBaz&tVal=881f3dc3-7d08-40db-b45a-1275c0245685&HalTurId=2"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    istek = requests.get(url, kimlik)
    corba = BeautifulSoup(istek.content.decode('utf-8', 'ignore'), 'lxml')


    tablo = corba.find('table')
    pandaVeri = pd.read_html(str(tablo))[0]

    return pandaVeri

def yerliSebze():
    yil_ay = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%Y-%m")
    gun = int(datetime.datetime.now(pytz.timezone("Turkey")).strftime("%d")) - 1
    halZaman = f"{yil_ay}-{gun}"
    
    url = f"https://gida.ibb.istanbul/inc/halfiyatlari/gunluk_fiyatlar.asp?tarih={halZaman}&kategori=6&tUsr=M3yV353bZe&tPas=LA74sBcXERpdBaz&tVal=881f3dc3-7d08-40db-b45a-1275c0245685&HalTurId=2"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    istek = requests.get(url, kimlik)
    corba = BeautifulSoup(istek.content.decode('utf-8', 'ignore'), 'lxml')


    tablo = corba.find('table')
    pandaVeri = pd.read_html(str(tablo))[0]

    return pandaVeri

def ithal():
    yil_ay = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%Y-%m")
    gun = int(datetime.datetime.now(pytz.timezone("Turkey")).strftime("%d")) - 1
    halZaman = f"{yil_ay}-{gun}"
    
    url = f"https://gida.ibb.istanbul/inc/halfiyatlari/gunluk_fiyatlar.asp?tarih={halZaman}&kategori=7&tUsr=M3yV353bZe&tPas=LA74sBcXERpdBaz&tVal=881f3dc3-7d08-40db-b45a-1275c0245685&HalTurId=2"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    istek = requests.get(url, kimlik)
    corba = BeautifulSoup(istek.content.decode('utf-8', 'ignore'), 'lxml')


    tablo = corba.find('table')
    pandaVeri = pd.read_html(str(tablo))[0]

    return pandaVeri


# print(yerliMeyve())
# print(yerliSebze())
# print(ithal())


yerliMeyve_jsonVeri = json.loads(yerliMeyve().to_json(orient='records'))
yerliSebze_jsonVeri = json.loads(yerliSebze().to_json(orient='records'))
ithal_jsonVeri = json.loads(ithal().to_json(orient='records'))
# print(yerliMeyve_jsonVeri)
# print(yerliSebze_jsonVeri)
# print(ithal_jsonVeri)

yerlimeyve_jsonCikti = json.dumps(yerliMeyve_jsonVeri, indent=2, sort_keys=False, ensure_ascii=False)
yerliSebze_jsonCikti = json.dumps(yerliSebze_jsonVeri, indent=2, sort_keys=False, ensure_ascii=False)
ithal_jsonCikti = json.dumps(ithal_jsonVeri, indent=2, sort_keys=False, ensure_ascii=False)
# print(yerlimeyve_jsonCikti)
# print(yerliSebze_jsonCikti)
# print(ithal_jsonCikti)

yerliMeyve_anahtarlar = [anahtar for anahtar in yerliMeyve_jsonVeri[0].keys()]
yerliSebze_anahtarlar = [anahtar for anahtar in yerliSebze_jsonVeri[0].keys()]
ithal_anahtarlar = [anahtar for anahtar in ithal_jsonVeri[0].keys()]
# print(yerliMeyve_anahtarlar)
# print(yerliSebze_anahtarlar)
# print(ithal_anahtarlar)