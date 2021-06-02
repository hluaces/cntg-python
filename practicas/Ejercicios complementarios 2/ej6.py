#!/usr/bin/env python

def print_biggest_string(str1, str2):
    if len(str1) > len(str2):
        print(str1)
    elif len(str2) > len(str1):
        print(str2)
    else:
        print(str1)
        print(str2)


if __name__ == "__main__":
    tests = (
            ("String mayor!", "String menor"),
            ("String menor 2", "String mayor! 2"),
            ("String igual 3", "String igual 3")
            )

    for test in tests:
        print_biggest_string(*test)
