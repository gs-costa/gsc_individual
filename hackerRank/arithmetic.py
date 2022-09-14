def arithmetic_func(a,b):
    print(a+b)
    print(a-b)
    print(a*b)

def __main__(a,b):
    arithmetic_func(a,b)

if __name__ == '__main__':
    a = int(input('a:'))
    b = int(input('b:'))

    __main__(a,b)