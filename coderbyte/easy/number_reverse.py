# Number Reverse
# Desafío: Invertir Números en una Cadena
# Escribe una función llamada NumberReverse(strParam) que tome como argumento una cadena de texto strParam que contenga números separados por espacios. La función debe devolver una nueva cadena con los números en el orden inverso.
# Entrada: "1 2 3 4"
# Salida: "4 3 2 1"
# Entrada: "10 20 30"
# Salida: "30 20 10"

def NumberReverse(strParam):
    # code goes here
    return " ".join(reversed(strParam.split(" ")))


# keep this function call here
print(NumberReverse((input())))
