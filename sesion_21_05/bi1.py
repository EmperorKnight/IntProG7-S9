# arreglo bidimensional
# dos dimensiones

matriz = [[1,2,3],[1,2,3]]

for fila in matriz:
    for columna in fila:
        print(columna, end=" ")
    print()

suma = 0
for fila in matriz:
    for columna in fila:
        suma += columna

print(f"La suma de los elementos es: {suma}")