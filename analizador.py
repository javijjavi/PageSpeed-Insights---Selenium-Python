#!/usr / bin / env python 
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


#profile.set_preference("general.useragent.override", "[user-agent string]")
#profile.set_preference("general.useragent.override", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0")

# Introducimos la variable "options" con la cual conseguiremos que nuestro navegador se ejecute en modo background reduciendo el consumo de cpu.
# A continuacion llamamos al driver de firefox y le intreducimos la variable options para el background y el path de nuestro firefox que previamente tenemos que tener descargado.

try:
    options = Options()
    options.headless = True
    brower = webdriver.Firefox(options=options, executable_path=r"C:\PROYECTOS\WebDriver\Firefox\geckodriver.exe")
except:
    print("Tiene que descargar geckodriver.exe y a continuacion introducirlo en la siguiente dirección:")
    print("C:\PROYECTOS\WebDriver\Firefox\geckodriver.exe")
    time.sleep(10)
    exit()

# Ya tendriamos que tener todos lo necesario si hemos llegado hasta aqui. HF!

website_URL ="https://developers.google.com/speed/pagespeed/insights/?hl=es"
brower.get(website_URL)

#Introducimos la pagina web que queremos analizar
#def funcion_buscarweb():
elem = brower.find_element_by_css_selector("input.url.label-input-label")
elem.send_keys("https://github.com/")
elem.send_keys(Keys.RETURN)
#time.sleep(20)
web = brower.current_url
brower.get(web)
puntuacion_movil = brower.find_element_by_class_name("lh-gauge__percentage").text
print(puntuacion_movil)


frases_encontradas = brower.find_elements_by_xpath("//div[@class='lh-audit-group lh-audit-group--load-opportunities']//div[@class='lh-audit__title']//span")
orportunidades_movil = []
print("OPORTUNIDADES")
for frase in frases_encontradas:
    text = frase.text
    orportunidades_movil.append(text)
    print(text)

frases_encontradas = brower.find_elements_by_xpath("//div[@class='lh-audit-group lh-audit-group--diagnostics']//span[@class='lh-audit__title']//span")
diagnosticos_movil = []
print("DIAGNOSTICOS")
for frase in frases_encontradas:
    text = frase.text
    diagnosticos_movil.append(text)
    print(text)

cambiar = brower.find_element_by_id(":8")
cambiar.click()

#Ya estmos en PC
#web = brower.current_url
#brower.get(web)
#brower.implicitly_wait(2)#seconds 
#wait = WebDriverWait(brower, 2)
#wait.until(lambda brower: brower.current_url != web)

print("En ordenador")
elemento_ordenador = brower.find_element_by_xpath("//a[@class='lh-gauge__wrapper lh-gauge__wrapper--pass lh-gauge__wrapper--huge']//div[@class='lh-gauge__percentage']").text
print(elemento_ordenador)

frases_encontradas = brower.find_elements_by_xpath("//div[@class='lh-audit-group lh-audit-group--load-opportunities']//div[@class='lh-audit__title']//span")
oportunidades_ordenador = []
print("OPORTUNIDADES")
for frase in frases_encontradas:
    text = frase.text
    oportunidades_ordenador.append(text)
    print(text)

frases_encontradas = brower.find_elements_by_xpath("//div[@class='lh-audit-group lh-audit-group--diagnostics']//span[@class='lh-audit__title']//span")
diagnosticos_ordenador = []
print("DIAGNOSTICOS")
for frase in frases_encontradas:
    text = frase.text
    diagnosticos_ordenador.append(text)
    print(text)

time.sleep(5)

brower.close()