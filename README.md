# KolektifAPI
Python / Flask ile yazılmış REST API

#

> [/halGorsel?tur=sebze](https://kolektifapi.herokuapp.com/halGorsel?tur=sebze)

> [/hal?tur=meyve](https://kolektifapi.herokuapp.com/hal?tur=meyve)

> [/hal/ithal](https://kolektifapi.herokuapp.com/hal/ithal)

#

> [/udemyGorsel?kategori=python](https://kolektifapi.herokuapp.com/udemyGorsel?kategori=python)

> [/udemy?kategori=linux](https://kolektifapi.herokuapp.com/udemy?kategori=linux)

> [/udemy/bash](https://kolektifapi.herokuapp.com/udemy/bash)

#

> [/havaGorsel?sehir=canakkale](https://kolektifapi.herokuapp.com/havaGorsel?sehir=canakkale)

> [/hava?sehir=Beylikdüzü](https://kolektifapi.herokuapp.com/hava?sehir=Beylikdüzü)

> [/hava/pursaklar](https://kolektifapi.herokuapp.com/hava/pursaklar)

#

> [/eczaneGorsel?il=canakkale&ilce=merkez](https://kolektifapi.herokuapp.com/eczaneGorsel?il=canakkale&ilce=merkez)

> [/eczane?il=hatay&ilce=samandag](https://kolektifapi.herokuapp.com/eczane?il=hatay&ilce=samandag)

> [/eczane/mardin/nusaybin](https://kolektifapi.herokuapp.com/eczane/mardin/nusaybin)

#

> [/depremGorsel](https://kolektifapi.herokuapp.com/depremGorsel)

> [/deprem](https://kolektifapi.herokuapp.com/deprem)

#

> [/akaryakit](https://kolektifapi.herokuapp.com/akaryakit)

#

> [/haberGorsel](https://kolektifapi.herokuapp.com/haberGorsel)

#

## Proje Gelişimi

### [v1](https://github.com/KolektifAPI/gelisimAsamalari/tree/master/v1)
- *Spatula*(_Scrape_) dosyaları oluşturulup, `Flask` tek dosya olarak oluşturuldu.
- `gunicorn` ile *Heroku* _Deploy_ edildi.

### [v2](https://github.com/KolektifAPI/gelisimAsamalari/tree/master/v2)
- Kod okunurluğunu arttırmak ve projenin geliştirilebilmesi için `Flask` ın el verdiği dosya/dizin sistemi oluşturuldu.
- `jinja2` iyileştirmeleri yapıldı ve dosya/dizin sistemi oluşturuldu.
- `gunicorn` ile *Heroku* _Deploy_ edildi.

### [v3](https://github.com/KolektifAPI/gelisimAsamalari/tree/master/v3)
- `flask_sitemap` kütüphanesi kullanılarak otomatik bir sitemap oluşturuldu.
- `jsonify` ile dönen sayfalara _favicon_ eklendi.
- _gunicorn_'un `app.config` konfigürasyonlarını yoksayması sorunları yüzünden `waitress` _serve_ kullanıldı.
