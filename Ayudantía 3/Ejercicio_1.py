import time
import random
import math

print("--- PISTA DE CARRERAS ---")
nombre = input("Ingresa tu nombre: ")

print("Comienza la cuenta regresiva\n")
# 1. Uso de TIME: Cuenta regresiva
time.sleep(1)
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...\n")

# 2. Uso de RANDOM: Asignamos una velocidad al azar (entre 20 y 60 metros por segundo)
velocidad = random.randint(20, 60)

distancia = 500
tiempo = distancia / velocidad

# Usamos MATH para redondear hacia arriba a un número entero
tiempo_final = math.ceil(tiempo)

print(
    f"¡Carrera finalizada!, el auto de {nombre} alcanzó una velocidad de {velocidad} metros por segundo, llegando a la meta en {tiempo_final} segundos.")
