# PageSpeed-Insights---Selenium-Python

En este proyecto vamos a realizar una herramienta en python v.3.7.3, la cual realizará automaticamente el analisis de diferentes URLs en page speed insight.   
      
![Gif](source/pg_gif.gif)

## Funcionamiento 
El funcionamiento de la herramienta es el siguiente, un usuario escribe en un archivo txt las URLs que desea analizar con page speed insight. Ahora el usuario tendrá que ejecutar el python pg_speed_analize.py, el cual gracias a selenium y a un web driver irá recorriendo las diferentes URLs dentro de la web y extrayendo la información más relevante, la cual hemos progrmado previamente, una vez recogida esta informacion se conectará a un docker en el cual reside un contenedor de MongoDB, el cual ira recogiendo la información extraida por el usuario.               
Para poder ver toda esta informacion extraida, en un formato amigable, hemos desarrollado una web en Django la cual se conecta al docker y desde este a la base de datos, extrallendo la información de esta y mostrandola en su template.   

![Esquema](source/esquema.png)   

## Instalacion 
Necesitaremos la version de python 3.7.3    
- Este es el *[link de descarga.](https://www.python.org/downloads/)*         
Dentro de python tendremos que tener instaladas las siguientes librerias.           
- Libreria de Selenium     
``pip install selenium``
- Libreria de MongoDB    
``pip install pymongo``
- Libreria de Psutil          
``pip install psutil``
- Django        
``pip install django``          
Dentro de django tendremos que instalar tambien algunas librerias, es recomendable utilizar un virtual enviroment, para poder instalarlas en una carpeta que no se encuentre Path de Python. Esto tambien depende de la instalacion que realizaras de Python.
- Estas son las librerias que tendremos que tener en Django:       
    ``pip install djongo``                      
    ``pip install django_tables2``            
    ``djangotoolbox``

Para la instalación de Docker solo tendremos q