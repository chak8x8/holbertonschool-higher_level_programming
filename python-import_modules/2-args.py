#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv) - 1

    if n == 0:
        print("{} arguments.", n)
    elif n == 1:
        print("{} argument:", n)
    else:
        print("{} arguments:", n)

    for i in range(1, n):
        print("{}: {}".format(i, sys.argv[i]), end = "\n")
