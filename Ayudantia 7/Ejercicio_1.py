import numpy as np
numClientes = int(input("ingrese el número de clientes: "))
edades = np.zeros((numClientes, 1))
for i in range(0, numClientes, 1):
    edades[i] = int(input(f"ingrese la edad del cliente {i}: "))
print("La edad mínima es ", edades.min())
print("La edad promedio es ", edades.mean())
print("La edad máxima es ", edades.max())
