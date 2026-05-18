############### Variables y tipos de datos ###############

nombre = "Juan"
edad = 20
promedio = 6.2
aprobado = True
# Esto se conoce como lista y lo veremos mas adelante
mascotas = ["Firulais", "Washington", "Bobby"]

print(nombre, edad, promedio, aprobado)

############### Modificación de variables ###############

# Podemos cambiar tanto el valor de una variable como el tipo de dato que contiene

edad = 20
print(edad)

edad = "veinte"  # Asignamos nuevamente la variable edad, pero esta vez a un string
print(edad)

############### Reglas y buenas practicas para nombrar variables ###############

# NO SE PUEDE

""" 1usuario = "Juan"  # Comenzar con un numero
nombre usuario = "Pedro"  # Colocar espacios, para eso se usa el guion bajo _
usu@rio = "Rodrigo"  # Colocar simbolos especiales (@, ?, !)
print = 22  # Usar palabras reservadas (print, input, True, if, for, etc) """

# Buenas practicas

# Usar nombres con significado, que cualquier persona pueda comprender
nombre_usuario = "Juan"
NombReUsuARio = "Pedro" """ Usar una convencion consistente para nombrar variables 
(siempre minuscula, primera letra en mayuscula, etc). En lo personal utilizo palabra1_palabra2_etc"""

############### Textos formateados ###############

# Nos permiten imprimir variables dentro de un texto

nombre = "Matias"

print(f"Bienvenido {nombre}")
