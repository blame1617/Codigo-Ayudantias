import time
import random

print("--- ADIVINA RÁPIDO ---\n")

# El computador elige un número fácil (del 1 al 5)
numero_secreto = random.randint(1, 5)

print("Pensé un número del 1 al 5.")
print("¡Adivínalo rápido y presiona ENTER!\n")

# Empieza a medir el tiempo
inicio = time.time()

# El usuario intenta adivinar
respuesta = int(input("Tu intento: "))

# Termina de medir el tiempo y calculamos
fin = time.time()
# Opcional, se redondea el tiempo a dos decimales
tiempo_demorado = round(fin - inicio, 2)

print(
    f"¡Tu respuesta fue {respuesta}!, y te demoraste {tiempo_demorado} segundos.")

# esto devuelve true o false dependiendo del resultado
comparacion = (respuesta == numero_secreto)

print("\n--- RESULTADOS DEL DESAFÍO ---\n")
print(f"El número secreto era {numero_secreto}")
print(f"¿Acertaste?: {comparacion}")
