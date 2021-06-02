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
    ret = []

    for number in range(1000, 3001):
        if not _is_valid_number(number):
            continue

        ret.append(str(number))

    print(",".join(ret))


if __name__ == "__main__":
    main()
