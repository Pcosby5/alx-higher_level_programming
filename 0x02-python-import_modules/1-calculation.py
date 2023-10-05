#!/usr/bin/python3
# import function from python file

from calculator_1 import add, sub, mul, div
# does not execute upon importing

if __name__ == "__main__":
    a = 10
    b = 5

    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b

    print("{} + {} = {}".format(a, b, addition))

    print("{} - {} = {}".format(a, b, subtraction))

    print("{} * {} = {}".format(a, b, multiplication))

    print("{} / {} = {}".format(a, b, division))
