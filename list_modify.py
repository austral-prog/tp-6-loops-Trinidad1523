# Replace the "ANSWER HERE" for your answer

def put(value, lst):
    for elemento in lst:
        if "" == elemento:
            lst[lst.index(elemento)] = value
            return lst.index(value)
    return -1
    """
    Coloca value en el primer lugar vacio ("") que encuentre en lst
    y retorna el indice donde lo coloco.
    Si no hay ningun lugar vacio, retorna -1.
    IMPORTANTE: esta funcion modifica la lista original.

    Ejemplo:
        colors = ["Red", "", "Green"]
        put("Blue", colors) -> 1
        # colors ahora es ["Red", "Blue", "Green"]
    """
    return "ANSWER HERE"  # Remove this line and implement

def remove(value, lst):
    delete = 0
    for elem in lst:
        if value == elem:
            lst[lst.index(elem)] = ""
            delete += 1
    return delete

"""
    Busca todas las ocurrencias de value en lst, las reemplaza por ""
    y retorna la cantidad de eliminaciones realizadas.
    IMPORTANTE: esta funcion modifica la lista original.

    Ejemplo:
        colors = ["Red", "Green", "Red", "Blue"]
        remove("Red", colors) -> 2
        # colors ahora es ["", "Green", "", "Blue"]
    """

