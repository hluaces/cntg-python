#!/usr/bin/env python
from random import randrange


def print_border():
    '''
    Imprime el borde superior/inferior de cada fila del tablero
    '''
    print("+-------+-------+-------+")


def get_graphic_for_cell(board, row, column):
    '''
    Devuelve el caracter que representa cada ficha del tablero.

    Devolver un string con el carácter que será usado para imprimir
    la ficha correspondiente a un tablero y su posición.

    Parameters
    ----------
    board : list[list[]]
        La matriz bidimensional que representa el tablero.
    row : int
        El número de la fila de la que queremos conocer la representación (0-2)
    column: int
        El número de la columna de la que queremos conocer la representación
        (0-2)
    '''
    return board[row][column] or ' '


def print_row(board, row):
    '''
    Imprime por pantalla el estado actual de una fila del tablero.

    La función imprimirá la fila, sus casillas con contenido y el borde
    superior, e inferior si corresponde.

    Parameters
    ----------
    board : list[list[]]
        La matriz bidimensional que representa el tablero.
    row : int
        La fila que queremos imprimir por pantalla.
    '''
    print_border()

    print("|       |       |       |")
    print("|   %s   |   %s   |   %s   |" % (
        get_graphic_for_cell(board, row, 0),
        get_graphic_for_cell(board, row, 1),
        get_graphic_for_cell(board, row, 2)
    ))
    print("|       |       |       |")

    if row == 2:
        print_border()


def display_board(board):
    """
    Imprime por pantalla la representación gráfica del estado del tablero.

    Parameters
    ----------
    board : list[list[]]
        La matriz bidimensional que representa el estado del tablero.
    """

    for row in range(0, len(board)):
        print_row(board, row)


def make_list_of_free_fields(board):
    """
    Dado un tablero, devuelve la lista de celdas libres.

    La función tomará el tablero y devolverá una lista de tuplas en formato
    (X, Y), siendo 'X' la fila e 'Y' la columna, con aquellas casillas que
    aún no tienen asignadas una ficha del juego.

    Un ejemplo de la salida podría ser:

        [(0, 1), (1, 2), (2, 0)]

    Parameters
    ----------
    board : list[list[]]
        La matriz bidimensional que representa el estado del tablero.
    """
    free = []

    for row in range(0, len(board)):
        for column in range(0, len(board[0])):
            if board[row][column] == 0:
                free.append((row, column))

    return free


def draw_move(board):
    """
    Función que efectúa el turno de la computadora.

    La computadora elegira una casilla libre al azar y colocará allí su
    movimiento.

    Parameters
    ----------
    board : list[list[]]
        La matriz bidimensional que representa el estado del tablero.
    """
    choices = make_list_of_free_fields(board)
    choice = choices[randrange(0, len(choices))]
    board[choice[0]][choice[1]] = 'X'


def victory_for(board, sign):
    """
    Función que determina si un signo en particular ha ganado la partida.

    La función comprueba que eixsta un \"tres en raya\" en alguna dirección
    para el símbolo dado.

    TODO: refactorizar & optimizar

    Parameters
    ----------
    board: list[list[]]
        La matriz bidimensional que representa el estado del tablero.

    sign: string
        El carácter a comprobar (normalmente 'O' o 'X')
    """

    # Switches de control para saber si hay match en diagonales
    match_right_d = match_left_d = True

    # Auxiliar de la longitud del tablero
    max_len = len(board) - 1

    # Búsqueda de victoria en columnas o diagonales
    for column in range(0, len(board)):
        column_matched = True

        # Búsqueda en columnas
        for row in range(0, len(board)):
            if board[row] == [sign, sign, sign]:
                return True

            column_matched = column_matched and board[row][column] == sign

        # Búsqueda en diagonales
        match_left_d = match_left_d and board[column][column] == sign
        match_right_d = match_right_d and board[max_len-column][column] == sign

        if column_matched:
            return True

    return match_left_d or match_right_d


def get_board_position_for(board, pos):
    """
    Devuelve la tupla con la posición de la matriz que corresponde a un entero.

    Esta función traduce las entradas de enteros 1-10 a las respectivas
    posiciones del tablero que ocupan dichos valores. P.ej.:

        - 1 -> (0, 0)
        - 5 -> (1, 2)
        - 9 -> (2, 2)

    Parameters
    ----------
    board : list[list[]]
        El estado de la matriz bidimensional que representa el tablero.

    pos : int
        El entero de posición (1-10) que queremos traducir a coordenadas de
        tablero.
    """
    current = 0

    for row in range(0, len(board)):
        for column in range(0, len(board)):
            current += 1

            if pos == current:
                return (row, column)

    return None


def enter_move(board):
    """
    Función que acepta el movimiento de un jugador.

    La función tomará como entrada un valor de 1-10 y realizará las
    comprobaciones pertinentes para asegurarse de que no se introduce una
    jugada incorrecta.

    Parameters
    ----------
    board : table[table[]]
        El estado de la matriz bidimensional que representa el tablero.
    """
    x = input("Enter your move:")

    if not x.isnumeric():
        print("El valor introducido no es correcto.")
        return enter_move(board)

    x = int(x)

    if x < 1 or x > 10:
        print("Valor inválido para X, ha de estar entre 0 y 10.")
        return enter_move(board)

    pos = get_board_position_for(board, x)

    if board[pos[0]][pos[1]]:
        print("La posición (%d,%d) está ocupada." % (pos[0], pos[1]))
        return enter_move(board)

    board[pos[0]][pos[1]] = 'O'
    return True


def check_game_status(board):
    """
    Función que comprueba el estado del juego y lo devuelve como una tupla

    La función determinará el estado del juego en este orden:

        1. Comprobará si la computadora ha ganado.
        2. Si no, comprobará si el jugador ha ganado.
        3. Si no, comprobará si hay un empate.
        4. En cualquier otro caso considerará que el juego está 'en progreso'.

    La función devolverá una tupla (Bool, String), siendo el primer valor
    un boolean que representa si el juego ha de interrumpirse (True) o no
    (False).

    El segundo valor es un string que identifica el estado del juego y puede
    ser:

        - "computer victory"
        - "player victory"
        - "draw
        - "in progress"

    Parameters
    ----------
        board : table[table[]]
        El estado de la matriz bidimensional que representa el tablero.
    """
    if victory_for(board, 'X'):
        return (True, 'computer victory')

    if victory_for(board, 'O'):
        return (True, 'player victory')

    if len(make_list_of_free_fields(board)) == 0:
        return (True, 'draw')

    return (False, 'in progress')


def main():
    """
    Función principal del juego.
    """
    # Initialization
    board = [[0 for row in range(0, 3)] for column in range(0, 3)]
    player_turn = randrange(0, 2) == 1
    game_status = (False, None)

    # Initial board
    display_board(board)

    # Main loop
    while not game_status[0]:
        if player_turn:
            enter_move(board)
        else:
            draw_move(board)

        game_status = check_game_status(board)
        player_turn = not player_turn
        display_board(board)

    # End messages
    if game_status[1] == 'player victory':
        print("Has ganado a la computadora. No te extrañe que un " +
              "robot viaje a esta línea temporal desde el futuro " +
              "en aras de destruírte.")
    elif game_status[1] == 'computer victory':
        print("La computadora ha ganado, dando fe de que la dominación " +
              "mundial por parte de las máquinas es un futuro cercano e " +
              "inexorable.")
    else:
        print("La partida ha terminado en empate. La sempiterna pugna " +
              "por la supremacía entre los seres humanos y las máquinas " +
              "todavía no ha terminado.")


if __name__ == "__main__":
    main()
