# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 16:40:40 2023

@author: yazol
"""



#Normalización (0 a 1) de los precios
def normalizar(lista):
    
    lista_normalizada = []
    
    for numero in lista:
        valor = ((numero - min(lista)) / (max(lista) - min(lista)))
        
        lista_normalizada.append(valor)
        
    return (lista_normalizada)



#Se convierten los datos a porcentaje para calcular la variación porcentual
def variacion_porcentual(lista):
    
    lista_porcentual = []

    valor_ref = lista[0]
    
    for i in range(len(lista)):
        valor = ((lista[i] - valor_ref)/valor_ref) * 100 
        lista_porcentual.append(valor)

        
    return (lista_porcentual)



#Se calcula la caída porcentual en el primer trimestre
def caida_porcentual(lista):
    
    #conversión a porcentaje mediante la función ya creada
    lista_porcentual = variacion_porcentual(lista)
    
    #máximo en el primer trimestre
    precio_max = max(lista_porcentual[0:89]) 
    
    #índice del máximo
    index_max = lista_porcentual[0:89].index(precio_max) 
    
    #precio mínimo a partir del máximo
    precio_min = min(lista_porcentual[index_max:89]) 
    
    #cálculo de caída
    caida = precio_max - precio_min
    
    return (caida)
    
   
    
#Se calcula el repunte o crecimiento en porcentaje
def crecimiento_porcentual(lista):
     
     #conversión a porcentaje mediante la función ya creada
     lista_porcentual = variacion_porcentual(lista)
     
     #mínimo valor de la lista
     minimo = min(lista_porcentual)
     
     #último valor de la lista
     ultimo = lista_porcentual[-1]
     
     #cálculo de crecimiento
     crecimiento = ultimo - minimo
     
     return (crecimiento)