# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:28:10 2023

@author: yazol
"""

import gestor_archivo as gestor
import random as r

#Muestra las opciones del menú
def mostrar_menu():
    
    print(
        
        "\n" + "#####################################" + "\n"
        "# Películas: Preguntas y respuestas #" + "\n"
        "#####################################" + "\n"
        "Elige una opción" + "\n" + "\n"
        "1 - Mostrar lista de películas." + "\n"
        "2 - ¡Trivia de película!" + "\n"
        "3 - Mostrar secuencia de opciones seleccionadas previamente." + "\n"
        "4 - Borrar historial de opciones." + "\n"
        "5 - Salir." + "\n"
      
        )


#Opción 1: mostrar lista de películas
def mostrar_peliculas(diccionario):
    
    #Ordenamiento alfabéticamente mediante "sorted()"
    #Indexación de la lista ordenada mediante "enumerate()" comenzando con "1"
    for i, lista in enumerate(sorted(diccionario.items()), 1):
    
        #return
        (print(i, lista[0])) 
        
        #parece que el return no anda
        #le comenté el return y ahora imprime bien la lista 
        #cuando se elige la opción 2 (y si opcion=!2 no la muestra)
        
        
        
#Opción 2: Trivia de Películas        
def mostrar_trivia(diccionario): 
    
        #Mediante choice() se obtiene un valor random del diccionario
        x = r.choice (list(diccionario.values()))
        #Se hace corresponder el valor con la clave
        clave = [i for i in diccionario if diccionario[i] == x]
       
        #Se asigna solo una respuesta correcta mediante la obtención de las claves
        a = r.choice(list(diccionario.keys()) )
        b = clave[0]
        c = r.choice(list(diccionario.keys()))
        
        print ("\n Elija opción 1, 2 o 3")
        print ( "\n ", "Frase: ", x)
        print ("\n")
        
        ##### no entiendo esto ##########################################
        fa = -1
        fr = -1
        cf = 0
        pelispartida=[a,b,c]
        orden_muestreo=[]

        while cf<3:
            #randint() devuelve un número entero incluido entre los valores indicados
            f=r.randint(0,2)
            if f != fa and fr != f:    
                print(f'{cf+1}) {pelispartida[f]}')
                orden_muestreo.append(pelispartida[f])
                fr = fa
                fa = f
                cf += 1
        #################################################################
        
        #Pedido de opciones por teclado
        eleccion = input("¿A qué película pertenece la frase?: ")
        opciones = ['1','2','3']
        
        #Se corrobora que el número ingresado corresponda a las opciones 
        #permitiendo volver a ingresar una opción mientras no sea correcta
        if eleccion not in opciones:
            while eleccion not in opciones:
                eleccion = input("/n" + "Elija una opcion valida : ")
        
        #convierte lo guardado en input (string) en un entero
        eleccion = int(eleccion)  
        
        #Se crea un archivo que almacena las opciones elegidas anteriormente 
        archivo_historial = open('historial.txt','a+')
        archivo_historial.write(str (eleccion) + ' ')
       
        archivo_historial.close()
        
        #Informe de respuesta correcta o incorrecta
        if orden_muestreo[eleccion - 1] == b:
            print ("\nFelicidades! Elegiste la opción correcta")
        else:
            print(f'\nERROR! La frase pertenece a {b}')
        
        
        
#Opción 3: mostrar historial   
def mostrar_historial(historial):
    
    archivo = open('historial.txt')
    lineas = archivo.readlines()
    
    return(print (lineas))        


        
#Opción 4: borrar historial        
def borrar_historial (p_historial):
    
    archivo = open('historial.txt', 'r+')
    archivo.truncate(0)
    
    archivo.close()
        
            
#Elecciones del menú
def opciones_menu():
    opcion = 0
    diccionario = gestor.abrir_archivo()
    
    
    #Se muestra el menú mientras la opción sea distinta a "5 - Salir"
    
    while (opcion != 5): 
        
        mostrar_menu()
        
        opcion = input("Elige una opción: ")
          
        
        if opcion == '1':
            mostrar_peliculas(diccionario)
            print ("\n" )
            
        elif opcion == '2':
            mostrar_trivia(diccionario)
            print ("\n" ) 
            
        elif opcion == '3':
            mostrar_historial("historial.txt")
            print ("\n" )
            
        elif opcion == '4':
            borrar_historial("historial.txt")
            print("Historial borrado \n")
            
        else:
            print("Opción no válida")
            