# Ejercicio 2: Obtener elemento en posición específica

def get_element(lista, indice):
    largo = len(lista)
    if largo == indice:
        return largo
    else:
        return "None"
get_element([10, 20, 30], 1)