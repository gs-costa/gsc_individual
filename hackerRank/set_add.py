def arithmetic_func(a,b):
    print(a+b)
    print(a-b)
    print(a*b)

def __main__(stamps):
    print(len(stamps))

if __name__ == '__main__':
    N = int(input())
    stamps = set()
    for _ in range(N):
        country = str(input())
        stamps.add(country)

    __main__(stamps)