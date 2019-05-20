#!/usr / bin / env python 

# Comprobamos librerias de selenium

try:
    from selenium import webdriver 
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import time 
    import selenium as se
    from selenium.webdriver.firefox.options import Options
except:
    print("Falta la libreria selenium en su python, pip install selenium")
    time.sleep(10)
    exit()

# Comprobamos librerias de mongodb

try:
    import pymongo
except:
    print("Falta la libreria de mongodb en su python, pip install pymongo")

#profile.set_preference("general.useragent.override", "[user-agent string]")
#profile.set_preference("general.useragent.override", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0")

# Conexion con la base de datos Mongo DB y comprobar si esta la base de datos si no instalarla.
# Eligiremos nuestra base de datos la columna y si esta se encuentra, eliminarla.

try:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["db_pagespeed"]
    mycol = mydb["dates"]
    mycol.drop()
except:
    print("No se ha podido conectar con la base de datos, revisa MongoDB shell.")

# Combrobamos librearia de psutil con el cual podremos observar cuanta memoria esta consumiendo nuestro proceso, por si tenemos que llegar a finalizarlo antes de que bloquee nuestro ordenador.

try:
    import psutil
except:
    print("Necesita descargar la libreria psutil")

# Descargar los dominios de nuestro archivo dominios.txt donde debes introducir los dominios y los pasará a un array para su procesamiento.

try:
    with open('dominios.txt', 'r') as dominio:
        dominios = dominio.readlines()
    with open('dominios.txt', 'r') as dominio:
        dominios = [line.strip() for line in dominio]
except:
    print("No se ha encontrado el archivo dominios.txt, o se ha localizado algun fallo relacionado con el, porfavor revisalo.")

# Ya tendriamos que tener todos lo necesario si hemos llegado hasta aqui. HF!
# Aquí empezaremos nuestro programa en la pagina inicial de PageSpeed Insights
# Función con la cual analizamos la url e introducimos los diferentes url para analizarlos y sacar la información.

_id = 0

def funcion_analizarURL(dominios, _id):
    for dominio in dominios:
        options = Options()
        options.headless = True
        brower = webdriver.Firefox(options=options, executable_path=r"C:\PROYECTOS\WebDriver\Firefox\geckodriver.exe")
        website_URL ="https://developers.google.com/speed/pagespeed/insights/?hl=es"
        brower.get(website_URL)
        elem = brower.find_element_by_css_selector("input.url.label-input-label")
        elem.send_keys(dominio)
        elem.send_keys(Keys.RETURN)
        web = brower.current_url
        _id = _id + 1
        funcion_sacarINF(web, brower, _id, dominio)
        del elem
        del web

# Función con la cual sacamos la iformación de las diferentes paginas tanto de la app para movil como para la de ordenador.

def funcion_sacarINF(web, brower, _id, dominio):
    brower.get(web)

    puntuaciones = brower.find_elements_by_class_name("lh-gauge__percentage")
    puntuaciones_porcentaje_movil = []
    for puntuacion in puntuaciones:
        text = puntuacion.text
        puntuaciones_porcentaje_movil.append(text)

    frases_encontradas = brower.find_elements_by_xpath("//div[@class='lh-audit-group lh-audit-group--load-opportunities']//div[@class='lh-audit__title']//span")
    orportunidades_movil = []
    for frase in frases_encontradas:
        text = frase.text
        if len(text) > 2:
            orportunidades_movil.append(text)
        else:
            continue

    frases_encontradas = brower.find_elements_by_xpath("//div[@class='lh-audit-group lh-audit-group--diagnostics']//span[@class='lh-audit__title']//span")
    diagnosticos_movil = []
    for frase in frases_encontradas:
        text = frase.text
        if len(text) > 2:
            diagnosticos_movil.append(text)
        else:
            continue
    
    cambiar = brower.find_element_by_id(":8")
    cambiar.click()
    time.sleep(2)

    frases_encontradas = brower.find_elements_by_xpath("//div[@class='lh-audit-group lh-audit-group--load-opportunities']//div[@class='lh-audit__title']//span")
    oportunidades_ordenador = []
    for frase in frases_encontradas:
        text = frase.text
        if len(text) > 2:
            oportunidades_ordenador.append(text)
        else:
            continue

    frases_encontradas = brower.find_elements_by_xpath("//div[@class='lh-audit-group lh-audit-group--diagnostics']//span[@class='lh-audit__title']//span")
    diagnosticos_ordenador = []
    for frase in frases_encontradas:
        text = frase.text
        if len(text) > 2:
            diagnosticos_ordenador.append(text)
        else:
            continue
    
    puntuaciones = brower.find_elements_by_class_name("lh-gauge__percentage")
    puntuaciones_porcentaje_ordenador = []
    for puntuacion in puntuaciones:
        text = puntuacion.text
        puntuaciones_porcentaje_ordenador.append(text)

    porcentaje_movil = puntuaciones_porcentaje_movil[0]
    porcentaje_ordenador = puntuaciones_porcentaje_ordenador[1]

    time.sleep(2)
    brower.close()
    print(porcentaje_movil)
    print(orportunidades_movil)
    print(diagnosticos_movil)
    print(porcentaje_ordenador)
    print(oportunidades_ordenador)
    print(diagnosticos_ordenador)

    funcion_MongoDB(_id, dominio, porcentaje_movil, orportunidades_movil, diagnosticos_movil, porcentaje_ordenador, oportunidades_ordenador, diagnosticos_ordenador)
    funcion_memoryMagnement(brower)

# En la funcion "funcion_MongoDB" recogeremos los datos anteriormente extraido y lo insertaremos en nuestra base de datos MongoDB.

def funcion_MongoDB(_id, dominio, porcentaje_movil, orportunidades_movil, diagnosticos_movil, porcentaje_ordenador, oportunidades_ordenador, diagnosticos_ordenador):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["db_pagespeed"]
    mycol = mydb["dates"]   
    mydates = {
    "_id": _id,
    "dominio": dominio,
    "porcentaje_movil": porcentaje_movil, 
    "orportunidades_movil": orportunidades_movil,
    "diagnosticos_movil": diagnosticos_movil,
    "porcentaje_ordenador": porcentaje_ordenador,
    "oportunidades_ordenador": oportunidades_ordenador,
    "diagnosticos_ordenador": diagnosticos_ordenador   
    }

    insertar = mycol.insert_one(mydates)

    print(insertar)

# En esta funcion avmos a comrpobar cuanta memoria esta consumiendo  nuestro proceso y asi poder controlarla.

def funcion_memoryMagnement(brower):
    memoria = psutil.virtual_memory()
    controlador = 100 * 1024 * 100
    if memoria.available <= controlador:
        brower.close
        exit()
    

funcion_analizarURL(dominios, _id)