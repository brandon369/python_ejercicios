def search_element(lista, elemento):
    if elemento in lista:
        print("Elemento encontrado")
    else:
        print("Elemento no encontrado")

# Ejemplo de uso
my_list = [1, 2, 3, 4, 5]
element_to_search = 3
search_element(my_list, element_to_search)

element_to_search = 6
search_element(my_list, element_to_search)