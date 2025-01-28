# Happy Numbers
# Descripción:
# Un número feliz es un número definido por el siguiente proceso: Comenzando con cualquier entero positivo, reemplaza el número por la suma de los cuadrados de sus dígitos y repite el proceso hasta que el número sea igual a 1 (donde permanecerá) o entre en un ciclo que no incluya 1. Aquellos números para los cuales este proceso termina en 1 son llamados números felices; los demás son considerados números infelices o tristes.
# Objetivo:
# Escribe un programa que determine si un número dado es un número feliz.
# Ejemplo:
# Entrada: 19
# Salida: true


def HappyNumbers(num):
    # code goes here
    result = 0

    while num > 0:
        result += (num % 10) ** 2
        num = num // 10

    if result == 1:
        return "true"
    elif result < 10:
        return "false"
    else:
        return HappyNumbers(result)


# keep this function call here
print(HappyNumbers(int(input())))