print("--- SISTEMA DE CIERRE DE SEMESTRE ---")

notas = [
    [4.5, 5.0, 5.5],
    [3.0, 3.5, 4.2],
    [6.0, 6.5, 6.2],
    [5.5, 4.8, 5.1]
]

filas = len(notas)
columnas = len(notas[0])

for i in range(filas):

    suma_notas = 0

    # Ciclo interno: Recorremos los 3 certámenes del alumno actual (i)
    for j in range(columnas):

        suma_notas += notas[i][j]

    # Una vez que termina el ciclo interno, ya tenemos la suma completa de ese alumno
    # Calculamos su promedio dividiendo por la cantidad de certámenes
    promedio = suma_notas / columnas

    # Evaluamos si aprueba o reprueba y mostramos el resultado
    if promedio >= 4.0:
        estado = "APROBADO"
    else:
        estado = "REPROBADO"

    print(f"Alumno {i}: Promedio {round(promedio, 2)} -> {estado}")
