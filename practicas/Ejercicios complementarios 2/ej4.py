#!/usr/bin/env python

def sum_numbers_as_string(str1, str2):
    return int(str1) + int(str2)


if __name__ == "__main__":
    tests = (("2","2"), ("3", "2"), ("-1", "1"))

    for test in tests:
        print(test, "=", sum_numbers_as_string(*test))