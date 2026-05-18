print("\n--- Calculadora de Materiales para Terreno ---\n")

largo = int(input("Ingrese el largo del terreno en metros: "))
ancho = int(input("Ingrese el ancho del terreno en metros: "))

# Cálculos geométricos
perimetro = 2 * (largo + ancho)  # También válido: (largo * 2) + (ancho * 2)
area = largo * ancho

print("\n--- Resumen de Compra ---\n")
print(
    f"Se requieren {perimetro} metros de malla y {area} metros cuadrados de pasto para el terreno.")
