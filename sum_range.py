# Replace the "ANSWER HERE" for your answer

def sum_to_n(n):
    if n <= 0:
        return 0
    else:
        for num in range(n+1):
            return sum(range(n+1))
    """
    Retorna la suma de todos los enteros desde 1 hasta n (inclusive).
    Si n <= 0, retorna 0.

    Ejemplo: sum_to_n(5) -> 15  (1+2+3+4+5)
    """

def sum_evens(n):
    if n <= 0:
        return 0
    else:
        for num in range(n+1):
            return sum(range(0, n+1, 2))
    """
    Retorna la suma de todos los numeros pares desde 1 hasta n (inclusive).
    Si n <= 0, retorna 0.

    Ejemplo: sum_evens(10) -> 30  (2+4+6+8+10)
    """
print(sum_evens(-5))

def factorial(n):
    factor = 1
    for num in range(1, n+1):
        factor = factor*num
    return factor


"""
    Retorna el factorial de n (n!).
    Si n <= 0, retorna 1.

    Ejemplo: factorial(5) -> 120  (1*2*3*4*5)
    """

