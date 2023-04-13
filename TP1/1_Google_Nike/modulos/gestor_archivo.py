# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 16:40:21 2023

@author: yazol
"""

import csv

#Se abre el archivo csv y se guarda en una lista de listas
def abrir_archivo (nombre_archivo):
    #Lista de listas
    lista_de_listas = [] 
    
    #Apertura del archivo
    with open (nombre_archivo, newline ='') as cvsfile:
            lector = csv.reader(cvsfile, delimiter = ",")
            
            #Saltea primera línea
            next (lector)
            
            for fila in lector:
                fila[1] = float(fila[1])
                lista_de_listas.append(fila)
                
            return (lista_de_listas)
      
        
#Defino una lista de precios para poder usarlos posteriormente
def pasar_lista_precios (registros):
   
    precios = []
     
    for fila in registros:
        fila[1] = float(fila[1])
        precios.append(fila[1])
         
    return (precios)