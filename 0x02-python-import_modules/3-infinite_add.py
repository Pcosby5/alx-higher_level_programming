#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total = 0
    args = sys.argv

    for argc in range(len(args) - 1):
        total += int(args[argc + 1])
    print("{}".format(total))
