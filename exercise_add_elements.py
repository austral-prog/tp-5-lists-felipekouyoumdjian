# Ejercicio 3: Agregar elementos al principio y final

def add_elements(lista):
    return lista.insert(0, "Pink") + lista + lista.append("Yellow")

