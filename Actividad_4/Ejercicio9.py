# 9. Separar pares e impares
# ✓ Llena una lista con 10 números enteros aleatorios entre 1 y 100, y
# sepáralos en dos listas: pares e impares.

import random

numeros = []
pares = []
impares = []

for i in range(10):
    valores = random.randint(1,100)
    numeros.append(valores)

for i in numeros:
    if (i % 2) == 0:
        pares.append(i)
    else:
        impares.append(i)

print(pares)
print(impares)