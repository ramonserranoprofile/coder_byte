# Link: https://www.coderbyte.com/editor/Missing%20Digit:Python3
# Description:
#   Have the function MissingDigit(str) take the str parameter, which will be a simple mathematical formula with three numbers, a single operator (+, -, *, or /) and an equal sign (=) and return the digit that completes the equation. In one of the numbers in the equation, there will be an "x", and your program should determine what digit is missing. For example, if str is "3x + 12 = 46" then your program should output 4. The x character can appear in any of the three numbers and all three numbers will be greater than or equal to 0 and less than or equal to 100.
# Examples
#   Input: "4 - 2 = x"
#   Output: 2
#   Input: "1x0 * 12 = 1200"
#   Output: 0
# Tags:
#   Math Fundamentals, String Manipulation

def missing_digit(strParam):
    # Divide la ecuación en el lado izquierdo y el resultado
    left, result = strParam.split(" = ")

    # Verifica si el resultado contiene "?" y lo convierte en None
    if "?" in result:
        result = None
    else:
        result = int(result)

    # Define los operadores y encuentra cuál está en el lado izquierdo
    operators = ["+", "-", "*", "/"]
    operator = None
    for op in operators:
        if op in left:
            operator = op
            operand1, operand2 = left.split(f" {op} ")
            break

    # Define una función para realizar el cálculo según el operador
    def calculate(a, b, op):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            if b == 0:
                return None
            return a / b
        return None

    # Itera a través de los dígitos del 0 al 9 para encontrar el dígito faltante
    for i in range(10):  # Revisamos todos los dígitos posibles (0-9)
        # Reemplaza "?" con el dígito actual
        replaced_operand1 = operand1.replace("?", str(i))
        replaced_operand2 = operand2.replace("?", str(i))

        try:
            # Convertimos los operandos solo si tienen "?"
            num1 = int(replaced_operand1) if "?" in operand1 else int(operand1)
            num2 = int(replaced_operand2) if "?" in operand2 else int(operand2)

            # Si el resultado contiene "?", lo calculamos para igualar al dígito faltante
            if result is None:
                if operator == "*":
                    # En el caso de multiplicación, comprobar que el valor de num1 * num2 sea el resultado esperado
                    if calculate(num1, num2, operator) == result:
                        return (
                            num2  # Devolvemos el número faltante en la multiplicación
                        )
                else:
                    if calculate(num1, num2, operator) == i:
                        return i
            # Si el resultado es un número, verificamos si el cálculo coincide
            elif calculate(num1, num2, operator) == result:
                return i
        except ValueError:
            continue  # Ignorar valores no válidos

    return None  # Si no se encuentra solución, devuelve None


# Casos de prueba
print(missing_digit("1? + 3 = 17"))  # Salida: 4
print(missing_digit("12 - ? = 5"))  # Salida: 7
print(missing_digit("42 * ? = 84"))  # Salida: 2
print(missing_digit("6 / ? = 3"))  # Salida: 2
print(missing_digit("3? + 1 = 14"))  # Salida: None
print(missing_digit("2 - ? = 0"))  # Salida: 2
print(missing_digit("10 * ? = 90"))  # Salida: 9
print(missing_digit("10 / ? = 2"))  # Salida: 5
print(missing_digit("10 / 0 = ?"))  # Salida: None
