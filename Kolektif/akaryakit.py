from Kolektif import app
from flask import request, jsonify
from Kolektif.hata import besYuz
from Kolektif.Spatula.akaryakit import akaryakitFiyat

@app.route('/akaryakit')
def akaryakit():
    try: akaryakitFiyat()
    except: return besYuz('hata')

    return jsonify(akaryakitFiyat())