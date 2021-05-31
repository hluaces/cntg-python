#!/usr/bin/env python

def main():
    numbers = range(2000, 3201)
    first = True
    list = []

    for number in numbers:
        if number %7 != 0 or number %5 == 0:
            continue

        if first:
            print(number, end="")
            first=False
        else:
            print(",", number, end="", sep="")

    print("")

if __name__ == "__main__":
    main()
