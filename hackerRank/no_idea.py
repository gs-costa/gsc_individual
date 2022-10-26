
def happiness(array_ini, arrayA, arrayB):
    happy = 0
    for i in array_ini:
        if i in arrayA:
            happy += 1
        elif i in arrayB:
            happy -=1
    return happy

def f(x, l=[]):
    for i in range(x):
        l.append(i * i)
    print(l)


if __name__ == '__main__':
    n, m = list(map(int,input().split()))
    array_ini = list(map(int,input().split()))

    arrayA = set(map(int,input().split()))
    arrayB = set(map(int,input().split()))
    print(array_ini, arrayA, arrayB)
    print(happiness(array_ini, arrayA, arrayB))

    # y = ['2', '5j', '6']
    # y.insert(2, 'java')
    # #print(y)
    # #print([i.lower() for i in "TURING"])
    # #print('The {0} side {1} {2}'.format('bright', 'of', 'life'))
    # # z = 'abcdef'
    # # i = 'a'
    # # while i in z[:-1]:
    # #     print(i, end=' ')
    # # z.add('san')
    # # z.update(set(['p','q']))
    # #newlist = z.copy()
    # # newlist = list(z)
    # # print(newlist)
    # result = re.findall('Welcome to turing', 'Welcome', 1)
    
    # # print(list(map(lambda y:len(y), y)))
    # a = [1,2,3,4,5]
    # # b = [12,6,2,1]
    # # a.pop()
    # # print(a)
    # # a.pop(2)
    # # print(2**(3**2), (2**3)**2, (2**3)**3)
    # m = map(lambda x: 2**x, a)
    # # print(list(m))
    # array = ['Welcom', 'To', 'Turing']
    # print('-'.join(array))
