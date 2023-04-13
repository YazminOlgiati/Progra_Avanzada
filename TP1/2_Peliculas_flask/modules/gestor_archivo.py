# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:24:36 2023

@author: yazol
"""

#datos/frases_de_peliculas.txt

#Se abre el archivo y es guardado en un diccionario
def abrir_archivo ():

    with open("datos/frases_de_peliculas.txt", "r") as archivo:

        #Primero se crea un diccionario vacío, diccionario.
        diccionario = {}
    
        #Lectura del archivo
        leer = archivo.readlines()
        
        for linea in leer:
            #Lo que está antes del ";" se guarda en frase
            #Lo que está después del ";" se guarda en pelicula
            (frase, pelicula) = linea.split(";")
            
            #La frase es la clave, la película es el valor
            diccionario[str(pelicula)] = frase
            
            print(diccionario)
        
            
        # for frase, pelicula in diccionario.items():
        #     print(frase, pelicula)
    
        return diccionario           
           
           
           