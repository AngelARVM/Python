"""
Manejo de archivos
Manejo de listas
Manejo libreria time
"""


import time
from datetime import datetime as dt

#ACLARACION: en ruta windows, direccion d es solo para archivo de pruebas.
#de ser requerido trabajar con archivo hosts orginal quitar d de la ruta.
#RECOMENDACIO: guardar una copia del archivo hosts orginal antes de iniciar el programa.


#Windows C:\Windows\System32\drivers\etc\d
#Unix /etc/hosts

ruta_host_win = r"C:\Windows\System32\drivers\etc\d\hosts"
ruta_host_unix = r"/etc/hosts"


#Agregue aquí los sitios web que desea bloquear.
lista_websites = [
    "www.facebook.com",
    "facebook.com",
    "mail.google.com",

]


#Modifique aquí su franja horaria de trabajo
horario_inicio = 14
horario_fin = 18


#Modifique aquí direccion a la que quiere ser redireccionado.
#Por defecto, se redirecciona a "127.0.0.1"
redireccion = "127.0.0.1"



while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, horario_inicio) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, horario_fin):
        print("working")
        with open(ruta_host_win, 'r+') as file:
            contenido = file.read()
            for website in lista_websites:
                if website in contenido:
                    pass
                else:
                    file.seek(0,2)
                    file.write("\n" + redireccion + " " + website )
    else:
        print ("free")
        with open(ruta_host_win, 'r+') as file:
            contenido = file.readlines()
            file.seek(0)
            for line in contenido:
                if not any(website in line for website in lista_websites):
                    file.write(line)
                file.truncate()
            
    time.sleep(5)
