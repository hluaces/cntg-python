#!/usr/bin/env

def main(min=1, max=3):
    ret = dict([(x, x**2) for x in range(1, 21)])

    for _, val in ret.items():
        print(val)


if __name__ == "__main__":
    main()
