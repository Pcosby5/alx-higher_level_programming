#!/usr/bin/python3
def uppercase(str):
    for lower_case in str:
        if ord(lower_case) > 96 and ord(lower_case) < 123: #check for lowercase using ASCII
            lower_case = chr(ord(lower_case) - 32) #converts lowercase to uppercase
        print("{}".format(lower_case), end="")
    print("")
