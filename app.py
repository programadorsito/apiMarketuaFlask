from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask import request
from os import environ
from controller import ProductController
from controller import BrandController
from controller import CategoryController
import sys


app = Flask(__name__)

# cors = CORS(app,  origins=['http://localhost:8080'])
cors = CORS(app)
api = Api(app)

from flask import jsonify
from flask_restful import Resource,reqparse

parser = reqparse.RequestParser()

@api.resource('/categories')
class Categories(Resource):
    def get(self):
        return jsonify({"status":"OK", "data":CategoryController.get_all()})

@api.resource('/brands')
class Brands(Resource):
    def get(self):
        return jsonify({"brands":BrandController.get_all()})
    

@api.resource('/items/category/<category_name>')
class ProductsByCategory(Resource):
    def get(self,  category_name:str):
        return jsonify({"products":ProductController.get_by_category(category_name)})
        
        # return jsonify({"products":listaItems})
    
@api.resource('/items/brand/<brand_name>')
class ProductsByBrand(Resource):
    def get(self, brand_name:str):
        items=ProductController.get_by_brand(brand_name)
        return jsonify({"products":items})
        

@api.resource('/items/<item_id>')
class Product(Resource):
    def get(self, item_id):
        item = ProductController.get(str(item_id))
        return jsonify(item)

@api.resource('/search')
class Products(Resource):
    def get(self):
        nombre = request.args.get('q')
        return jsonify({"products":ProductController.get_by_name(nombre)})

@api.resource("/")
class AllProducts(Resource):
    def get(self):
        return jsonify(items)


app.run(host= '0.0.0.0', port=environ.get('PORT'))