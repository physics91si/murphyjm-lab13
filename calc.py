#!/usr/bin/python

# Lab 13
# Physics 91SI
# Spring 2016

import sys

def main():
    """Join command-line arguments and pass them to unitcalc(), then print."""
    calculation = ''.join(sys.argv[1:])
    print(calc(calculation))

def calc(s):
    """Parse a string describing an operation on quantities with units."""
    ops = []
    afterOp = False
    # Iterate over the string from start to finish to find out which operators are contained in the expression. Store them in the ops list.
    # Takes care not to count leading negative signs on numbers as operators as well as passing over decimal points.
    for i in range(0,len(s)):
        if not s[i].isdigit() and not s[i] == '.':
            if i==0 and s[i] == '-':
                continue
            if afterOp and s[i] == '-':
                continue
            ops.append(s[i])
            afterOp = True
        else:
            afterOp = False

    nums = s.split('+ | \* | / | -') # Split the string at the various operators '+', '/', and '*'.
                                     # Doesn't split on the minus sign '-' since it could be part of a negative number
    nums = [float(num) for num in nums]
    result = 0
    for operation in ops:
        if operation=='+':
            result += 
        elif operation=='-':
            pass
        elif operation=='*':
            pass
        elif operation=='/':
            pass


if __name__ == "__main__": main()
