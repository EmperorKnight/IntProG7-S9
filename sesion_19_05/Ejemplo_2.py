estudiantes = ["Jorge Picado","Franklin Callejas","Josue Espinoza","Joshua Saenz"]
tamaño = len(estudiantes)

# Contar cuantos elementos posee el arreglo
print(f"Cantidad de estudiantes {tamaño}")

# Recorrer los elementos del arreglo
for estudiante in estudiantes:
    print(f"{estudiante} tiene {len(estudiante)} letras")
    vocales = "aeiou"
    sumavoc = 0
    for letra in estudiante:
        if letra in vocales:
            sumavoc += 1
        # print(f"{letra.upper()}" * 1)
    print(f"{estudiante} tiene {sumavoc} vocales")
