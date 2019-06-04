from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse
import datetime
from miapp.models import Post
import pymongo
from pprint import pprint
import django_tables2 as table
from miapp.tables import DateTable
from django_tables2 import RequestConfig


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

#def current_database(request):
#    contador = Post.objects.count()

#    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#    mydb = myclient["prueba2"]
#    mycol = mydb["miapp_post"]

#    template = loader.get_template('miapp/index.html')

#    objetoMongo = mycol.find({})

#    context = []

#    for x in objetoMongo:
#        context.append(x)
    
#    table = 
    
#    return render(request, 'miapp/index.html', {'context': context})
    
def tabla_mongo(request):
    myclient = pymongo.MongoClient("mongodb://10.0.75.1:55059")
    mydb = myclient["prueba2"]
    mycol = mydb["miapp_post"]
    dis_data = mycol.find()
    table = DateTable(list(dis_data))
    RequestConfig(request).configure(table)
    return render(request, 'miapp/index.html', {'table': table})
    
    
    
    
    
    
    
    
    
    #for x in objetoMongo:
        #dominio = x['dominio']
        #porcentaje_movil = x['porcentaje_movil']
       # orportunidades_movil = x['orportunidades_movil']
       # diagnosticos_movil = x['diagnosticos_movil']
      #  porcentaje_ordenador = x['porcentaje_ordenador']
      #  oportunidades_ordenador = x['oportunidades_ordenador']
      #  diagnosticos_ordenador = x['diagnosticos_ordenador']
        
     #   array.append(dominio)
     #   array.append(porcentaje_movil)
     #   array.append(orportunidades_movil)
      #  array.append(diagnosticos_movil)
     #   array.append(porcentaje_ordenador)
     #   array.append(oportunidades_ordenador)
     #   array.append(diagnosticos_ordenador)

    #return render(request, 'miapp/index.html', {'array': objetoMongo})
    #eturn render(request, 'miapp/index.html', {'array': array})
        #return HttpResponse(html)
        #return HttpResponse(template.render(thisdict))
        #return HttpResponse(template.render(dominio))
        #return HttpResponse(template.render(dominio, porcentaje_movil, orportunidades_movil, diagnosticos_movil, porcentaje_ordenador, oportunidades_ordenador, diagnosticos_ordenador))
        #dicionario = {
        #'dominio': dominio,
        #'porcentaje_movil': porcentaje_movil,
        #'orportunidades_movil': orportunidades_movil,
        #'diagnosticos_movil': diagnosticos_movil,
        #'porcentaje_ordenador': porcentaje_ordenador,
        #'oportunidades_ordenador': oportunidades_ordenador,
        #'diagnosticos_ordenador': diagnosticos_ordenador,
        #}