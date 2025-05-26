filas = int(input(f"¿Cuantas filas quieres? \n-> "))
columnas = int(input(f"¿Cuantas columnas quieres? \n-> "))

matriz = []

for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor = int(input(f"Ingrese el valor para la posición ({i}, {j}): \n-> "))
        matriz[i].append(valor)

print(" ")

for fila in matriz:
    for columna in fila:
        print(columna, end=" ")
    print()

suma = 0
for fila in matriz:
    for columna in fila:
        suma += columna

print(" ")
print(f"La suma de los elementos es: {suma:,}")

nueva_matriz = [[]]
escalar = int(input(f"Introduzca el escalar de la nueva matriz \n-> "))
for fila in matriz:
    for columna in fila:
        n_matriz = escalar * columna
        nueva_matriz.append(n_matriz)
    
# print(nueva_matriz)

for fila in nueva_matriz:
    for columna in fila:
        print(columna, end=" ")
    print()