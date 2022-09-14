import math
import os
import random
import re
import sys

def weird_notweird(number):
    n = number % 2
    if n != 0:
        print('Weird')
    elif number >=2 and number <=5:
        print('Not Weird')
    elif number >=6 and number <=20:
        print('Weird')
    else:
        print('Not Weird')


def __main__(number):
    weird_notweird(number)

if __name__ == '__main__':
    n = int(input().strip())
    __main__(n)
