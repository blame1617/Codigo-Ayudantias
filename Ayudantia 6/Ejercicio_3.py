print("--- PANEL DE DIAGNÓSTICO ---")

# 1. Solicitamos el tamaño (Matriz cuadrada de N x N)
n = int(input("Ingrese el tamaño del panel de sensores: "))

panel = []

# 2. CREACIÓN DINÁMICA DE LA MATRIZ
for i in range(n):

    # Creamos la lista temporal para la fila actual
    fila_temporal = []

    for j in range(n):

        if i == j:
            fila_temporal.append(1)  # Encendemos el sensor (Diagonal)
        else:
            fila_temporal.append(0)  # Apagamos el sensor (Resto del panel)

    # Una vez que la fila temporal está completa, la agregamos a la matriz principal
    panel.append(fila_temporal)


# 4. IMPRESIÓN VISUAL
print("\nEstado del panel:")
for i in range(n):
    print(panel[i])
