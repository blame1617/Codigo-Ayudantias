print("--- Buscador del Número Mayor ---")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# 1. Validación usando operadores lógicos
if num1 <= 0 or num2 <= 0 or num3 <= 0:
    print("Error: Todos los números deben ser positivos.")

else:
    # 2. Búsqueda del mayor encadenando comparaciones
    if num1 >= num2 and num1 >= num3:
        mayor = num1

    elif num2 >= num1 and num2 >= num3:
        mayor = num2

    else:
        mayor = num3

    print(f"El número mayor es: {mayor}")
