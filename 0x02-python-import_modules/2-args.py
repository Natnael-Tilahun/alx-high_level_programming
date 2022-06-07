#!/usr/bin/python3
import sys
if len(sys.argv) == 0:
    print("0 arguments.")
else:
    print("{} argument:".format(len(sys.argv)))
    for index in range(len(sys.argv)):
        print("{}: {}:".format(index, sys.argv[index]))
