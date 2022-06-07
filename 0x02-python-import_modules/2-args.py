#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1
    if i == 0:
        print("0 arguments.")
    elif i == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    elif i > 1:
        print("{} arguments:".format(i))
        for index in range(1, len(sys.argv)):
            print("{}: {}".format(index, sys.argv[index]))
