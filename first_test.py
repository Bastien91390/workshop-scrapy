import sys
import math

def calc():
    x = 0
    while (x <= 100):
        if (x % 3 == 0 and x % 5 != 0):
            print("Three")
        elif (x % 3 != 0 and x % 5 == 0):
            print("Five")
        elif (x % 3 == 0 and x % 5 == 0):
            print("ThreeFive")
        elif (x % 3 != 0 and x % 5 != 0):
            print(x)
        x = x + 1

def main():
    calc()
main()