nombres = ["Ana", "Juan", "Alberto", "María", "Pedro", "Adriana"]

for nombre in nombres:
    if nombre[0].upper() != 'A':
        continue
    print(nombre)
