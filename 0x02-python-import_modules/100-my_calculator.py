#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == '+':
        addition = add(a, b)
        print("{} + {} = {}".format(a, b, addition))
    elif argv[2] == '-':
        subtraction = sub(a, b)
        print("{} - {} = {}".format(a, b, subtraction))
    elif argv[2] == '*':
        multiplication = mul(a, b)
        print("{} * {} = {}".format(a, b, multiplication))
    elif argv[2] == '/':
        division = div(a, b)
        print("{} / {} = {}".format(a, b, division))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)