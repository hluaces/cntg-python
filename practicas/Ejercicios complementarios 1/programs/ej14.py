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
    numbers_squared = [x**2 for x in numbers if x % 2 != 0]

    print(numbers, numbers_squared)

    for number in numbers_squared:
        if number == numbers_squared[0]:
            print(number, end="")
        else:
            print("," + str(number), end="")

    print("")


if __name__ == "__main__":
    main()
