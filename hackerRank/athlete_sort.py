def athlete_sort(arr, k):
    arr.sort(key = lambda i: int(i[k]))
    for i in arr:
        for j in range(len(i)):
            print(i[j], end=' ')
        print('', end= '\n')

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    print('arr:', arr)
    k = int(input())

    athlete_sort(arr, k)