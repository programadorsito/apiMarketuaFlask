from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from os import environ
from service import Car
from service import CarList
from service import Categories
from service import Products
from service import ProductsByCategory
from service import ProductsByBrand
from service import Brands
from service import Product
import sys

categories = {"status":"OK","data":[{"id":4,"category":"cellphone","created_at":"2019-09-12T03:50:18.799Z","updated_at":"2019-09-12T03:50:18.799Z"},{"id":5,"category":"computers","created_at":"2019-09-12T03:50:33.846Z","updated_at":"2019-09-12T03:50:33.846Z"},{"id":6,"category":"audio","created_at":"2019-09-12T03:50:43.038Z","updated_at":"2019-09-12T03:50:43.038Z"},{"id":7,"category":"cameras","created_at":"2019-09-12T03:50:53.422Z","updated_at":"2019-09-12T03:50:53.422Z"},{"id":8,"category":"tv","created_at":"2019-09-12T03:51:02.408Z","updated_at":"2019-09-12T03:51:02.408Z"}]}
items = {"status":"OK","data":[{"id":5,"name":"Portatil Lenovo Thinkpad","price":2500000.0,"brand":"Lenovo","thumbnail":"https://www.lenovo.com/medias/lenovo-laptop-thinkpad-x1-carbon-7th-gen-gallery-10.jpg?context=bWFzdGVyfHJvb3R8MTQxNDAyfGltYWdlL2pwZ3xoZDUvaDIwLzEwMDYxMzIxNDY5OTgyLmpwZ3xhYjJjMTU3YjkzNThhN2E2NTkyMjBlNTUzMDUwOGNlYzBmMmU5NDhkZWExOGNmYmViN2YwMmQzMTYwYWFiYjlh","rating":4.8,"description":"16 GB RAM","sold_units":15,"category_id":5,"seller_id":2,"created_at":"2019-09-12T04:25:38.117Z","updated_at":"2019-09-12T04:25:38.117Z"},{"id":6,"name":"ASUS Zenfone","price":450000.0,"brand":"ASUS","thumbnail":"https://media.aws.alkosto.com/media/catalog/product/cache/6/image/69ace863370f34bdf190e4e164b6e123/4/7/4718017172684_10.jpg","rating":4.0,"description":"De segunda, pero está como nuevo","sold_units":0,"category_id":4,"seller_id":3,"created_at":"2019-09-12T04:30:56.567Z","updated_at":"2019-09-12T04:30:56.567Z"},{"id":4,"name":"Portatil ASUS Intel Core i5","price":1500000.0,"brand":"ASUS","thumbnail":"https://p7.hiclipart.com/preview/599/481/84/asus-eee-pad-transformer-laptop-intel-core-i5-touchscreen-2-in-1-pc-asus-laptop-png-transparent.jpg","rating":4.5,"description":"Portátil bacano con 8 GB de RAM y 2 GB de Gráfica","sold_units":0,"category_id":5,"seller_id":1,"created_at":"2019-09-12T04:00:40.682Z","updated_at":"2019-09-12T04:00:40.682Z"},{"id":7,"name":"Samsung Galaxy A20","price":494900.0,"brand":"Samsung","thumbnail":"https://cdn.tmobile.com/content/dam/t-mobile/en-p/cell-phones/samsung/Samsung-Galaxy-A20/Black/Samsung-Galaxy-A20-Black-frontimage.jpg","rating":4.5,"description":"El Samsung Galaxy A20 tiene un tamaño de pantalla de 6,4\", con una resolución de 1.560 x 720. Procesador Exynos 7884 de 2 núcleos que alcanza una velocidad de reloj de 1,8 GHz. La cámara frontal que acompaña a la pantalla es de 8 Mpx con una apertura de f/2.0. Mientras, en la parte trasera la cámara princiapl es de 13 Mpx y apertura de f/1.9 con una segunda lente de 5 Mpx y f/2.2.","sold_units":5,"category_id":4,"seller_id":3,"created_at":"2019-09-12T20:03:30.062Z","updated_at":"2019-09-12T20:08:28.504Z"},{"id":8,"name":"Iphone X","price":3079900.0,"brand":"Apple","thumbnail":"https://images-na.ssl-images-amazon.com/images/I/61nlT53kRKL._SY445_.jpg","rating":4.7,"description":"Pantalla Super Retina HD de 5,8 pulgadas con HDR y True Tone. Cámara dual de 12 Mpx con modo Retrato, Iluminación de Retratos, HDR automático y vídeo 4K hasta 60 f/s. Cámara frontal TrueDepth de 7 Mpx con modo Retrato, Iluminación de Retratos y HDR automático. Diseño de vidrio y acero inoxidable resistente al agua y al polvo (calificación IP67).","sold_units":10,"category_id":4,"seller_id":4,"created_at":"2019-09-12T20:26:05.921Z","updated_at":"2019-09-12T20:26:05.921Z"},{"id":9,"name":"Celular Libre Huawei P20 Pro 128gb","price":2399900.0,"brand":"Huawei","thumbnail":"https://www.achocom.net/server/Portal_0015185/img/products/huawei-p20-pro-128gb-dual-sim-azul_5201952_xxl.jpg","rating":4.8,"description":"La serie P de HUAWEI siempre ha sido pionera de la fotografía en smartphones. Una vez más el HUAWEI P20 Pro lidera el camino con una revolucionaria Triple Cámara Leica, donde la visión estética se combina con un avanzado sistema de cámara que inaugura una nueva era de fotografía inteligente.   Pantalla: 6.1\" Cámara Trasera: 40 MP + 20MP + 8MP Cámara Frontal: 24 MP Sistema Operativo: Android Oreo 8.1 Memoria Interna: 128 GB  Batería: 4000 mAh Procesador: Octa Core (Quad 2,36 GHz + Quad 1,8 GHz) Posee:Camara con Inteligencia Artificial","sold_units":10,"category_id":4,"seller_id":4,"created_at":"2019-09-12T20:52:08.963Z","updated_at":"2019-09-12T20:52:08.963Z"},{"id":10,"name":"Celular Xiaomi Redmi Note 7 Global","price":699900.0,"brand":"Xiaomi","thumbnail":"https://http2.mlstatic.com/celular-xiaomi-redmi-note-7-64gb-48mp-forro-envio-gratis-D_NQ_NP_602546-MCO31080263585_062019-Q.jpg","rating":4.9,"description":"* SO // Android 9 // MIUI 10 * Procesador // Qualcomm SDM660 Snapdragon 660 Octa-core (4x2.2 GHz Kryo 260 \u0026 4x1.8 GHz Kryo 260) * GPU // Adreno 512 * Cámara Principal // Dual: 48 MP (f/1.8, 1/2\"\", 0.8µm, PDAF) + 5 MP ( f/2.4, depth sensor) * Cámara Frontal // 13 MP (f/2.2, 1.25µm)","sold_units":30,"category_id":4,"seller_id":4,"created_at":"2019-09-12T21:05:56.079Z","updated_at":"2019-09-12T21:05:56.079Z"},{"id":11,"name":"Portátil Toshiba Tecra A40-E","price":4499900.0,"brand":"Toshiba","thumbnail":"https://i.linio.com/p/4bc5953558906933f75378eefd7682ec-product.jpg","rating":4.0,"description":"Resolución de vídeo: 1,366 x 768 Disco duro (capacidad - tipo): 512 GB M.2 SSD Procesador: Intel Core i7-7500U Ram: 16GB DDR4-2133 MHz,  32GB max,  two 260-pin SO-DIMM sockets, Conectividad: Gigabit Intel® Ethernet Intel i219V Connection (10/100/1000Mbps) / Intel® Dual-Band Wireless-AC 8265 (2x2) plus Bluetooth Tamaño pantalla: 14.0 Color: Negro Video: Intel HD Graphics  620 in processor Marca: TOSHIBA Tipo de Ram: DDR4-2133 MHz, Generación del procesador: Septima Generación Tarjeta grafica: Intel HD Graphics  620 in processor Ranuras de memoria: 2 Slot Sistema operative: Windows 10 Pro 64-bit Puertos; Video (RGB, HDMI), 4 USB 3.0, RJ-45 LAN port, SD Card Reader, Spill-Resistant, Backlit, Spanish Keyboard, NO AccuPoint + SecurePad NO Fingerprint Reader","sold_units":2,"category_id":5,"seller_id":3,"created_at":"2019-09-12T21:13:27.570Z","updated_at":"2019-09-12T21:13:27.570Z"},{"id":12,"name":"Portatil Acer A315-41g-r0zz","price":1899999.0,"brand":"Acer","thumbnail":"https://http2.mlstatic.com/portatil-acer-a315-41g-r0zz-ryzen-5-1tb-8g-radeon-2gb-15-D_NQ_NP_754375-MCO31556374398_072019-F.jpg","rating":4.0,"description":"","sold_units":1,"category_id":5,"seller_id":3,"created_at":"2019-09-12T21:24:11.333Z","updated_at":"2019-09-12T21:24:11.333Z"},{"id":13,"name":"Portatil HP 15 Da0015la","price":2779900.0,"brand":"HP","thumbnail":"https://i.linio.com/p/f049628110c815f7626a4ab33d1bc6a9-product.jpg","rating":4.5,"description":"","sold_units":10,"category_id":5,"seller_id":3,"created_at":"2019-09-12T21:33:48.587Z","updated_at":"2019-09-12T21:33:48.587Z"},{"id":14,"name":"Celular Motorola Moto E5 Play","price":289900.0,"brand":"Motorola","thumbnail":"https://1519641355.rsc.cdn77.org/content/images/thumbs/0007311_celular-motorola-moto-e5-play-xt-1920_550.png","rating":4.3,"description":"","sold_units":5,"category_id":4,"seller_id":4,"created_at":"2019-09-12T21:58:07.542Z","updated_at":"2019-09-12T21:58:07.542Z"}]}
brands =  {"brands":[{"brand":"HP"},{"brand":"Huawei"},{"brand":"Lenovo"},{"brand":"Samsung"},{"brand":"Motorola"},{"brand":"Xiaomi"},{"brand":"Apple"},{"brand":"Toshiba"},{"brand":"ASUS"},{"brand":"Acer"}]}
app = Flask(__name__)

# cors = CORS(app,  origins=['http://localhost:8080'])
api = Api(app)

from flask import jsonify
from flask_restful import Resource,reqparse

parser = reqparse.RequestParser()

@api.resource('/categories')
class Categories(Resource):
    def get(self):
        return jsonify(categories)

@api.resource('/brands')
class Brands(Resource):
    def get(self):
        return jsonify(brands)

@api.resource('/items/category/<category_name>')
class ProductsByCategory(Resource):
    def get(self,  category_name:str):
        listaItems = []
        categoria = None
        for c in categories["data"]:
            if str(c["category"]).lower()==str(category_name).lower():
                categoria=c
                break
        
        if categoria:
            for item in items["data"]:
                if str(item["category_id"]).lower()==str(categoria["id"]).lower():
                    item["category"]=categoria
                    listaItems.append(item)
        return jsonify({"products":listaItems})
        
        # return jsonify({"products":listaItems})
    
@api.resource('/items/brand/<brand_name>')
class ProductsByBrand(Resource):
    def get(self, brand_name:str):
        listaItems = []
        for item in items["data"]:
            if str(item["brand"]).lower()==str(brand_name).lower():
                listaItems.append(item)
        return jsonify({"products":listaItems})
        # return jsonify({"products":[{"id":6,"name":"ASUS Zenfone","price":450000.0,"brand":"ASUS","thumbnail":"https://media.aws.alkosto.com/media/catalog/product/cache/6/image/69ace863370f34bdf190e4e164b6e123/4/7/4718017172684_10.jpg","rating":4.0,"description":"De segunda, pero está como nuevo","sold_units":0,"seller":{"seller_id":3,"seller_name":"Tobón","seller_rating":3.8,"seller_email":"juan.tobon6@marketua.co","created_at":"2019-09-12T04:30:42.151Z","updated_at":"2019-09-12T04:30:42.151Z"},"category":{"category_id":4,"category_name":"cellphone"}},{"id":4,"name":"Portatil ASUS Intel Core i5","price":1500000.0,"brand":"ASUS","thumbnail":"https://p7.hiclipart.com/preview/599/481/84/asus-eee-pad-transformer-laptop-intel-core-i5-touchscreen-2-in-1-pc-asus-laptop-png-transparent.jpg","rating":4.5,"description":"Portátil bacano con 8 GB de RAM y 2 GB de Gráfica","sold_units":0,"seller":{"seller_id":1,"seller_name":"ASUS","seller_rating":4.3,"seller_email":"asus@marketua.co","created_at":"2019-08-31T20:45:55.638Z","updated_at":"2019-08-31T20:45:55.638Z"},"category":{"category_id":5,"category_name":"computers"}}]})
        

@api.resource('/items/<item_id>')
class Product(Resource):
    def get(self, item_id):
        for item in items["data"]:
            if str(item["id"])==str(item_id):
                return jsonify(item)
        return jsonify({})

@api.resource('/search')
class Products(Resource):
    def get(self):
        return jsonify({"products":[{"id":5,"name":"Portatil Lenovo Thinkpad","price":2500000.0,"brand":"Lenovo","thumbnail":"https://www.lenovo.com/medias/lenovo-laptop-thinkpad-x1-carbon-7th-gen-gallery-10.jpg?context=bWFzdGVyfHJvb3R8MTQxNDAyfGltYWdlL2pwZ3xoZDUvaDIwLzEwMDYxMzIxNDY5OTgyLmpwZ3xhYjJjMTU3YjkzNThhN2E2NTkyMjBlNTUzMDUwOGNlYzBmMmU5NDhkZWExOGNmYmViN2YwMmQzMTYwYWFiYjlh","rating":4.8,"description":"16 GB RAM","sold_units":15,"seller":{"seller_id":2,"seller_name":"Lenovo","seller_rating":4.2,"seller_email":"lenovo@marketua.co"},"category":{"category_id":5,"category_name":"computers"}},{"id":4,"name":"Portatil ASUS Intel Core i5","price":1500000.0,"brand":"ASUS","thumbnail":"https://p7.hiclipart.com/preview/599/481/84/asus-eee-pad-transformer-laptop-intel-core-i5-touchscreen-2-in-1-pc-asus-laptop-png-transparent.jpg","rating":4.5,"description":"Portátil bacano con 8 GB de RAM y 2 GB de Gráfica","sold_units":0,"seller":{"seller_id":1,"seller_name":"ASUS","seller_rating":4.3,"seller_email":"asus@marketua.co"},"category":{"category_id":5,"category_name":"computers"}},{"id":12,"name":"Portatil Acer A315-41g-r0zz","price":1899999.0,"brand":"Acer","thumbnail":"https://http2.mlstatic.com/portatil-acer-a315-41g-r0zz-ryzen-5-1tb-8g-radeon-2gb-15-D_NQ_NP_754375-MCO31556374398_072019-F.jpg","rating":4.0,"description":"","sold_units":1,"seller":{"seller_id":3,"seller_name":"Tobón","seller_rating":3.8,"seller_email":"juan.tobon6@marketua.co"},"category":{"category_id":5,"category_name":"computers"}},{"id":13,"name":"Portatil HP 15 Da0015la","price":2779900.0,"brand":"HP","thumbnail":"https://i.linio.com/p/f049628110c815f7626a4ab33d1bc6a9-product.jpg","rating":4.5,"description":"","sold_units":10,"seller":{"seller_id":3,"seller_name":"Tobón","seller_rating":3.8,"seller_email":"juan.tobon6@marketua.co"},"category":{"category_id":5,"category_name":"computers"}}]})

@api.resource("/")
class AllProducts(Resource):
    def get(self):
        return jsonify(items)

class Car(Resource):

    def get(self, car_id: str):
        return jsonify({'success': True, 'data': {}})

    def post(self):
        data = parser.parse_args()
        return jsonify({'success': True, 'data': None})

    def put(self):
        data = parser.parse_args()
        return jsonify({'success': True, 'data': None})

    def delete(self, car_id):
        return jsonify({'success': True, 'data': None})



# api.add_resource(Car, '/car', '/car/<car_id>',methods=['GET', 'POST', 'PUT', 'DELETE'])
# api.add_resource(CarList, '/cars',methods=['GET'])
# api.add_resource(Categories, "/categories", methods=["GET"])
# api.add_resource(Brands, "/brands", methods=["GET"])
# api.add_resource(ProductsByCategory, "/items/category/<category_name>", methods=["GET"])
# api.add_resource(ProductsByCategory, "/items/category", methods=["GET"])
# api.add_resource(ProductsByBrand, "/items/brand/<brand_name>", methods=["GET"])
# api.add_resource(ProductsByBrand, "/items/brand", methods=["GET"])
# api.add_resource(Product, "/items/<item_id>", methods=["GET"])
# api.add_resource(Product, "/items", methods=["GET"])
# api.add_resource(Product, "/items", methods=["GET"])
# api.add_resource(Products, "/search", methods=["GET"])


app.run(host= '0.0.0.0', port=environ.get('PORT'))