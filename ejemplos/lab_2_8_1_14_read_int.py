def read_int(prompt, min, max):
    try:
        x = int(input(prompt))

        if x > max or x < min:
            raise OverflowError

        return x
    except ValueError:
        print("Error: wrong input")
    except OverflowError:
        print("The value is not within allowed range %s..%s." % (min, max))

    return read_int(prompt, min, max)


v = read_int("Enter a number from -10 to 10: ", -10, 10)


print("The number is:", v)
