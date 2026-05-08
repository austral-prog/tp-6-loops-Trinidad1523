# Replace the "ANSWER HERE" for your answer

def countdown(n):
    numero = n
    lista = []
    while numero >= 0:
            lista.append(numero)
            numero -= 1
    return lista

"""
    Retorna una lista con la cuenta regresiva desde n hasta 0.
    Si n < 0, retorna una lista vacia.

    Ejemplo: countdown(5) -> [5, 4, 3, 2, 1, 0]
    Ejemplo: countdown(0) -> [0]
    Ejemplo: countdown(-1) -> []
    """


def double_until(limit):
    num = 1
    lista = []
    while num <= limit:
        if limit < 1:
            return lista
        else:
            lista.append(num)
            num *= 2
    return lista

"""
    Comenzando desde 1, va duplicando el valor y agrega cada uno
    a una lista mientras sea menor o igual a limit.
    Si limit < 1, retorna una lista vacia.

    Ejemplo: double_until(10) -> [1, 2, 4, 8]
    Ejemplo: double_until(1) -> [1]
    Ejemplo: double_until(0) -> []
    """

