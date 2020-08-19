from Kolektif import app
from flask import render_template, request, jsonify
from Kolektif.hata import besYuz
from Kolektif.Spatula.koronaTum import anahtarlar, jsonVeri

kaynak = 'worldometers.info'

@app.route('/koronaGorsel')
def koronaGorsel():
    ulke = request.args.get('Neresi')
    if not ulke:
        return render_template(
            'veriSayfasi.html',
            veriler = jsonVeri,
            anahtarlar = anahtarlar,
            baslik = "Korona Genel Verileri"
        )

    veri = [jsonVeri[veri] for veri in range(len(jsonVeri)) if jsonVeri[veri]['Ülkeler'] == ulke]
    if veri == []: return besYuz('hata')

    return render_template(
        'veriSayfasi.html',
        veriler = veri,
        anahtarlar = anahtarlar,
        baslik = f"Korona {ulke} Verileri"
    )

@app.route('/korona')
def koronaJson():
    ulke = request.args.get('Neresi')
    if not ulke: return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = jsonVeri)

    veri = [jsonVeri[veri] for veri in range(len(jsonVeri)) if jsonVeri[veri]['Ülkeler'] == ulke]
    if veri == []: return besYuz('hata')

    return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = veri)

@app.route('/korona/<ulke>')
def koronaJsonUlke(ulke):
    veri = [jsonVeri[veri] for veri in range(len(jsonVeri)) if jsonVeri[veri]['Ülkeler'] == ulke]
    if veri == []: return besYuz('hata')

    return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = veri)