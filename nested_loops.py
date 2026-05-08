# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    nueva = []
    for fila in matrix:
        for elemento in fila:
            nueva.append(elemento)
    return nueva

"""
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """


def row_sums(matrix):
    lista = []
    for fila in matrix:
        lista.append(sum(fila))
    return lista
print(row_sums([[1, 2, 3], [4, 5, 6]]))
"""
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """


def col_sums(matrix):
    lista = []
    for col in range(len(matrix[0])):
        total = 0
        for fila in matrix:
            total += fila[col]
        lista.append(total)
    return lista
print(col_sums([[1, 2, 3], [4, 5, 6]]))
"""
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """

