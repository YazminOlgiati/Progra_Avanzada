# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 16:40:54 2023

@author: yazol
"""

import matplotlib.pyplot as plt

def graficar(lista_n, lista_g, posicion, titulo):
    
    #Fila 1, Columna 2, varío si es el primer o segundo gráfico
    plt.subplot(1, 2, posicion) 
    
    plt.plot(lista_n, label = "Nike")
    plt.plot(lista_g, label = "Google")
    
    plt.grid()
    plt.legend()
    plt.title(titulo)
    
    return
