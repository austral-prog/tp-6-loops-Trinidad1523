# Replace the "ANSWER HERE" for your answer

def index_of(target, lst):
    for elemento in lst:
        if target == elemento:
            return lst.index(elemento)
    return -1

"""
    Retorna el indice de la primera ocurrencia de target en lst.
    Si no se encuentra, retorna -1.

    Ejemplo: index_of("Black", ["Red", "Green", "Black"]) -> 2
    """



def index_of_by_index(target, lst, start):
    for ele in range(start, len(lst)):
        if lst[ele] == target:
            return ele
    return -1
    """
    Retorna el indice de la primera ocurrencia de target en lst,
    buscando a partir del indice start (inclusive).
    Si no se encuentra, retorna -1.

    Ejemplo: index_of_by_index("Black", ["Red", "Black", "Green", "Black"], 2) -> 3
    """

def index_of_empty(lst):
    for elemento in lst:
        if "" == elemento:
            return lst.index(elemento)
    return -1
    """
    Retorna el indice del primer string vacio ("") en lst.
    Si no hay ninguno, retorna -1.

    Ejemplo: index_of_empty(["Red", "", "Green"]) -> 1
    """

