import os
import random
import re
import time
from string import ascii_lowercase
from jsonrpclib import Server

proxy = Server('http://localhost:7002')


def jogar():

    os.system('cls')
    
    print('_______________________________________')
    print('Bem-vindo(a) ao Campo Minado em Python!')
    print('_______________________________________\n')

    tamanho_tabuleiro = eval(input('Escolha o tamanho do tabuleiro (Mínimo: 4(4x4) - Máximo: 10(10x10)): '))
    '''tamanho_tabuleiro = 9'''
    qtd_minas = eval(input('Escolha a quantidade de minas (Mínimo: 1 - Máximo: Total de posições do tabuleiro - 1): '))
    '''qtd_minas = 10'''

    os.system('cls')

    tabuleiro_atual = [[' ' for i in range(tamanho_tabuleiro)] for i in range(tamanho_tabuleiro)]

    tabuleiro = []
    bandeiras = []
    tempo_inicio = 0

    mensagem_ajuda = ("Digite a coluna seguida da linha (exemplo: a3). \n" "Para colocar ou remover uma bandeira, digite 'F' após a célula (exemplo: a3f).\n")

    proxy.mostrar_tabuleiro(tabuleiro_atual)
    print(mensagem_ajuda + "Digite 'ajuda' para mostrar essa mensagem novamente.\n")

    while True:
        minas_restantes = qtd_minas - len(bandeiras)
        jogada = input('Escolha a próxima célula ({} mina(s) restante(s)): '.format(minas_restantes))
        resultado = proxy.analisar_entrada(jogada, tamanho_tabuleiro, mensagem_ajuda + '\n')

        mensagem = resultado['mensagem']
        celula = resultado['celula']

        os.system('cls')

        if celula:
            # print('\n\n')
            num_linha, num_coluna = celula
            celula_atual = tabuleiro_atual[num_linha][num_coluna]
            bandeira = resultado['bandeira']

            if not tabuleiro:
                tabuleiro, minas = proxy.criar_tabuleiro(tamanho_tabuleiro, celula, qtd_minas)
            if not tempo_inicio:
                tempo_inicio = time.time()

            if bandeira:
                # Coloca um bandeira se a célula estiver vazia
                if celula_atual == ' ':
                    tabuleiro_atual[num_linha][num_coluna] = 'F'
                    bandeiras.append(celula)
                # Remove a bandeira se já tiver uma 
                elif celula_atual == 'F':
                    tabuleiro_atual[num_linha][num_coluna] = ' '
                    bandeiras.remove(celula)
                else:
                    mensagem = 'Impossível colocar uma bandeira aqui.'

            # Se já existir uma bandeira, mostrar uma mensagem
            elif celula in bandeiras:
                mensagem = 'Já existe uma bandeira aqui.'

            elif tabuleiro[num_linha][num_coluna] == 'X':

                print('Você perdeu! :(\n')
                proxy.mostrar_tabuleiro(tabuleiro)
                if proxy.jogar_novamente():
                    jogar()
                return

            elif celula_atual == ' ':
                proxy.mostra_celulas(tabuleiro, tabuleiro_atual, num_linha, num_coluna)

            else:
                mensagem = "Esta célula já foi liberada."

            if set(bandeiras) == set(minas):
                minutos, segundos = divmod(int(time.time() - tempo_inicio), 60)
                print(
                    'Você venceu! :D\n'
                    'Esta partida demorou {} minutos e {} segundos para ser finalizada!\n'.format(minutos, segundos))
                proxy.mostrar_tabuleiro(tabuleiro)
                if jogar_novamente():
                    jogar()
                return

        os.system('cls')
        proxy.mostrar_tabuleiro(tabuleiro_atual)
        print(mensagem)

jogar()