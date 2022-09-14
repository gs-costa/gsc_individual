import numpy as np

def la_determinant(N):
    nv_linha = ''
    for i in range(0,N):
        nova_linha = input()
        if i != N-1:
            nv_linha = nv_linha + nova_linha + '; '
        else:
            nv_linha = nv_linha + nova_linha
    
    matriz = np.array(np.mat(nv_linha), subok = True)
    #print(nv_linha)

    return round(np.linalg.det(matriz),2)

N = int(input())

print(la_determinant(N))