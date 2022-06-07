#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    i = len(sys.argv) - 1
    opr = sys.argv[2]
    a = sys.argv[1]
    b = sys.argv[3]
    if i < 3:
        print("Usage: {} {} {} {}".format(sys.argv[0], a, opr, b))
        sys.exit(1)
    elif opr != '+' or opr != '-' or opr != '*' or opr != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        if opr == '+':
            print("{} {} {} = {}".format(a, opr, b, add(a, b)))
        elif opr == '-':
            print("{} {} {} = {}".format(a, opr, b, sub(a, b)))
        elif opr == '*':
            print("{} {} {} = {}".format(a, opr, b, mul(a, b)))
        else:
            print("{} {} {} = {}".format(a, opr, b, div(a, b)))
