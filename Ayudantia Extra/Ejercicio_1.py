### Encontrar el número mayor ###
maximo = 0

edad = True


while edad:

    numero = int(input("Ingrese su numero: "))

    if numero > maximo:

        maximo = numero

    if numero <= 0:

        bandera = False

print(f"El número mayor es: {maximo}")
print("El número mayor es: ", maximo)
