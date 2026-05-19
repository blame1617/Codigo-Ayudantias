print("--- SISTEMA DE TAQUILLA ---")

sala_cine = [
    [1, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]

# Inicializamos el contador en cero antes del ciclo
asientos_libres = 0

# Calculamos las dimensiones dinámicamente
filas = len(sala_cine)
columnas = len(sala_cine[0])

# Recorrido de la matriz
for i in range(filas):
    for j in range(columnas):

        # Evaluamos la coordenada actual
        if sala_cine[i][j] == 0:
            asientos_libres += 1

# Imprimimos el resultado fuera de todos los ciclos
print(f"Para la función actual quedan {asientos_libres} butacas disponibles.")
