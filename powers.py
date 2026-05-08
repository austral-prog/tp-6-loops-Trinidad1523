# Replace the "ANSWER HERE" for your answer

def power(base, exp):
    resultado = 1
    for numero in range(exp):
        resultado *= base
    return resultado
    """
    Retorna base elevado a exp usando un bucle for.
    exp es siempre >= 0.

    Ejemplo: power(2, 3) -> 8  (2*2*2)
    """
def sum_of_powers(base, max_exp):
    res = 0
    for num in range(max_exp+1):
        res += power(base, num)
    return res
print(sum_of_powers(2, 3))
"""
    Retorna la suma de base^0 + base^1 + ... + base^max_exp.
    Debe USAR la funcion power.

    Ejemplo: sum_of_powers(2, 3) -> 15  (1+2+4+8)
    """
