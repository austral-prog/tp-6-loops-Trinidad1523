# Replace the "ANSWER HERE" for your answer

def enumerate_list(lst):
    nueva = []
    indice = 0
    for elemento in lst:
        if elemento != "":
            nueva.append(f"{indice}. {elemento}")
            indice += 1
    return nueva

    """
    Dada una lista de strings, retorna una nueva lista donde cada elemento
    tiene el formato "indice. valor". Los strings vacios se deben saltear
    y no deben aparecer en la lista resultante.
    El indice debe ser consecutivo (no el indice original).

    Ejemplo: enumerate_list(["Red", "Green", "", "White"]) -> ["0. Red", "1. Green", "2. White"]
    """

def enumerate_backwards(lst):
    lista = []
    indice = 0
    for ele in lst:
        if ele != "":
            lista.append(f"{indice}. {ele[::-1]}")
            indice += 1
    return lista
    """
    Igual que enumerate_list, pero cada palabra debe estar escrita al reves.
    Los strings vacios se deben saltear.

    Ejemplo: enumerate_backwards(["Red", "Green", ""]) -> ["0. deR", "1. neerG"]
    """