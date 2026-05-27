import numpy as np

print("--- SISTEMA ANTICOLISIÓN DE DRONES ---")

# 1. Creamos el espacio aéreo (6x6)
# Usamos una lista de listas para que vean claramente dónde están los 1
espacio_aereo = np.array([
    [0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0]
])

# Coordenada del dron a evaluar
fila = 2
col = 3

sector_radar = espacio_aereo[fila-1: fila+2, col-1: col+2]  # Uso de slicing

print("\nSector escaneado (3x3):")
print(sector_radar)

# 3 y 4. Contar todos los drones del sector y restar el dron central
drones_totales = sector_radar.sum()
dron_central = espacio_aereo[fila, col]

vecinos_cercanos = drones_totales - dron_central

print(f"\nDrones vecinos detectados: {vecinos_cercanos}")

# 5. Operación lógica con el resultado
if vecinos_cercanos >= 2:
    print("¡ALERTA CRÍTICA! Alto riesgo de colisión. Cambiar altitud.")
else:
    print("Espacio aéreo seguro.")
