# 6. Invertir una lista
# ✓ Pide 10 números al usuario, guárdalos en una lista e imprímelos en orden
# inverso.

import os

os.system("cls || clear")
print("Introduzca 10 numeros")

numeros = []

for i in range(1,11):
    numero = int(input(f"{i}) "))
    numeros.append(numero)

os.system("cls || clear")
print(numeros)
print(" ")
numeros.reverse()
print(numeros)
print(" ")