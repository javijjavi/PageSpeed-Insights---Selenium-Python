import pymongo
import pprint
import json
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["prueba2"]
mycol = mydb["miapp_post"]
cursor = mycol.find()
for x in cursor:
    print(x['_id'], x['id'], x['porcentaje_movil'], x['porcentaje_ordenador'], x['dominio'])
    dominio = x['dominio']
    print(dominio)