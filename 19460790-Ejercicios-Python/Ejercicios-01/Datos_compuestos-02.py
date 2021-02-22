
n = int(input("Cuantas asignaturas desea capturar en lista? "))
asignaturas = []
i = 0
while i < n:
    asignaturas.append(input("Ingrese el nombre de la asignatura: "))
    i += 1

print(f"La lista de asignaturas es: {asignaturas} ")
