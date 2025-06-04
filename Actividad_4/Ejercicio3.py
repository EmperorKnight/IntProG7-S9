# Promedio de calificaciones
# ✓ Solicita al usuario 8 calificaciones, guárdalas en una lista y calcula el
# promedio.

import os

notas = []

os.system("cls || clear")
print("Introduzca 8 calificaciones del estudiante")

suma = 0
for i in range(1,9):
    calificacion = int(input(f"{i}) "))
    notas.append(calificacion)
    suma += calificacion

promedio = suma / len(notas)

os.system("cls || clear")
print(f"Las notas fueron: {notas}")
print(f"El promedio es de: {promedio:,}")
