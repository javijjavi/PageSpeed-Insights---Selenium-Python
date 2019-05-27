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

# Conexion con la base de datos Mongo DB y comprobar si esta la base de datos si no instalarla.
# Eligiremos nuestra base de datos la columna y si esta se encuentra, eliminarla.

try:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")        # Conectamos con nuestro cliente MongoDB
    mydb = myclient["db_pagespeed"]     # Seleccionamos nuestra base de datos
    mycol = mydb["dates"]       # Seleccionamos nuestra columna dentro de nuestra base de datos
    mycol.drop()        # Si encontramos la columna la borramos
except:
    print("No se ha podido conectar con la base de datos, revisa MongoDB shell.")

# Combrobamos librearia de psutil con el cual podremos observar cuanta memoria esta consumiendo nuestro proceso, por si tenemos que llegar a finalizarlo antes de que bloquee nuestro ordenador.

try:
    import psutil
except:
    print("Necesita descargar la libreria psutil")

# Descargar los dominios de nuestro archivo dominios.txt donde debes introducir los dominios y los pasará a un array para su procesamiento.

try:
    with open('dominios.txt', 'r') as dominio:      # Abrimos nuestro nuestro archivo txt en forma de leer.
        dominios = dominio.readlines()      # Leemos las diferentes lineas del archivo txt.
    with open('dominios.txt', 'r') as dominio:      # Volvemos a abrir nuestro documento txt en formato lectura.
        dominios = [line.strip() for line in dominio]       # Pasamos cada una de las lineas a un array, cada linea estará en un lugar del array.
    # Ejemplo:
    # Si en el dominios.txt tenemos lo siguiente:
    # https://github.com/
    # https://www.quackit.com/
    # https://www.udemy.com/

    # Este codigo nos pasara estos dominios a un array de la siguiente forma:
    # dominios = [https://github.com/, https://www.quackit.com/, https://www.udemy.com/]
except:
    print("No se ha encontrado el archivo dominios.txt, o se ha localizado algun fallo relacionado con el, porfavor revisalo.")

# Ya tendriamos que tener todos lo necesario si hemos llegado hasta aqui. HF!
# Aquí empezaremos nuestro programa en la pagina inicial de PageSpeed Insights
# Función con la cual analizamos la url e introducimos los diferentes url para analizarlos y sacar la información.

_id = 0

def funcion_analizarURL(dominios, _id):
    for dominio in dominios:        # Creamos un bucle para ir analizando dominio tras dominio de nuestro array anteriormente creado dominios.
        options = Options()     # Creamos la variable options, para poder modificar el webdriver.
        options.headless = True     # Le decimos al web driver que active la opcion headless, con esta opcion el navegador (webdriver) no se nos abrirá tras ejecutar el programa, reduciendo asi el consumo de memoria.
        brower = webdriver.Firefox(options=options, executable_path=r"C:\PROYECTOS\WebDriver\Firefox\geckodriver.exe")      # Le indicamos donde esta localizado el web driver en nuestro ordenador, en mi caso utilizo un Mozilla Firefox, pero podria haber utilizado otro cualquiera.
        website_URL ="https://developers.google.com/speed/pagespeed/insights/?hl=es"        # Le indico cual es la URL de la website que posteriormente introducire en el navegador.
        brower.get(website_URL)     # Aqui abro el navegador (con la opcion anterior headless activada se nos abrirá como un proceso en background) y le introduce la URL que anteriormente hemos definido.
        elem = brower.find_element_by_css_selector("input.url.label-input-label")       # Defino la variable elem la cual es la busqueda dentro de la URL introducida del selector que utiliza el css input.url.label-input-label
        # En este caso elem siempre seria el input de la URL 
        elem.send_keys(dominio)     # Le mandamos a la variable elem uno de nuestros dominios pasados a array anteriormente
        elem.send_keys(Keys.RETURN)     # Una vez introducido el domino con este codigo seria como pulsar "enter" en la pagina para empezar a analizar el dominio
        # En otras palabras con este codigo analizado hasta ahora lo que hariamos seria abrir un webDriver en este caso Firefox, escribir la URL marcada, ir a LA URL marcada y una vez dentro de la URL (pagespeed) buscar el elemento donde podemos escribir el domino, seleccionarlo escribir el dominio y pulsar "enter" para empezar a analizarlo.
        web = brower.current_url        # Una vez analizado creamos la variable web y le decimos que sea la URL actual
        _id = _id + 1       # Creamos la variable _id que la utilizaremos posterimormente para nuestra funcion MongoDB
        funcion_sacarINF(web, brower, _id, dominio)     # Llamamos a la funcion sacar informacion y les pasamos las variables web, brower, _id y dominio
        # Llamamos aqui a la funcion para que nos vaya extrayendo la informacion dominio a dominio de nuestro array, asi hasta que no haya terminado de procesar un domino no pasara al siguiente de nuestro array
        del elem        # Debido a la velocidad que va nuestro programa es combeniente eleminar las variables definidas anteriormente porque si no lo hacemos a veces pilla los datos de las variables antiguas y no de las nuevas
        del web

# Función con la cual sacamos la iformación de las diferentes paginas tanto de la app para movil como para la de ordenador.

def funcion_sacarINF(web, brower, _id, dominio):
    brower.get(web)         # Le indicamos al navegador en que URL se debe encontrar para evitar errores
    puntuaciones = brower.find_elements_by_class_name("lh-gauge__percentage")       # Aqui definimos la variable puntuaciones esta nos buscara los elemntos de tengan el class name lh-gauge__percentage en este caso seria el porcentaje de la pagina en el movil 
    # Este elemento es un poco peculiar ya que hay dos con el mismo class name el porcentaje del movil y del ordenador lo que pasa que si nos encontramos en la pagina del movil js esconde el porcentaje del ordenador, pero aun asi el programa llega a detectarlo asi que lo mejor es buscar ya directamente los dos porcentajes
    puntuaciones_porcentaje_movil = []      # Creamos un array llamado puntuaciones_porcentaje_movil
    for puntuacion in puntuaciones:     # Creamos bucle para los elementos extraidos anteriormente que seran 2 poder analizarlo uno a uno
        text = puntuacion.text      # Creamos la variable text y le decimos que uno de los elemntos extraidos nos lo pase a formato texto
        puntuaciones_porcentaje_movil.append(text)      # Introducimos en la array anteriormente creada el porcentaje en formato texto
# Aqui seguimos en la URL del movil
    frases_encontradas = brower.find_elements_by_xpath("//div[@class='lh-audit-group lh-audit-group--load-opportunities']//div[@class='lh-audit__title']//span")        # Esta vez buscamos los elementos pero utilizando el path utilizamos este sistema porque este texto es generado por js y no dispone de class name se encuentran en etiquetas span
    orportunidades_movil = []       # Creamos array
    for frase in frases_encontradas:        # Analizamos cada elemento encontrado independientemente de la variable frases_encontradas
        text = frase.text       # Pasmos el elemento a formato texto
        if len(text) > 2:       # Creamos una condicion con la cual le decimos que si la longitud del elememto es mayor que 2,
            orportunidades_movil.append(text)       # nos los menta en el array
        else:       # Si la longitud no es mayor que 2,
            continue        # pasamos a otro elemento o continuamos con el programa
        # Esta condicion la creo porque el programa siemrpe encuentra 10 elementos pero 5 elementos estan vacios porque esta extrayendo la informacion del ordenador, pero como he dicho anteriormente esta informacion esta en oculto hasta que no hagamos click en el.
# Aqui realizamos basicamente lo mismo lo unico que cambia es el path ya que aqui recogemos otros elementos.
    frases_encontradas = brower.find_elements_by_xpath("//div[@class='lh-audit-group lh-audit-group--diagnostics']//span[@class='lh-audit__title']//span")
    diagnosticos_movil = []
    for frase in frases_encontradas:
        text = frase.text
        if len(text) > 2:
            diagnosticos_movil.append(text)
        else:
            continue
    
    # Una vez recogida toda la informacion va a ejecutar el siguiente codigo
    cambiar = brower.find_element_by_id(":8")       # Buscamos el elemento con el id :8 que en este caso es un boton de la pagina donde nos encontramos
    # En concreto es el boton que nos permite cambiar de movil a ordenador
    cambiar.click()     # Le decimos que haga click en el 
    time.sleep(2)       # Esperamos 2 segundos para asegurarnos que se han cargado todos los elementos correctamente

# Ahora ya la informacion del ordenador no se encuentra en oculto asi que ya la podremos extraer, aqui hacemos mas o menos lo mismo que antes pero extrayendo los datos del ordenador
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

    porcentaje_movil = puntuaciones_porcentaje_movil[0]     # Indicamos en que lugar del array esta el porcentaje del movil
    porcentaje_ordenador = puntuaciones_porcentaje_ordenador[1]     # Indicamos en que lugar del array esta el porcentaje del ordenador

    time.sleep(2)       # Esperamos dos segundos para termiar de recoger toda la informacion
    brower.close()      # IMPORTANTE!
                        # Cerramos el navegador, porque si no por cada dominio analizado nos abriria un navegador y imaginamos que analizamos 200 dominios, nuestro ordenador petaria porque serian mas de 200 nevegadores abiertos
                        # De esta manera por dominio analizado navegador cerrado entonces solo tendriamos un navegador como maximo abierto
    print(porcentaje_movil)
    print(orportunidades_movil)
    print(diagnosticos_movil)
    print(porcentaje_ordenador)
    print(oportunidades_ordenador)
    print(diagnosticos_ordenador)
        # LLamanos a la funcion MongoDB y le pasamos las variables que hemos extraido
    funcion_MongoDB(_id, dominio, porcentaje_movil, orportunidades_movil, diagnosticos_movil, porcentaje_ordenador, oportunidades_ordenador, diagnosticos_ordenador)
        # Llammos a la funcion memorimagnement esto nos servirá para analizar cuanta memoria estamos consumiendo y si estamos consumiendo mas de la cuenta nos cierra el programa
        # Esto es un control de seguridad pero nunca tendria que activarse a no ser que tengamos 2000 programas abierto y el ordenador este muy al limite por los otros programas
    funcion_memoryMagnement(brower)

# En la funcion "funcion_MongoDB" recogeremos los datos anteriormente extraido y lo insertaremos en nuestra base de datos MongoDB.

def funcion_MongoDB(_id, dominio, porcentaje_movil, orportunidades_movil, diagnosticos_movil, porcentaje_ordenador, oportunidades_ordenador, diagnosticos_ordenador):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")        # Conectamos con nuestra base de datos MongoDB
    mydb = myclient["db_pagespeed"]     # Seleccionamos nuestra base de datos db_pagespeed
    mycol = mydb["dates"]           # Seleccionamos nuestra columna dates
    mydates = {     # Introdicimos en una variable llamada mydates un bson (utilizado en mongoDB) con las variables extraidas anteriormente y con los nombres de relacion con estas en la base de datos
    "_id": _id,     # La variable con nonmbre _id en la base de datos es la variable _id de nuestro programa
                    # Definimos las siguientes variables.
    "dominio": dominio,
    "porcentaje_movil": porcentaje_movil, 
    "orportunidades_movil": orportunidades_movil,
    "diagnosticos_movil": diagnosticos_movil,
    "porcentaje_ordenador": porcentaje_ordenador,
    "oportunidades_ordenador": oportunidades_ordenador,
    "diagnosticos_ordenador": diagnosticos_ordenador   
    }

    insertar = mycol.insert_one(mydates)        # Insertamos la el bson en la base de datos

    print(insertar)     

# En esta funcion avmos a comrpobar cuanta memoria esta consumiendo  nuestro proceso y asi poder controlarla.

def funcion_memoryMagnement(brower):
    memoria = psutil.virtual_memory()       # Utilizamos la libreria psutil para extraer la memoria virtual que esta consumiendo nuestro ordenador
    controlador = 100 * 1024 * 100      # Creamos el controlador el cual va a tener como resultado 100MB
    if memoria.available <= controlador:        # Cremaos la condicon si la memoria disponible es menor a 100 MB 
        brower.close                            # Cerramos el navegador
        exit()                                  # Cerramso el programa
    
# LLamamos a la primera funcion pasandole el array dominios y la variable _id
funcion_analizarURL(dominios, _id)