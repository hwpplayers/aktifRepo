from Kolektif import app
from flask import render_template, request, jsonify
from Kolektif.hata import besYuz
from Kolektif.Spatula.eczaneler import basliklar, nobetciEczane

kaynak = 'eczaneler.gen.tr'

@app.route('/eczaneGorsel')
def eczaneGorsel():
    il = request.args.get('il')
    ilce = request.args.get('ilce')
    if not il or not ilce: return besYuz('hata')

    try: nobetciEczane(il,ilce)
    except: return besYuz('hata')

    return render_template(
        'veriSayfasi.html',
        veriler = nobetciEczane(il, ilce),
        anahtarlar = basliklar(il, ilce),
        baslik = "Eczane Verileri"
    )

@app.route('/eczane')
def eczaneJsonArgs():
    il = request.args.get('il')
    ilce = request.args.get('ilce')
    if not il or not ilce: return besYuz('hata')

    try: nobetciEczane(il,ilce)
    except: return besYuz('hata')

    return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = nobetciEczane(il, ilce))

@app.route('/eczane/<il>/<ilce>')
def eczaneJsonDizin(il, ilce):
    if not il or not ilce: return besYuz('hata')

    try: nobetciEczane(il,ilce)
    except: return besYuz('hata')

    return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = nobetciEczane(il, ilce))