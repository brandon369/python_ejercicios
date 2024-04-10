texto = "Este es un ejemplo de texto para contar vocales"
vocales = 'aeiouAEIOU'
contador = 0

for caracter in texto:
    if caracter not in vocales:
        continue
    contador += 1

print("Número total de vocales en el texto:", contador)
