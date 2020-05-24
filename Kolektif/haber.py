from Kolektif import app
from flask import render_template
from Kolektif.Spatula.haberler import haberVerisi

@app.route('/haberGorsel')
def haberGorsel():
    return render_template(
        'haberSayfasi.html',
        veriler = haberVerisi,
        anahtarlar = ['Haber'],
        baslik = "Son Dakika Verileri"
    )