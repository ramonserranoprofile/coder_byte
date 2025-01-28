# Knight Jumps
# Description:
#     Have the function KnightJumps(str) read str which will be a string representation of the position of a knight on a chess board. The board will be a standard 8x8 alpha space and will be in the format of "([a-h][1-8])" which represents the position of the knight with x and y coordinates. Your function should determine how many spaces the knight can jump to from its current position on the board and return the number of spaces as an integer. For example: if str is "(d4)" then your program should output 8 because the knight can jump to 8 different spaces from position d4.
#     The knight is not blocked and can jump to any space on the board.
# Examples
#     Input: "(d4)"
#     Output: 8
#     Input: "(a1)"
#     Output: 2

# Tags
# chess chessboard game knight math string string manipulation


def KnightJumps(strParam):
    # Obtener las coordenadas del caballo
    column = ord(strParam[1]) - ord("a") + 1  # Convertir 'a'-'h' a 1-8
    row = int(strParam[2])  # Convertir '1'-'8' a entero

    # Posibles movimientos del caballo
    possible_moves = [
        (column - 2, row + 1),
        (column - 2, row - 1),
        (column + 2, row + 1),
        (column + 2, row - 1),
        (column - 1, row + 2),
        (column - 1, row - 2),
        (column + 1, row + 2),
        (column + 1, row - 2),
    ]

    result = 0
    # Contar movimientos válidos
    for move in possible_moves:
        if 1 <= move[0] <= 8 and 1 <= move[1] <= 8:
            result += 1

    return result  # Retornar un entero


# keep this function call here
print(KnightJumps("(d4)"))  # Output: 8
