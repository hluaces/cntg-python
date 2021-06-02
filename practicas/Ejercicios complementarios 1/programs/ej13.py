#!/usr/bin/env python

def _get_number():
    while True:
        x = input("Introduce un número: ")

        if not x.isnumeric():
            continue

        return int(x)


def main():
    number = _get_number()
    total = 0

    for i in range(1, 5):
        total = total + number ** i

    print(total)


if __name__ == "__main__":
    main()
