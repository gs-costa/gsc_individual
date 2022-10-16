from calendar import weekday, day_name, month_abbr, weekheader
from datetime import datetime
import math
import os
import random
import re
import sys

def dayofweek():
    mes, dia, ano = map(int, input().split())
    diasemana = weekday(ano, mes, dia)
    print(list(day_name)[diasemana].upper())

def modificadatas(t):
    a, d, b, Y, HMS, z = t.split()
    a = int(weekheader(3).split().index(a))
    b = list(month_abbr).index(b)
    d, Y = int(d), int(Y)

    H, M, S = map(int, HMS.split(':'))
    sign, hours, minutes = re.match('([+\-]?)(\d{2})(\d{2})', z).groups()
    sign = -1 if sign == '-' else 1
    thours, tminutes = sign*int(hours), sign*int(minutes)
    offset = thours*3600 + tminutes*60

    return datetime(Y, b, d, H, M, S), offset

# Complete the time_delta function below.
def time_delta(t1, t2):
    t1, offset1 = modificadatas(t1)
    t2,offset2 = modificadatas(t2)
    print(t1)
    print(t2)
    diff = (t1-t2).total_seconds()
    print(diff, offset1, offset2)
    diff = abs(diff - offset1 + offset2)
    
    return diff

if __name__ == '__main__':
    #fptr = open(os.environ['jaja'], 'w')

    t = 1#int(input())

    for t_itr in range(t):
        t1 = 'Sat 02 May 2015 19:54:36 +0530'#input()

        t2 = 'Fri 01 May 2015 13:54:36 -0000'#input()

        delta = str(time_delta(t1, t2))
        print(type(delta))
        #fptr.write(delta + '\n')

    #fptr.close()