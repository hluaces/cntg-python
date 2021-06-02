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

    print(numbers)
    print(tuple(numbers))


if __name__ == "__main__":
    main()
