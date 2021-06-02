#!/usr/bin/env/python

class AbortInput(BaseException):
    pass


class UnknownDirection(BaseException):
    pass


def __get_movement():
    commands = input("Introduce dirección y distancia o texto en blanco para salir:")
    commands = commands.strip()

    if commands == "":
        raise AbortInput

    commands = commands.split(" ")
    valid_directions = ["UP", "DOWN", "LEFT", "RIGHT"]

    if len(commands) != 2:
        print("Formato incorrecto. Ha de ser una dirección seguido de un " +
              "valor numérico.")
        print("Direcciones válidas: ", valid_directions)
        return __get_movement()

    if commands[0] not in valid_directions:
        print("Dirección inválida '%s'." % commands[0])
        return __get_movement()

    if not commands[1].isnumeric():
        print("El valor '%s' no es un número." % commands[1])
        return __get_movement()

    return (commands[0], int(commands[1]))


def __move_position(current_position, command):
    params = {
        'UP': {'sign':  1, 'position': 1},
        'DOWN': {'sign': -1, 'position': 1},
        'RIGHT': {'sign':  1, 'position': 0},
        'LEFT': {'sign': -1, 'position': 0}
    }

    if command[0] not in params.keys():
        raise UnknownDirection(command[0])

    params = params[command[0]]
    current_position[params['position']] += params['sign'] * command[1]
    return current_position


def __calculate_distance(point_a, point_b):
    return ((point_b[0] - point_a[0])**2 + (point_b[1] - point_a[1])**2) ** 0.5


def main():
    starting_point = [0, 0]
    current_point = starting_point[:]

    try:
        while True:
            command = __get_movement()
            current_point = __move_position(current_point, command)

            print("> Moviéndome %d puntos hacia hacia %s."
                  % (command[1], command[0]))

    except (AbortInput, KeyboardInterrupt):
        pass

    len = __calculate_distance(starting_point, current_point)
    print("")
    print("Distancia recorrida:", int(len))


if __name__ == "__main__":
    main()
