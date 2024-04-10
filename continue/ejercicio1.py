suma_pares = 0

for num in range(1, 101):
    print(num)
    if num % 2 != 0:
        continue
    suma_pares += num

print("La suma de los números pares del 1 al 100 es:", suma_pares)
