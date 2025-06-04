# 4. Buscar un elemento
# ✓ Dada una lista de palabras, solicita al usuario una palabra y muestra si está
# o no en la lista.

import os

palabras = ["Azul","Cafe","Aguacate","Marron","Espacio"]

i = 1

while i != 0:
    os.system("cls || clear")
    palabra = input(f"Introduzca una palabra \n-> ").capitalize()

    if palabra in palabras:
        os.system("cls || clear")
        print("La palabra que introdujo esta en la lista \n ")
    else:
        os.system("cls || clear")
        print("La palabra que introdujo no esta en la lista \n ")
    
    i = int(input(f"¿Quiere volver a introducir la palabra? \nSi = 1 || No = 0 \n-> "))
