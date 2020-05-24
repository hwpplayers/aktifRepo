from Kolektif import app
from flask import render_template, request, jsonify
from Kolektif.hata import besYuz
from Kolektif.Spatula.disc import udemySpatula

kaynak = 'discudemy.com'

@app.route('/udemyGorsel')
def udemyGorsel():
    kategori = request.args.get('kategori')
    if not kategori: return besYuz('hata')

    try: udemySpatula(kategori)
    except: return besYuz('hata')

    return render_template(
        'veriSayfasi.html',
        veriler = udemySpatula(kategori),
        baslik = "udemy Verileri"
    )

@app.route('/udemy')
def udemyJsonArgs():
    kategori = request.args.get('kategori')
    if not kategori: return besYuz('hata')

    try: udemySpatula(kategori)
    except: return besYuz('hata')

    return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = udemySpatula(kategori))

@app.route('/udemy/<kategori>')
def udemyJsonDizin(kategori):
    if not kategori: return besYuz('hata')

    try: udemySpatula(kategori)
    except: return besYuz('hata')

    return jsonify(kaynak = kaynak, saglayici = '@keyiflerolsun', veri = udemySpatula(kategori))