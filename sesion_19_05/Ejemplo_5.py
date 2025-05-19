# Leer x cantidad de numeros y decir cuantos son pares y cuantos son impares
suma_pares = 0
suma_impares = 0
numeros = []

while(True):
    numero = int(input(f"Dime un numero \n-> "))
    numeros.append(numero)

    resp = input(f"¿Desea agregar otro? [S] si, [N] no: \n-> ")
    if resp.upper() == "N":
        False
        break

for numero in numeros:
    if (numero % 2) == 0:
        suma_pares += 1
    elif numero % 2 != 0:
        suma_impares += 1

print(f"Cantidad de pares: {suma_pares} \nCantidad de impares: {suma_impares}")
