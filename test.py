import pymongo
import pprint

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["prueba2"]
mycol = mydb["miapp_post"]
#template = loader.get_template('miapp/index.html')
array = []
#contador = int(contador)
#array.append(contador)
#objetoMongo = mycol.find()
#pprint(objetoMongo)
for x in mycol:
    print(x)
