# 8. Eliminar duplicados
# ✓ Dada una lista con valores repetidos, crea una nueva lista sin duplicados.

numeros = [1,1,2,2,3,3,4,4,5,5]
nueva = []

for i in numeros:
    if i not in nueva:
        nueva.append(i)

print(nueva)
