print("--- SISTEMA DE INVENTARIO ---")

bodega = [
    [10, 5, 2, 8],
    [0, 12, 4, 3],
    [7, 1, 15, 0]
]

total_productos = 0

filas = len(bodega)
columnas = len(bodega[0])

for i in range(filas):
    for j in range(columnas):

        cantidad_estante = bodega[i][j]

        print(f"Pasillo {i}, Estante {j}: {cantidad_estante} productos")

        total_productos += cantidad_estante

print(f"\nEl inventario total de la bodega es de {total_productos} productos.")
