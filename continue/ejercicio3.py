numeros = [25, 6, 9, 12, 18, 20, 22, 27]
for numero in numeros:
    if numero % 3 != 0:
        continue
    primer_divisible_por_3 = numero
    print("El primer número divisible por 3 es:", primer_divisible_por_3)
    break


