from Kolektif import app
from flask import make_response, jsonify
import json

istekler = json.load(open("Kolektif/istekler.json", "r+", encoding='utf8'))

# @app.route('/favicon.ico', methods=['GET'])
# def favicon():
#     return send_from_directory(directory=app.root_path, filename='favicon.ico', mimetype='image/x-icon')

@app.errorhandler(404)
def dortYuzDort(error):
    return make_response(jsonify(KolektifAPI='Sayfa Bulunamadı', istekler=istekler), 404)

@app.errorhandler(500)
def besYuz(error):
    return make_response(jsonify(KolektifAPI='Düzgün Argüman Verilmedi', istekler=istekler), 500)