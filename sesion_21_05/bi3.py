fila = 3
columna = 3
matriz = []

for i in range(fila):
    matriz.append([])
    for j in range(columna):
        valor = int(input(f"Introduzca el valor para la posicion ({i}, {j})\n-> "))
        matriz[i].append(valor)

matrizb = []

for m in range(fila):
    matrizb.append([])
    for k in range(columna):
        valor1 = int(input(f"Introduzca el valor para la posicion ({m}, {k})\n-> "))
        matrizb[m].append(valor1)

matrizc = []

for i in range(fila):
    matrizc.append([])
    for j in range(columna):
        matrizc1 = matriz[i][j] + matrizb[i][j]
        matrizc[i].append(matrizc1)

fila = str()
for fila in matrizc:
    for columna in fila:
        print(columna, end=" ")
    print()
