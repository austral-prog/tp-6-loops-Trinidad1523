# ---- Funciones provistas (NO modificar) ----

def find_min(numbers):
    """Dada una lista de numeros, retorna el menor valor."""
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


def find_max(numbers):
    """Dada una lista de numeros, retorna el mayor valor."""
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

def range_of(numbers):
    return find_max(numbers) - find_min(numbers)

def average(numbers):
    if len(numbers) == 0:
        avg = 0.0
    else:
        total = 0
        for number in numbers:
            total += number
        avg = round(total / len(numbers), 1)
    return avg

def describe(numbers):
    if len(numbers) == 0:
        description = "Empty list"
    else:
        description = (
            "Min:" + str(find_min(numbers)) +
            " Max:" + str(find_max(numbers)) +
            " Range:" + str(range_of(numbers)) +
            " Avg:" + str(average(numbers))
        )
    return description

