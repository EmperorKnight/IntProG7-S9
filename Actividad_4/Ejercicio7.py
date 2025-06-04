# 7. Encontrar el máximo y el mínimo
# ✓ A partir de una lista de números reales, encuentra el mayor y el menor
# valor.

import os, random

numeros = []

valores = random.randint(1,10)
for i in range(valores):
    valores = random.randint(1,10)
    numeros.append(valores)

print(numeros)

mayor = numeros[0]
menor = numeros[0]

for i in numeros:
    if i > mayor:
        mayor = i
    elif i < menor:
        menor = i

print(mayor,menor)