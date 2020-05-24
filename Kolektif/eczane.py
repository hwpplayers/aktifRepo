from Kolektif import app
from flask import render_template, request, jsonify
from Kolektif.hata import besYuz
from Kolektif.Spatula.eczaneler import anahtarlar, jsonVeri

kaynak = 'eczaneler.gen.tr'

@app.route('/eczaneGorsel')
def eczaneGorsel():
    il = request.args.get('il')
    ilce = request.args.get('ilce')
    if not il or not ilce: return besYuz('hata')

    try: jsonVeri(il,ilce)
    except: return besYuz('hata')

    return render_template(
        'veriSayfasi.html',
        veriler = jsonVeri(il, ilce),
        anahtarlar = anahtarlar(il, ilce),
        baslik = "Eczane Verileri"
    )

@app.route('/eczane')
def eczaneJsonArgs():
    il = request.args.get('il')
    ilce = request.args.get('ilce')
    if not il or not ilce: return besYuz('hata')

    try: jsonVeri(il,ilce)
    except: return besYuz('hata')

    return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = jsonVeri(il, ilce))

@app.route('/eczane/<il>/<ilce>')
def eczaneJsonDizin(il, ilce):
    if not il or not ilce: return besYuz('hata')

    try: jsonVeri(il,ilce)
    except: return besYuz('hata')

    return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = jsonVeri(il, ilce))