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


options = Options()
brower = webdriver.Firefox(options=options, executable_path=r"C:\PROYECTOS\WebDriver\Firefox\geckodriver.exe")
website_URL ="https://developers.google.com/speed/pagespeed/insights/?hl=es"
brower.get(website_URL)
elem = brower.find_element_by_css_selector("input.url.label-input-label")
elem.send_keys('https://www.udemy.com/')
elem.send_keys(Keys.RETURN)
web = brower.current_url



brower.get(web)
puntuacion_movil = brower.find_element_by_class_name("lh-gauge__percentage").text


cambiar = brower.find_element_by_id(":8")
cambiar.click()
puntuacion_ordenador = brower.find_element_by_class_name("lh-gauge__percentage").text
#puntuacion_ordenador = brower.find_element_by_xpath("//a[@class='lh-gauge__wrapper lh-gauge__wrapper--pass lh-gauge__wrapper--huge']//div[@class='lh-gauge__svg-wrapper']").text
print(puntuacion_movil)
print(puntuacion_ordenador)