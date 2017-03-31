# -*- coding: utf-8 -*-
import string
import random

# Configuração do Grid
def setupgrid(gridsize,start,numberofmines):
    grid = [['0' for i in range(gridsize)] for i in range(gridsize)]
    mines = generatemines(grid,start,numberofmines)
    getnumbers(grid)
    return (grid,mines)

# Mostra o Grid do jogo separados por '-' e ' | ' para mostrar as celulas
def showgrid(grid):
    gridsize = len(grid)
    horizontal = '   '+4*gridsize*'-'+'-'
    # Imprimir letras da coluna superior
    toplabel = '     '
    for i in string.ascii_lowercase[:gridsize]:
        toplabel = toplabel+i+'   '
    print toplabel+'\n'+horizontal
    # Imprimir numeros da linha esquerda
    for idx,i in enumerate(grid):
        row = '{0:2} |'.format(idx+1)
        for j in i:
            row = row+' '+j+' |'
        print row+'\n'+horizontal
    print ''

#Random das celulas
def getrandomcell(grid):
    gridsize = len(grid)
    a = random.randint(0,gridsize-1)
    b = random.randint(0,gridsize-1)
    return (a,b)

#Pegando os vizinhos
def getneighbors(grid,rowno,colno):
    gridsize = len(grid)
    row = grid[rowno]
    column = grid[rowno][colno]

    neighbors = []

    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0: continue
            elif -1<rowno+i<gridsize and -1<colno+j<gridsize:
                neighbors.append((rowno+i,colno+j))
    return neighbors

# Gerador de Minas
def generatemines(grid,start,numberofmines):
    gridsize = len(grid)
    mines = []
    for i in range(numberofmines):
        cell = getrandomcell(grid)
        while cell==(start[0],start[1]) or cell in mines:
            cell = getrandomcell(grid)
        mines.append(cell)

    for i,j in mines: grid[i][j] = 'X'
    return mines

def getnumbers(grid):
    gridsize = len(grid)
    for rowno,row in enumerate(grid):
        for colno,col in enumerate(row):
            if col!='X':
                # Obtém os valores dos vizinhos
                values = [grid[r][c] for r,c in getneighbors(grid,rowno,colno)]

                # Conta quantos são minas
                grid[rowno][colno] = str(values.count('X'))

def showcells(grid,currgrid,rowno,colno):
    # Sair da função se a célula já foi mostrada
    if currgrid[rowno][colno]!=' ':
        return

    # Mostra a celula atual
    currgrid[rowno][colno] = grid[rowno][colno]

    # Obter os vizinhos se a célula estiver vazia
    if grid[rowno][colno] == '0':
        for r,c in getneighbors(grid,rowno,colno):
            # Repetir função para cada vizinho que não tem um sinalizador
            if currgrid[r][c] != 'F':
                showcells(grid,currgrid,r,c)

