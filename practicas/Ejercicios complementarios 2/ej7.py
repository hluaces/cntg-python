#!/usr/bin/env

def main(min=1, max=3):
    print(dict([(x, x**2) for x in range(min, max+1)]))


if __name__ == "__main__":
    main()
