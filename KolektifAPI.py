from flask import Flask, render_template, request, jsonify, send_from_directory, make_response

import pandas as pd
from Spatula.koronaTum import pandaVeri, sozluk
from Spatula.eczane import dataFrame, eczaneJson
from Spatula.haber import hSozluk
#from json2html import json2html

app = Flask(__name__)

hata = {
    'HATALI İSTEK!' : 'Aradığınız içerik mevcut değil. Lütfen isteğinizi kontrol edin.',
    'İstek Çeşitleri' : {
        'korona': [
            '/koronaGorsel',
            '/koronaGorsel?Neresi=Turkey',
            '/korona',
            '/korona?Neresi=Turkey',
            '/korona/Turkey'
        ],
        'eczane': [
            '/eczaneGorsel?il=canakkale&ilce=merkez',
            '/eczane?il=hatay&ilce=samandag',
            '/eczane/mardin/nusaybin'
        ],
        'haber':[
            '/haberGorsel'
        ]
    }
}

@app.route('/koronaGorsel', methods=['GET'])
def koronaGorsel():
    ulke = request.args.get('Neresi')

    if not ulke:
        return render_template(
            'VeriSayfasi.html',
            tablolar = [pandaVeri.to_html(classes='KolektifAPI')],
            basliklar = ['na', 'Korona Verisi']
            )

    veri = [sozluk['Veri'][veri] for veri in range(len(sozluk['Veri'])) if sozluk['Veri'][veri]['Ülkeler'] == ulke]
    if veri == []: return besYuz(hata)
    return render_template(
        'VeriSayfasi.html',
        tablolar = [pd.DataFrame(veri).to_html(classes='KolektifAPI')],
        basliklar = ['na', 'Korona Verisi']
    )

@app.route('/korona', methods=['GET'])
def koronaJson():
    ulke = request.args.get('Neresi')

    if not ulke: return jsonify(sozluk)

    veri = [sozluk['Veri'][veri] for veri in range(len(sozluk['Veri'])) if sozluk['Veri'][veri]['Ülkeler'] == ulke]
    if veri == []: return besYuz(hata)
    return jsonify(veri[0])

@app.route('/korona/<ulke>', methods=['GET'])
def koronaJsonUlke(ulke):
    veri = [sozluk['Veri'][veri] for veri in range(len(sozluk['Veri'])) if sozluk['Veri'][veri]['Ülkeler'] == ulke]
    if veri == []: return besYuz(hata)
    return jsonify(veri[0])

@app.route('/eczaneGorsel', methods=['GET'])
def eczaneGorsel():
    il = request.args.get('il')
    ilce = request.args.get('ilce')

    return render_template(
        'VeriSayfasi.html',
        tablolar = [dataFrame(il, ilce).to_html(classes='KolektifAPI')],
        basliklar = ['na', 'Eczane Verisi']
        )

@app.route('/eczane', methods=['GET'])
def eczaneJsonArgs():
    il = request.args.get('il')
    ilce = request.args.get('ilce')

    if not il or not ilce: return besYuz(hata)

    sozluk = {
        "Veri Kaynağı": "https://eczaneler.gen.tr/",
        "Veri Sağlayıcısı": "@keyiflerolsun",
        "Veri": eczaneJson(il, ilce)
    }

    if sozluk['Veri'] == []: return besYuz(hata)

    return jsonify(sozluk)

@app.route('/eczane/<il>/<ilce>', methods=['GET'])
def eczaneJsonDizin(il, ilce):
    if not il or not ilce: return besYuz(hata)

    sozluk = {
        "Veri Kaynağı": "https://eczaneler.gen.tr/",
        "Veri Sağlayıcısı": "@keyiflerolsun",
        "Veri": eczaneJson(il, ilce)
    }

    if sozluk['Veri'] == []: return besYuz(hata)

    return jsonify(sozluk)

@app.route('/haberGorsel', methods=['GET'])
def haberGorsel():
    return render_template(
        'VeriSayfasi.html',
        tablolar = [pd.DataFrame(hSozluk['manset']).to_html(classes='KolektifAPI')],
        basliklar = ['na', 'Son Dakika Verisi']
        )

"""@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return send_from_directory(directory=app.root_path, filename='favicon.ico', mimetype='image/x-icon')"""

@app.errorhandler(404)
def dortYuzDort(error):
    return make_response(jsonify(hata), 404)

@app.errorhandler(500)
def besYuz(error):
    return make_response(jsonify(KolektifAPI="jajajaja", hata=hata), 500)

if __name__ == '__main__':
    app.config['JSON_SORT_KEYS'] = False
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True, host='0.0.0.0', port=5000)
