edades = [18,17,17,16,20,27,19,21]
print(edades)

# ordenar
edades.sort()
print(edades)
# mayor a menor
edades.sort(reverse=True)
print(edades)

# Libreria estadisticas
import statistics as st

# Mostrar la media
media = st.mean(edades)
print(f"Media: {media}")

# Mostrar la moda
moda = st.mode(edades)
print(f"Moda: {moda}")
