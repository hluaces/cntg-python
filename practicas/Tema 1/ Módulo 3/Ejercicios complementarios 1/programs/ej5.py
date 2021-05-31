#!/usr/bin/env python

def _get_input():
    numbers = []

    while len(numbers) != 2:
        x = input("Introduce un número entero:")

        if not x.isnumeric():
            print("Numero erróneo.")
            continue

        numbers.append(int(x))

    return numbers


def main():
    numbers = _get_input()
    matrix = [[x for x in range(0, numbers[1])] for y in range(0, numbers[0])]

    for i in range(0, numbers[0]):
        for j in range(0, numbers[1]):
            matrix[i][j] = i*j

    for i in range(0, len(matrix)):
        print(matrix[i])


if __name__ == "__main__":
    main()
