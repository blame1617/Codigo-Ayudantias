# Crea un programa que, usando un doble `for` y la librería `random`,
# cree una matriz de $X$ por $X$ (siendo $X$ un número que ingresa el usuario por teclado).

# La matriz debe rellenarse automáticamente con números aleatorios entre el `1` y el `3`.

# Con esa matriz recién creada, tu programa debe realizar las siguientes tareas de forma secuencial:
# 1. Mostrar la lista completa en formato matriz (cuadrícula) usando `for` y `print`.
# 2. Contar y mostrar la cantidad exacta de `1s`, `2s` y `3s` que existen en toda la matriz.
# 3. Modificar la matriz, cambiando **todos los valores de los bordes por un `0`**,
# y mostrar la nueva matriz resultante en formato cuadrícula.

import random
tamaño = int(input("Ingrese el tamaño de la matriz: "))
matriz = []
print()
for i in range(tamaño):
    temporal = []
    for j in range(tamaño):
        numero = random.randint(1, 3)
        temporal.append(numero)
    matriz.append(temporal)

for i in range(tamaño):
    print(*matriz[i])

suma_1 = 0
suma_2 = 0
suma_3 = 0

for i in range(tamaño):
    for j in range(tamaño):
        if matriz[i][j] == 1:
            suma_1 += 1
        elif matriz[i][j] == 2:
            suma_2 += 1
        else:
            suma_3 += 1
print()
print(f"Hay {suma_1} números 1 en la matriz, {suma_2} números 2 y {suma_3} números 3")
print()
for i in range(tamaño):
    for j in range(tamaño):
        if i == 0 or i+1 == tamaño or j == 0 or j + 1 == tamaño:
            matriz[i][j] = 0
    print(*matriz[i])
print()
