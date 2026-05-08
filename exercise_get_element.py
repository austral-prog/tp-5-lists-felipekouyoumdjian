# Ejercicio 2: Obtener elemento en posición específica

def get_element(lista, indice):
    if len(lista)==0:
        return None
    
    if indice < 0:
        indice = len(lista) + indice

    if indice < 0 or indice >= len(lista):
        return None

    return lista[indice]
