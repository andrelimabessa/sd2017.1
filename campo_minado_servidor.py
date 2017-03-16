import random

def sortearBombas(n,l,c):    
    vetor = []
    for i in range(n): #número de bombas
        i = random.randint(0,l-1) # y -1
        n = random.randint(0,c-1) # x -1
        if ([i,n] not in vetor):
            vetor.append([i,n])
    return vetor 

def bombasAoRedor(l,c,posBombas):
    count = 0
    if ([l+1,c] in posBombas):
        count += 1
    if ([l-1,c] in posBombas):
        count += 1
    if ([l,c-1] in posBombas):
        count += 1
    if ([l-1,c-1] in posBombas):
        count += 1
    if ([l+1,c-1] in posBombas):
        count += 1
    if ([l-1,c+1] in posBombas):
        count += 1
    if ([l+1,c+1] in posBombas):
        count += 1
    if ([l,c+1] in posBombas):
        count += 1
    return count;

def gerarMatriz(l,c):

    matriz = [[" " for x in range(l)] for y in range(c)] # l -> linhas ; c -> colunas
    return matriz

def mostrarMatriz(matriz,l):
    print("")
    for i in range(l):
        print(matriz[i])

