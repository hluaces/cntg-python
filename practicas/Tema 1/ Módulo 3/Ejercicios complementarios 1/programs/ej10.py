#!/usr/bin/env python

def _is_valid_number(number):
    if isinstance(number, int):
        number = str(number)

    for i in range(0, len(number)):
        x = int(number[i])

        if x % 2 != 0:
            return False

    return True


def main():
    sentence = input("Introduce una frase:")
    count = {'LETTERS': 0, 'DIGITS': 0}

    for word in sentence:
        for letter in word:
            if letter.isnumeric():
                count['DIGITS'] += 1
            else:
                count['LETTERS'] += 1

    for item in count.items():
        print(item[0], item[1])


if __name__ == "__main__":
    main()
