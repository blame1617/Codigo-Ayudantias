### Código con errores ###
edad = int(input("Ingrese su edad: "))
alergias = input("¿Tiene alergias? (si/no): ")
autorizacion = input("¿Tiene autorización médica? (si/no): ")

# Evaluación del tratamiento
if edad > 18 and edad < 40 or alergias == "si" and autorizacion == "no":
    print("Paciente APTO para el tratamiento.")
else:
    print("Paciente NO APTO.")


### Código corregido ###
edad = int(input("Ingrese su edad: "))
alergias = input("¿Tiene alergias? (si/no): ")
autorizacion = input("¿Tiene autorización médica? (si/no): ")

# Solución con lógica correcta y paréntesis, que si bien en este ejercicio no influye
# puede impactar en la lógica del programa, ya que el and se lee primero que el or en python
if (edad >= 18 and edad <= 40 and alergias == "no") or (autorizacion == "si"):
    print("Paciente APTO para el tratamiento.")
else:
    print("Paciente NO APTO.")
