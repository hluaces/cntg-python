#!/usr/bin/env python

def __is_binary(str):
    for i in range(0, len(str)):
        if str[i] not in ["0", "1"]:
            return False

    return True


def _get_input():
    numbers = []

    while len(numbers) != 4:
        x = input("Introduce un número binario de 4 dígitos: ")

        if len(x) != 4:
            print("Longitud inválida.")
            continue

        if not __is_binary(x):
            print("No es un número binario válido.")
            continue

        numbers.append(x)

    return numbers


def main():
    numbers = _get_input()
    found = False

    for number in numbers:
        base10 = int(number, 2)

        if base10 % 5 == 0:
            print(number + " (en decimal: " + str(base10) + ")")
            found = True

    if not found:
        print("Ninguno de los números binarios es divisible por 5.")


if __name__ == "__main__":
    main()
