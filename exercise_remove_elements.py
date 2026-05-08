# Ejercicio 4: Remover elementos en posiciones específicas

def remove_elements(lista):
    if len(lista) > 5:
         lista.pop(5)
    if len(lista) > 4:
        del lista[4]
    if len(lista) > 0:
        del lista[0]
    return lista
