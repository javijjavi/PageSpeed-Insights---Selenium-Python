
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



try:
    with open('ips.txt', 'r') as dominio:
        dominios = dominio.readlines()
    with open('ips.txt', 'r') as dominio:
        dominios = [line.strip() for line in dominio]
except:
    print("No se ha encontrado el archivo dominios.txt, o se ha localizado algun fallo relacionado con el, porfavor revisalo.")


def funcion_analizarURL(dominios):
    for dominio in dominios:
        options = Options()
        options.headless = True
        brower = webdriver.Firefox(options=options, executable_path=r"C:\PROYECTOS\WebDriver\Firefox\geckodriver.exe")
        website_URL ="https://db-ip.com/"
        brower.get(website_URL)
        elem = brower.find_element_by_id("search_input")
        elem.clear()
        elem.send_keys(dominio)
        elem.send_keys(Keys.RETURN)
        web = brower.current_url
        funcion_sacarINF(web, brower)
        del elem
        del web



def funcion_sacarINF(web, brower):
    brower.get(web)
    
    tabla_datos = brower.find_elements_by_xpath("//table[@class='table table-norowsep']//td")
    datos = []
    for dato in tabla_datos:
        text = dato.text
        datos.append(text)
    
    time.sleep(2)
    brower.close()

   # print("DOMINIO----------------------------------"+dominio)
    print("ASN-------------------------------------"+datos[2])
    print("ISP-------------------------------------"+datos[3])
    print("Organizacion----------------------------"+datos[4])
    print("Pais----------------------------------- "+datos[7])
    print("Estadado--------------------------------"+datos[8])
    print("Ciudad----------------------------------"+datos[9])

funcion_analizarURL(dominios)
