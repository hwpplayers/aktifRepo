from Kolektif import app
from flask import render_template, request, jsonify
from Kolektif.hata import besYuz
from Kolektif.Spatula.depremVeri import anahtarlar, jsonVeri

kaynak = 'afet.gen.tr'

@app.route('/depremGorsel')
def depremGorsel():

    try: jsonVeri
    except: return besYuz('hata')

    return render_template(
        'veriSayfasi.html',
        veriler = jsonVeri,
        anahtarlar = anahtarlar,
        baslik = "Son Depremler Verisi"
    )

@app.route('/deprem')
def depremJsonArgs():
    try: jsonVeri
    except: return besYuz('hata')

    return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = jsonVeri)