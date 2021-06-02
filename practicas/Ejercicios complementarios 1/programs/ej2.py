#!/usr/bin/env python

def _get_number():
    while True:
        x = input("Introduce un número: ")

        if not x.isnumeric():
            continue

        return int(x)


def main():
    x = _get_number()
    ret = {}

    for i in range(1, x+1):
        ret[i] = i*i

    print(ret)


if __name__ == "__main__":
    main()
