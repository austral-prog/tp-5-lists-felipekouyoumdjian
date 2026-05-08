# Ejercicio 12: Manipular lista de listas

def list_of_lists(lista_de_listas):
    primera = lista_de_listas[0][:2]
    segunda = lista_de_listas[1][1:4]
    tercera = lista_de_listas[2][-2:]
    return [primera, segunda, tercera]
