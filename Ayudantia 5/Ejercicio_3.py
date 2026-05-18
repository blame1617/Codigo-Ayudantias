edificio = [
    ["Ana", "Vacío"],    # Piso 0: sala 0, sala 1
    ["Vacío", "Pedro"],  # Piso 1: sala 0, sala 1
    ["Luis", "Vacío"]    # Piso 2: sala 0, sala 1
]

# 1. Ingreso de María (Piso 1, sala 0)
edificio[1][0] = "María"

# 2. Alta de Luis (Luis estaba en el Piso 2, sala 0)
edificio[2][0] = "Vacío"

# 3. Reporte del Piso 0
print("Estado final del Piso 0:", edificio[0])
