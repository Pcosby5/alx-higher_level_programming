#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator == '+':
        addition = add(a, b)
    elif operator == '-':
        subtraction = sub(a, b)
    elif operator == '*':
        multiplication = mul(a, b)
    elif operator == '/':
        division = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, operator, b, addition))
    print("{} {} {} = {}".format(a, operator, b, subtraction))
    print("{} {} {} = {}".format(a, operator, b, multiplication))
    print("{} {} {} = {}".format(a, operator, b, division))
