# 1. Mensaje de bienvenida
print("--- Bienvenido a la Calculadora Simple ---")

# 2. Solicitud de números (casteados a float para permitir decimales)
numero_1 = float(input("Por favor, ingresa el primer número: "))
numero_2 = float(input("Por favor, ingresa el segundo número: "))

# 3. Operaciones matemáticas
suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2
division = numero_1 / numero_2

# 4. Impresión de resultados
print("\n--- Resultados ---")
print(f"El resultado de la suma es: {suma}")
print(f"El resultado de la resta es: {resta}")
print(f"El resultado de la multiplicación es: {multiplicacion}")
print(f"El resultado de la división es: {division}")
