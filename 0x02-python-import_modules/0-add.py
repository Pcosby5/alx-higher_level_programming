#!/usr/bin/python3
a = 1
b = 2
if __name__ == "__main__":
    from add_0 import add
outcome = add(a, b)
print("{:d} + {:d} = {:d}".format(a, b, outcome))
