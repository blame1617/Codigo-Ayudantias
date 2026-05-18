### Análisis de pacientes ###
edadPacientes = [18, 23, 67, 48, 21, 52]
fumaPacientes = [1, 0, 1, 1, 1, 0]

juventud = []
adultez = []
personaMayor = []

for i in range(len(edadPacientes)):

    if edadPacientes[i] >= 60:

        personaMayor.append(fumaPacientes[i])

    elif edadPacientes[i] >= 27:

        adultez.append(fumaPacientes[i])

    else:

        juventud.append(fumaPacientes[i])

print("Juventud: ", (sum(juventud)/len(juventud))*100, "%",
      sum(juventud), "de los", len(juventud), "jovenes fuman")
