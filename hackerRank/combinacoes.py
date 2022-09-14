from itertools import combinations, combinations_with_replacement, groupby

def combinacoes(letters):
    
    split_va1 = letters.split()
    palavra = split_va1[0]
    nro = int(split_va1[1])
    palavra = list(palavra)
    palavra.sort()
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
    
def __main__(letters):
    #combinacoes(letters)
    #combinacoes_replacement(letters)
    agrupamento(letters)

if __name__ == '__main__':
    letters = '11223344445'#input().strip()
    __main__(letters)