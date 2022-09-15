from itertools import product

def maximize_it():
    K, M = map(int, '3 100'.split()) #input().split()
    listas_i = []
    for _ in range(K):
        n, lista_i = input().split(' ', 1)
        #print('n:', n,'listas:', end= '')
        lista_i = list(map(int, lista_i.split()))
        #print(lista_i)
        listas_i.append(lista_i)
    produto = list( product(*listas_i))
    print(produto)
    produto2 = []
    for i in produto:
        funcaosoma = 0
        for j in i:
            funcaosoma += j**2 
        produto2.append(funcaosoma % M)
    print(max(produto2))



def __main__():

    maximize_it()

if __name__ == '__main__':
    #letters = 10#input().strip()
    __main__()