print("\n--- Conversor de Temperaturas de Laboratorio ---\n")

celsius = float(input("Ingrese la temperatura en grados Celsius (°C): "))

# Fórmulas de conversión
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print("\n--- Reporte de Conversión ---\n")
print(f"Temperatura ingresada: {celsius} °C")
print(f"Equivalencia en Fahrenheit: {fahrenheit} °F")
print(f"Equivalencia en Kelvin: {kelvin} K")
