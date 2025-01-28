# Simple Evens
# Descripción:
# Escribe una función que determine si todos los dígitos de un número dado son números pares. La función debe devolver true si todos los dígitos son pares y false si al menos uno de los dígitos es impar.
# La función debe manejar excepciones para entradas no válidas, devolviendo -1 en caso de error. Los dígitos se deben evaluar individualmente.
# Ejemplo:
# Entrada: 2468
# Salida: true (todos los dígitos son pares)
# Entrada: 1234
# Salida: false (el dígito 1 es impar)
# Entrada: 0
# Salida: true (el dígito 0 es par)

def SimpleEvens(num):
    # code goes here
    try:
        string_num = str(num)
        return "true" if all(int(char) % 2 == 0 for char in string_num) else "false"

    except ValueError:
        return -1


# keep this function call here
print(SimpleEvens(int(input())))
