############### Tipo de dato por defecto en input ###############

# Input considera cualquier informacion que ingresemos como una string, independiente de que sea un numero u otro.

edad = input("Ingrese su edad:\n>")
print(type(edad))  # <class `str`> indica que se esta tomando como string

############### Funciones de conversion ###############

# Existen funciones que permiten transformar un tipo de dato en otro

edad = int(input("Ingrese su edad:\n>"))
# <class `int`> indica que se cambio exitosamente el tipo del input a un integer o entero.
print(type(edad))

# Precaucion, si intentamos cambiar un string de texto a numero dara error (Ej: Escribir veinte en vez de 20)

# ValueError: invalid literal for int() with base 10
edad = int(input("Ingrese su edad:\n>"))
