#### Solución N°1 - Slicing #####

numero_str = input("Ingrese un número: ")

numero_invertido = numero_str[::-1]

if numero_str == numero_invertido:
    print("Tu número es palíndromo")
else:
    print("Tu número no es palíndromo.")


#### Solución N°2 - Uso de indices #####

numero_str = input("Ingrese un número: ")
largo = len(numero_str)

es_palindromo = True

for i in range(largo // 2):

    if numero_str[i] != numero_str[largo - 1 - i]:
        es_palindromo = False

if es_palindromo:
    print("Tu número es palíndromo")
else:
    print("Tu número no es palíndromo.")


#### Solución N°3 - Uso de listas #####

numero_str = input("Ingrese un número: ")

lista_original = list(numero_str)
lista_revertida = []

largo = len(numero_str)

for i in range(largo):
    digito = numero_str[-i-1]
    lista_revertida.append(digito)

if lista_original == lista_revertida:
    print("Tu número es palíndromo")
else:
    print("Tu número no es palíndromo.")
