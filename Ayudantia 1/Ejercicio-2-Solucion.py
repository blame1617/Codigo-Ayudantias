# 1. Mensaje de bienvenida
print("--- Bienvenido a la Caja Rápida del Supermercado ---")

# 2. Mostrar la lista de productos
print("Arroz --- $1000 / kilo")
print("Manzana Verde --- $500 / unidad")
print("Pan --- $1500 / kilo")

# 3. Ingreso de datos (con casteo de tipos)
producto = input("Ingrese el nombre del producto: ")
precio_unitario = int(input("Ingrese el precio unitario del producto: $"))
cantidad = float(input("Ingrese la cantidad que lleva: "))

# 4. Cálculos matemáticos
subtotal = precio_unitario * cantidad
iva = subtotal * 0.19
total_final = subtotal + iva

# 5. Impresión de la boleta (usando f-strings y \n para ordenar)
print("\n--- BOLETA DE COMPRA ---")
print(f"Producto: {producto} (x {cantidad})")
print(f"Subtotal: ${subtotal}")
print(f"IVA (19%): ${iva}")
print(f"TOTAL A PAGAR: ${total_final}")
print("------------------------")
print("¡Gracias por su compra!")
