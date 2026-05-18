### Adivina el número ###

import random

numero_secreto = random.randint(1, 100)

bandera = True


print("¡Bienvenido al juego de adivinar el número!")

print("He pensado en un número entre 1 y 100.")

while bandera:

    valor_ingresado = int(input("Introduce tu número: "))

    if valor_ingresado > numero_secreto:

        print("El número es muy alto. ¡Intenta de nuevo!")

    elif valor_ingresado < numero_secreto:

        print("El número es muy bajo. ¡Intenta de nuevo!")

    elif valor_ingresado == numero_secreto:
        bandera = False

print(f"¡Felicidades! Adivinaste el número secreto. {numero_secreto}")
