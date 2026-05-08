# Replace the "ANSWER HERE" for your answer

def collatz_steps(n):
    numero = n
    pasos = 0
    while numero != 1:
        if numero == 1:
            pasos = 0
        elif numero % 2 == 0:
            numero = numero // 2
            pasos += 1
        else:
            numero = 3 * numero + 1
            pasos += 1
    return pasos

"""
    Retorna la cantidad de pasos necesarios para llegar a 1
    siguiendo la conjetura de Collatz:
      - Si n es par: n = n // 2
      - Si n es impar: n = 3 * n + 1

    n debe ser >= 1. Si n es 1, retorna 0 (ya esta en 1).

    Ejemplo: collatz_steps(6) -> 8
      6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1  (8 pasos)
    """



def collatz_sequence(n):
    numero = n
    lista = [numero]
    while numero != 1:
        if numero == 1:
            lista = [1]
        elif numero % 2 == 0:
            numero = numero // 2
            lista.append(numero)
        else:
            numero = 3 * numero + 1
            lista.append(numero)
    return lista
print(collatz_sequence(6))
"""
    Retorna la secuencia completa de Collatz como una lista,
    comenzando desde n y terminando en 1.

    n debe ser >= 1. Si n es 1, retorna [1].

    Ejemplo: collatz_sequence(6) -> [6, 3, 10, 5, 16, 8, 4, 2, 1]
    """

