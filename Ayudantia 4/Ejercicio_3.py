print("--- Sistema de Análisis de Riesgo ---")
edad = int(input("Ingrese la edad del paciente: "))
enfermedad = int(input("Ingrese 1 si tiene enfermedad crónica, 0 si no: "))

print("\n--- Resultados ---")

# Clasificación y riesgo combinado
if edad <= 26:
    print("Rango Etario: Juventud")

    if enfermedad == 1:
        print("Nivel de Riesgo: MEDIO")

    else:
        print("Nivel de Riesgo: BAJO")

elif edad >= 27 and edad <= 59:
    print("Rango Etario: Adultez")

    if enfermedad == 1:
        print("Nivel de Riesgo: ALTO")

    else:
        print("Nivel de Riesgo: MEDIO")

elif edad >= 60:

    print("Rango Etario: Persona Mayor")
    # Riesgo alto independiente de la enfermedad
    print("Nivel de Riesgo: ALTO")
