from itertools import combinations, combinations_with_replacement, groupby

def combinacoes(letters):
    
    split_va1 = letters.split()
    palavra = split_va1[0]
    nro = int(split_va1[1])
    palavra = list(palavra)
    palavra.sort()
    print(list(combinations(palavra, nro)))
    for k in range(nro):
        combinacao = list(combinations(palavra, k+1))
        for i in combinacao:
            
            for j in range(k+1):
                print(i[j],end='')
            print(end='\n')

def combinacoes_replacement(letters):
    print('Combinações com replacement:')
    split_va1 = letters.split()
    palavra = split_va1[0]
    nro = int(split_va1[1])
    palavra = list(palavra)
    palavra.sort()
    
    combinacao = list(combinations_with_replacement(palavra, nro))
    for i in combinacao: 
        for j in range(nro):
            print(i[j],end='')
        print(end='\n')

def agrupamento(letters):
   
    for k, g in groupby(letters):
        tamanhos = len(list(g))
        print('(' + str(tamanhos) + ', ' + k + ')', end=' ')

def probabilidade(letters):
    ## Output a single line consisting of the probability that at least one of the K indices selected contains the letter:'a'.
    letras = 'a z e i o a f g h k'.split(' ')#input().split(' ')
    indice = 5 #int(input())
    combinacao = list(combinations(letras, indice))
    cont = 0
    ind = 0
    print('letras', letras)
    print('indice', indice)
    for i in combinacao:
        for j in i:
            if j == 'a':
                cont +=1
                # print('ind:', ind, end= ' ')
                # print('j:', j, end= ' ')
                # print('cont', cont)
                break
        ind +=1
    len_combinacao = len(combinacao)
    print(cont, '/', len_combinacao, '= ', end= '')
    prob = cont / len_combinacao
    print(prob)

def __main__(letters):
    #combinacoes(letters)
    #combinacoes_replacement(letters)
    #agrupamento(letters)
    probabilidade(letters)

if __name__ == '__main__':
    letters = 10#input().strip()
    __main__(letters)