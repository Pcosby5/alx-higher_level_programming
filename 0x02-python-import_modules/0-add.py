#!/usr/bin/python3
# Assign values to variables
a = 1
b = 2
if __name__ == "__main__":
    #import function from python file
    from add_0 import add
#calc the outcome
outcome = add(a, b)
#print the outcome
print("{:d} + {:d} = {:d}".format(a, b, outcome))
