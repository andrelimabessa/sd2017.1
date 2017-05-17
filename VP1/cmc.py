# -*- coding: utf-8 -*-
from cms import *

def playagain():
    choice = raw_input('Jogar novamente? (s/n): ')
    return choice.lower() == 's'

def playgame():
    numberofmines = 10
    gridsize = 9

    currgrid = [[' ' for i in range(gridsize)] for i in range(gridsize)]
    showgrid(currgrid)
    grid = []
    flags = []
    helpmessage = "Digite primeiro a coluna depois a linha (ex.: a5).\nPara colocar ou remover uma bandeira, adicxione 'f' para a célula (ex.: a5f)\n"
    print helpmessage

    while True:
        while True:
            lastcell = str(raw_input('Digite a Celula ({} minas deixadas): '.format(numberofmines-len(flags))))
            print '\n\n'
            flag = False
            try:
                if lastcell[2] == 'f': flag = True
            except IndexError: pass

            try:
                if lastcell == 'Ajuda':
                    print helpmessage
                else:
                    lastcell = (int(lastcell[1])-1,string.ascii_lowercase.index(lastcell[0]))
                    break
            except (IndexError,ValueError):
                showgrid(currgrid)
                print "Celula invalida",helpmessage

        if len(grid)==0:
            grid,mines = setupgrid(gridsize,lastcell,numberofmines)
        rowno,colno = lastcell

        if flag:
            # Adiciona uma bandeira se a celula estiver vazia
            if currgrid[rowno][colno]==' ':
                currgrid[rowno][colno] = 'F'
                flags.append((rowno,colno))
            # Remove a bandeira se tiver uma
            elif currgrid[rowno][colno]=='F':
                currgrid[rowno][colno] = ' '
                flags.remove((rowno,colno))
            else: print 'Não pode colocar uma bandeira lá'

        else:
            # Se houver uma bandeira lá, mostre uma mensagem
            if (rowno,colno) in flags:
                print 'Há uma bandeira lá'
            else:
                if grid[rowno][colno] == 'X':
                    print 'Game Over\n'
                    showgrid(grid)
                    if playagain(): playgame()
                    else: exit()
                else:
                    showcells(grid,currgrid,rowno,colno)

        showgrid(currgrid)

        # Se todas o numero de bandeiras forem iguais aos de minas entao vence o jogo
        if set(flags)==set(mines):
            print 'Voce Venceu'
            if playagain(): playgame()
            else: exit()

playgame()