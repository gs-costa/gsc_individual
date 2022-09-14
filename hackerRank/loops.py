def square(number):
    number_list = range(1,number+1)

    for i in number_list:
        print(i, end='')
        #print(i**2)

def __main__(number):
    square(number)

if __name__ == '__main__':
    n = int(input().strip())
    __main__(n)