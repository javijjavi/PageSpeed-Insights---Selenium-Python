from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse
import datetime
from miapp.models import Post
import pymongo

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def current_database(request):
    contador = Post.objects.count()
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["prueba2"]
    mycol = mydb["miapp_post"]
    template = loader.get_template('miapp/index.html')
    
    for x in mycol.find():
        dominio = x['dominio']
        porcentaje_movil = x['porcentaje_movil']
        orportunidades_movil = x['orportunidades_movil']
        diagnosticos_movil = x['diagnosticos_movil']
        porcentaje_ordenador = x['porcentaje_ordenador']
        oportunidades_ordenador = x['oportunidades_ordenador']
        diagnosticos_ordenador = x['diagnosticos_ordenador']
        context = {
            'dominio': dominio,
            'porcentaje_movil': porcentaje_movil,
            'orportunidades_movil': orportunidades_movil,
            'diagnosticos_movil': diagnosticos_movil,
            'porcentaje_ordenador': porcentaje_ordenador,
            'oportunidades_ordenador': oportunidades_ordenador,
            'diagnosticos_ordenador': diagnosticos_ordenador,
        }
        return render(request, 'miapp/index.html', context)
        #return HttpResponse(html)
        #return HttpResponse(template.render(thisdict))
        #return HttpResponse(template.render(dominio))
        #return HttpResponse(template.render(dominio, porcentaje_movil, orportunidades_movil, diagnosticos_movil, porcentaje_ordenador, oportunidades_ordenador, diagnosticos_ordenador))