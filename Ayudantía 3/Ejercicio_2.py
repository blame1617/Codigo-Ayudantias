import time
import random

print("--- PLANTA DE ENERGÍA SOLAR ---\n")

# 1. Inicio de la recolección
input("Presiona ENTER para abrir los paneles solares...\n")
inicio = time.time()

# 2. Fin de la recolección
input("Presiona ENTER nuevamente para cerrar los paneles")
fin = time.time()

# 3. Transformación de datos (Matemática y Tiempo)
tiempo_exposicion = fin - inicio
print(
    # round() redondea a dos decimales
    f"\nPaneles cerrados. Tiempo de exposición: {round(tiempo_exposicion, 2)} segundos.")

# 4. Factor climático (Random)
intensidad_solar = random.randint(10, 50)

# 5. Cálculo final
energia_almacenada = tiempo_exposicion * intensidad_solar

# 6. Reporte Final
print("\n--- REPORTE DE BATERÍAS ---\n")
print(
    f"⚡ Energía total almacenada con éxito: {round(energia_almacenada)} MWh.")
