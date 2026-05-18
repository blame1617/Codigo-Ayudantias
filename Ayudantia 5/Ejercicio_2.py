print("--- BUSCADOR DE JUGADAS ---")

partido = [1, 3, 1, 2, 7, 8, 6, 1, 2, 7, 9, 4, 1, 2, 5]
jugada_dt = [1, 2]  # Secuencia buscada

contador = 0
largo_partido = len(partido)
largo_jugada = len(jugada_dt)

# Recorremos con la ventana deslizante
for i in range(largo_partido - largo_jugada + 1):

    if partido[i: i + largo_jugada] == jugada_dt:
        contador += 1

# Veredicto final simplificado
if contador > 0:
    print(f"La secuencia fue encontrada {contador} veces.")
else:
    print("No se encontró la secuencia.")
