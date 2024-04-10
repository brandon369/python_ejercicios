numeros = [25, 7, 9, 12, 18, 20, 22, 27, 31, 37, 42, 47]

for numero in numeros:
    if numero == 1:
        continue
    if numero == 2:
        print(numero)
        continue
    if numero % 2 == 0:
        continue
    es_primo = True
    for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(numero)
