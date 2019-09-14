import pymongo
client = pymongo.MongoClient("mongodb+srv://flask:flask@cluster0-pkjgu.mongodb.net/test?retryWrites=true&w=majority")
db = client.test


class BrandController:
    def get_all():
        lista=[]
        for d in db.brands.find({}):
            del d["_id"]
            lista.append(d)
        return lista
    
    def save(item):
        db.brands.save(item)
        
class CategoryController:
    def get_all():
        lista=[]
        for d in db.categories.find({}):
            del d["_id"]
            lista.append(d)
        return lista
    
    def get_by_name(nombre):
        lista=CategoryController.get_all()
        for l in lista:
            if str(l["category"]).lower()==str(nombre).lower():
                return l
    
    def save(item):
        db.categories.save(item)

class ProductController:
    def get_all():
        lista=[]
        for d in db.items.find({}):
            del d["_id"]
            lista.append(d)
        return lista
    
    def get(item_id):
        lista=ProductController.get_all()
        for i in lista:
            if str(i["id"])==str(item_id):
                return i
    
    def get_by_category(category_name):
        categoria = CategoryController.get_by_name(category_name)
        items=ProductController.get_all()
        listaItems=[]
        if categoria:
            for item in items:
                if str(item["category_id"]).lower()==str(categoria["id"]).lower():
                    item["category"]=categoria
                    listaItems.append(item)
        return listaItems
        
        lista=ProductController.get_all()
        for i in lista:
            if str(i["id"])==str(item_id):
                return i
    
    def get_by_brand(brand_name):
        result=[]
        lista=ProductController.get_all()
        for i in lista:
            if str(i["brand"]).lower()==str(brand_name).lower():
                result.append(i)
        return result
        
    def get_by_name(name):
        result=[]
        lista=ProductController.get_all()
        for i in lista:
            if str(i["name"]).lower().find(str(name).lower())!=-1:
                result.append(i)
        return result
        
    def save(item):
        db.items.save(item)
