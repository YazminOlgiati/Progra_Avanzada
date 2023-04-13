# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:17:30 2023

@author: yazol
"""

from flask import Flask, render_template, request
from modules.gestor_archivo import abrir_archivo

app = Flask(__name__)
lista_libros = []
RUTA = "./data/"
ARCHIVO = RUTA + "libros_leidos1.txt"

try:
    cargar_lista_desde_archivo(ARCHIVO, lista_libros)            
except FileNotFoundError:
    with open(ARCHIVO, "w") as archi:
        pass
        

#Se obtienen los datos que ingresó el usuario referidos a un nuevo 
#libro ingresado por el navegador, donde request.form es un diccionario, 
#y su contenido se puede acceder a través de las claves definidas en el 
#archivo html que contiene el formulario correspondiente
@app.route("/", methods=['GET', 'POST'])
def raiz():
    if request.method == 'POST':
        
        
        # Acá debería guardar la opción elegida del usuario
        
        # titulo = request.form["titulo"]
        # autor = request.form["autor"]
        # puntaje = request.form["puntaje"]
        # libro = {
        #     "nombre": titulo,
        #     "autor": autor,
        #     "puntaje": puntaje
        # }
        # lista_libros.append(libro)
        # guardar_libro_en_archivo(ARCHIVO, libro)
    
    if len(lista_libros) == 0:
        return render_template("home.html", esta_vacia=True)
    return render_template("home.html", esta_vacia=False, lista_libros=lista_libros )

    
@app.route("/add")
def agregar():
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)
    
    
#Al llamar a render_template, se pasa como primer parámetro el nombre del 
#documento html a utilizar como plantilla, y despues se le pasan como 
#argumentos adicionales las variables a las que vamos a acceder desde 
#dentro de la plantilla. De esta manera pasamos información de la 
#aplicación principal al html.