# 10. Sumar elementos en posiciones pares
# ✓ Suma los elementos que se encuentran en posiciones pares de la lista.

import random

numeros = []

for i in range(10):
    valores = random.randint(1,100)
    numeros.append(valores)

posicion = 0
suma = 0
for i in numeros:
    if (posicion % 2) == 0:
        suma += i
    posicion += 1

print(numeros)
print(suma)
