##################### Solución 1 de la pauta #####################
import numpy as np
import random

numDados = int(input("ingrese el número de dados: "))
dados = np.zeros((numDados, 1))

for i in range(0, numDados):
    dados[i] = random.randint(1, 6)

print(dados)
print("El número de 6 es ", (dados == 6).sum())
# cuando hacemos dados == 6 creamos una matriz de true y false, como true vale 1 y false 0
# al calcular la suma de esa nueva matriz podemos saber cuantas veces salio 6 en los dados
print("La probabilidad es ", (dados == 6).sum()/numDados)

##################### Solución 2 de la pauta #####################

numDados = int(input("Ingrese el número de veces que desea tirar el dado: "))

resultados = np.random.randint(1, 7, size=numDados)

cantidad_seis = np.count_nonzero(resultados == 6)
# count_nonzero cuenta todas las instancias que no son 0, como mencionamos antes, al hacer resultados == 6 creamos una matriz con true o false
# como false equivale a 0, solo se van a contar los true, que equivalen al numero de veces que sale el 6

probabilidad_seis = cantidad_seis / numDados

print(f"Número de veces que salió 6: {cantidad_seis}")
print(f"Probabilidad estimada de obtener un 6: {probabilidad_seis:.4f}")
