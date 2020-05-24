from Kolektif import app


if __name__ == '__main__':
    app.config['JSON_SORT_KEYS'] = False
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.config['JSON_AS_ASCII'] = False
    app.run(debug = True, host = '0.0.0.0', port = 5000)
