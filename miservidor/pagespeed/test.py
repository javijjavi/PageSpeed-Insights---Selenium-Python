import pymongo
from pprint import pprint

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["prueba2"]
mycol = mydb["miapp_post"]
#template = loader.get_template('miapp/index.html')
array = []
#contador = int(contador)
#array.append(contador)
objetMongo = mycol.find({})
#pprint(objetoMongo)
context = []
for x in objetMongo:
    #objetoMongo = pprint(x) 
    context.append(x)

print(context)

#pprint.pformat(objetoMongo)
