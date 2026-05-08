# Ejercicio 11: Comparar tercer elemento de dos listas

def check_lists(lista1, lista2):
    if len(lista1) < 3 or len(lista2) < 3:
        return False
    return lista1[2] == lista2[2]
