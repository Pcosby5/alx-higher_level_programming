#!/usr/bin/python3
import sys


def star():
    args = sys.argv[1:]
    len_of_args = len(args)
    if len_of_args == 0:
        print("0 arguments.")
    elif len_of_args == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(len_of_args))
        for argc in range(1, len_of_args + 1):
            print("{}: {}".format(argc, sys.argv[argc]))


if __name__ == "__main__":
    star()
