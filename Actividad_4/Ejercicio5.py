# 5. Contar elementos mayores que un número
# Dada una lista de 10 números, contar cuántos son mayores que 50.

import os

os.system("cls || clear")
numeros = [35,75,100,150,23,45,60,89,90,10]

contador = 0

for i in numeros:
    if i > 50:
        contador += 1

print(f" \nEn la lista hay {contador:,} numeros mayores que 50 \n ")