# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 17:33:52 2023

@author: yazol
"""

import gestor_archivo as gestor
import procesador_datos as procesador
import graficador as graficador
import matplotlib.pyplot as plt


def main():
    
    #Apertura de archivos
    lista_nike = gestor.abrir_archivo("../datos/nike.csv")
    lista_google = gestor.abrir_archivo("../datos/google.csv")

    #Pasaje de precios a una lista
    precios_n = gestor.pasar_lista_precios(lista_nike)
    precios_g = gestor.pasar_lista_precios(lista_google)

    #Normalización de datos
    norm_n = procesador.normalizar(precios_n)
    norm_g = procesador.normalizar(precios_g)
    
    #Variación porcentual
    variacion_n = procesador.variacion_porcentual(precios_n)
    variacion_g = procesador.variacion_porcentual(precios_g)
    
    #Caída porcentual primer trimestre de Google
    caida_g = procesador.caida_porcentual(precios_g)
    #Se utiliza la función 'round()' para acotar los decimales del resultado
    print(f"En el primer trimestre de Google, la caída fue de ", round(caida_g, 2), "%")

    #Crecimiento porcentual
    crecimiento_g = procesador.crecimiento_porcentual(precios_g)
    print(f"El porcentaje de repunte fue de ", round(crecimiento_g, 2), "%")
    
    
    #Gráficos
    graficador.graficar(norm_n, norm_g, 1, "Precios normalizados")
    graficador.graficar(variacion_n, variacion_g, 2, "Variación porcentual")
    plt.show()

    

#b) ¿Se corresponde aproximadamente el valor calculado en el punto anterior 
#con la caída para Google en el gráfico de la derecha? Justificar.
#Según el cálculo, esta caída corresponde a un 34%, aproximadamente observando
#la gráfica de la derecha, en el eje vertical la variación se corresponde a un 34%.


#d) ¿Se corresponde aproximadamente el valor calculado en el punto anterior 
#con el repunte para Google en el gráfico de la derecha? Justificar.
#Según el cálculo, esta repunte corresponde a un 50%, aproximadamente observando
#la gráfica de la derecha, en el eje vertical la variación se corresponde a un 50%.

main()