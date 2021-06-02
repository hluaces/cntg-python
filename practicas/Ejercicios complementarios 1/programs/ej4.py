#!/usr/bin/env python

def _get_input():
    while True:
        list_ok = True
        x = input("Input a comma-separated list of numbers: ")
        numbers = []

        for number in x.split(","):
            if not number.isnumeric():
                print("'" + str(number) + "'", "is not a valid value.")
                list_ok = False
                break

            numbers.append(int(number))

        if list_ok:
            return numbers


def main():
    numbers = _get_input()
    C = 50
    H = 30

    print([int(((2*C*D)/H)**0.5) for D in numbers])


if __name__ == "__main__":
    main()
