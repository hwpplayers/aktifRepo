from flask import Flask
from flask_sitemap import Sitemap

app = Flask(__name__)
ext = Sitemap(app=app)

from Kolektif import anaSayfa, hata, eczane, haber, udemy, deprem, akaryakit