# Power Set Count
# Descripción:
# El conjunto de potencias de un conjunto es el conjunto de todos los subconjuntos posibles, incluyendo el conjunto vacío y el propio conjunto. Por ejemplo, el conjunto de potencias de {1, 2} es {{}, {1}, {2}, {1, 2}}.
# Objetivo:
# Escribe una función que reciba un conjunto de elementos y devuelva la cantidad total de subconjuntos que se pueden formar a partir de ese conjunto.
# Ejemplo:
# Entrada: [1, 2, 3]
# Salida: 8


from itertools import chain, combinations

def PowerSetCount(arr):

    # code goes here
    try:
        power_set = list(
            chain(*map(lambda x: combinations(arr, x), range(0, len(arr) + 1)))
        )
        return len(power_set)
    except (AttributeError, TypeError):
        return -1


# keep this function call here
print(PowerSetCount([1, 2, 3]))  # 8
print(PowerSetCount([1, 2, 3, 4]))  # 16

