# 2. Sumar los elementos de una lista
# ✓ Solicita 10 números al usuario, guárdalos en una lista y muestra la suma
# total.

import os

os.system("cls || clear")
numeros = []

print("Introduzca 10 numeros enteros")

for i in range(1,11):
    numero = int(input(f"{i}) "))
    numeros.append(numero)

suma = 0
for i in numeros:
    suma += i

os.system("cls || clear")
print(f"Los numeros introducidos fueron {numeros}")
print(f"La sumatoria de todos los numeros da un total de {suma:,}")