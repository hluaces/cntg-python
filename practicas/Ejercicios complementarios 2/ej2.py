#!/usr/bin/env


def square_root(number):
    return number ** 0.5


if __name__ == "__main__":
    for i in range(0, 40, 2):
        sqrt = square_root(i)
        print("La raíz cuadrada de %2d es: %.2f" % (i, sqrt))
