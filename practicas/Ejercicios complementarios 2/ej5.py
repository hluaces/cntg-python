#!/usr/bin/env python

def concatenate_strings(str1, str2):
    print(str1, str2)


if __name__ == "__main__":
    tests = (("2", "2"), ("3", "2"), ("-1", "1"))

    for test in tests:
        print(test, "= ", end="")
        concatenate_strings(*test)
