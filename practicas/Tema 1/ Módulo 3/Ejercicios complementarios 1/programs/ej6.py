#!/usr/bin/env python

def _get_input():
    words = []

    while len(words) == 0:
        x = input("Imprime una lista de palabras separadas por comas: ")
        y = [x.strip() for x in x.split(',')]

        if len(y) == 1 and y[0] == '':
            print("Entrada inválida.")
            continue

        words = y

    return words


def main():
    words = _get_input()
    words.sort()
    print(words)


if __name__ == "__main__":
    main()
