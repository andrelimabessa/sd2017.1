import os
import random
import re
import time
from string import ascii_lowercase
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer



def criar_tabuleiro(tamanho_tabuleiro, inicio, qtd_minas):
    tabuleiro_vazio = [['0' for i in range(tamanho_tabuleiro)] for i in range(tamanho_tabuleiro)]

    minas = pega_minas(tabuleiro_vazio, inicio, qtd_minas)

    for i, j in minas:
        tabuleiro_vazio[i][j] = 'X'

    tabuleiro = pega_numeros(tabuleiro_vazio)

    return (tabuleiro, minas)


def mostrar_tabuleiro(tabuleiro):
    tamanho_tabuleiro = len(tabuleiro)

    horizontal = '   ' + (4 * tamanho_tabuleiro * '-') + '-'

    # Mostrar as letras das colunas
    label_colunas = '     '

    for i in ascii_lowercase[:tamanho_tabuleiro]:
        label_colunas = label_colunas + i + '   '

    print(label_colunas + '\n' + horizontal)

    # Mostrar os números das linhas
    for idx, i in enumerate(tabuleiro):
        linha = '{0:2} |'.format(idx + 1)

        for j in i:
            linha = linha + ' ' + j + ' |'

        print(linha + '\n' + horizontal)

    print('')


def pega_celula_aleatoria(tabuleiro):
    tamanho_tabuleiro = len(tabuleiro)

    a = random.randint(0, tamanho_tabuleiro - 1)
    b = random.randint(0, tamanho_tabuleiro - 1)

    return (a, b)


def pega_vizinhos(tabuleiro, num_linha, num_coluna):
    tamanho_tabuleiro = len(tabuleiro)
    vizinhos = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            elif -1 < (num_linha + i) < tamanho_tabuleiro and -1 < (num_coluna + j) < tamanho_tabuleiro:
                vizinhos.append((num_linha + i, num_coluna + j))

    return vizinhos


def pega_minas(tabuleiro, inicio, qtd_minas):
    minas = []
    vizinhos = pega_vizinhos(tabuleiro, *inicio)

    for i in range(qtd_minas):
        celula = pega_celula_aleatoria(tabuleiro)
        while celula == inicio or celula in minas or celula in vizinhos:
            celula = pega_celula_aleatoria(tabuleiro)
        minas.append(celula)

    return minas


def pega_numeros(tabuleiro):
    for num_linha, linha in enumerate(tabuleiro):
        for num_coluna, celula in enumerate(linha):
            if celula != 'X':
                # Pega os valores dos vizinhos
                valor = [tabuleiro[l][c] for l, c in pega_vizinhos(tabuleiro, num_linha, num_coluna)]

                # Contar quantas são minas
                tabuleiro[num_linha][num_coluna] = str(valor.count('X'))

    return tabuleiro


def mostra_celulas(tabuleiro, tabuleiro_atual, num_linha, num_coluna):
    # Sai da função se a célula já apareceu
    if tabuleiro_atual[num_linha][num_coluna] != ' ':
        return

    # Mostra célula atual
    tabuleiro_atual[num_linha][num_coluna] = tabuleiro[num_linha][num_coluna]

    # Pega os vizinhos se a célula estiver vazia
    if tabuleiro[num_linha][num_coluna] == '0':
        for l, c in pega_vizinhos(tabuleiro, num_linha, num_coluna):
            # Repete a função pra cada vizinho que não tem uma bandeira
            if tabuleiro_atual[l][c] != 'F':
                mostra_celulas(tabuleiro, tabuleiro_atual, l, c)


def jogar_novamente():
    escolha = input('Jogar novamente? (s/n): ')

    return escolha.lower() == 's'

    os.system('cls')

def analisar_entrada(string_entrada, tamanho_tabuleiro, mensagem_ajuda):
    celula = ()
    bandeira = False
    mensagem = "Célula inválida. " + mensagem_ajuda

    padrao = r'([a-{}])([0-9]+)(f?)'.format(ascii_lowercase[tamanho_tabuleiro - 1])
    entrada = re.match(padrao, string_entrada)

    if string_entrada == 'ajuda':
        mensagem = mensagem_ajuda

    elif entrada:
        num_linha = int(entrada.group(2)) - 1
        num_coluna = ascii_lowercase.index(entrada.group(1))
        bandeira = bool(entrada.group(3))

        if -1 < num_linha < tamanho_tabuleiro:
            celula = (num_linha, num_coluna)
            mensagem = ''

    return {'celula': celula, 'bandeira': bandeira, 'mensagem': mensagem}


def server():
    serverRPC = SimpleJSONRPCServer(('localhost', 7002))
    serverRPC.register_function(criar_tabuleiro)
    serverRPC.register_function(mostrar_tabuleiro)
    serverRPC.register_function(pega_celula_aleatoria)
    serverRPC.register_function(pega_vizinhos)
    serverRPC.register_function(pega_minas)
    serverRPC.register_function(pega_numeros)
    serverRPC.register_function(mostra_celulas)
    serverRPC.register_function(jogar_novamente)
    serverRPC.register_function(analisar_entrada)
    print("Starting server")
    serverRPC.serve_forever()