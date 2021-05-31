#!/usr/bin/env python

def _get_input():
    words = []

    while len(words) == 0:
        x = input("Imprime una lista de palabras separadas por espacios: ")
        y = [x.strip() for x in x.split(' ')]

        if len(y) == 1 and y[0] == '':
            print("Entrada inválida.")
            continue

        words = y

    return words


def main():
    words = list(set(_get_input()))
    words.sort()

    for word in words:
        if word == words[0]:
            print(word, end="")
        else:
            print(" " + word, end="")

    print("")


if __name__ == "__main__":
    main()
