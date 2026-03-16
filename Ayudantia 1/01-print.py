############### Print y Tipos ###############

print("Hello World")  # Strings
print(1)  # Integers / Enteros
print(1.3)  # Float / Decimales
print(True)  # Valores Logicos (Verdadero y Falso)
print(3 + 4, 3*4, 12/4)  # Operaciones matematicas
print("Hello " + "World", "Hello " * 5)  # Operaciones con strings

############### Multiples datos en un Print ###############

# La coma (,) nos permite separar datos dentro de un print
print("Hola", 12, True)

############### Separacion en lineas ###############

# Por defecto, cada print se genera en una nueva linea
print("Hola")
print("Mundo")

# Para evitar esto, podemos usar el parametro de ,end="", de esta forma el nuevo print sigue al anterior
print("Hola ", end="")
print("Mundo")

# Si queremos separar el contenido de un print en multiples lineas, lo podemos hacer con el operador \n
print("Hola\nMundo")
