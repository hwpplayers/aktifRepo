from Kolektif import app
from flask import render_template, request, jsonify
from Kolektif.hata import besYuz
from Kolektif.Spatula.hava import anahtarlar, havaDurumu

kaynak = 'google.com.tr'

@app.route('/havaGorsel')
def havaGorsel():
    sehir = request.args.get('sehir')
    if not sehir: return besYuz('hata')

    try: havaDurumu(sehir)
    except: return besYuz('hata')

    return render_template(
        'veriSayfasi.html',
        veriler = havaDurumu(sehir),
        anahtarlar = anahtarlar(sehir),
        baslik = "Hava Durumu Verisi"
    )

@app.route('/hava')
def havaJsonArgs():
    sehir = request.args.get('sehir')
    if not sehir: return besYuz('hata')

    try: havaDurumu(sehir)
    except: return besYuz('hata')

    return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = havaDurumu(sehir))

@app.route('/hava/<sehir>')
def havaJsonDizin(sehir):
    if not sehir: return besYuz('hata')

    try: havaDurumu(sehir)
    except: return besYuz('hata')

    return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = havaDurumu(sehir))