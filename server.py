# -*- coding: utf-8 -*-
import random
import socket

import sys

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000  # Porta que o Servidor esta
HOST = ''  # Endereco IP do Servidor


def server():
    # Abrindo um socket UDP na porta 5000
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ('Socket created')

    # Bind socket to local host and port
    try:
        sock.bind(orig)
    except socket.error:
        print ('Bind failed')
        sys.exit()
    print ('Socket bind complete')
    sock.listen(5)

    while True:
        sock.accept()
        # recebi dados
        data, address = sock.recvfrom(MAX_BYTES)  # Recebi dados do socket
        text = data.decode(ENCODE)  # Convertendo dados de BASE64 para UTF-8
        print(address, text)

        # # Envia resposta
        # text = "Total de dados recebidos: " + str(len(data))
        # data = text.encode(ENCODE)  # Codifica para BASE64 os dados
        # sock.sendto(data, address)  # Enviando dados
        put_bombs(data.bombs, data.rows, data.column)
        bombs_around(data.rows, data.columns, data.bombs)
        make_board(data.rows, data.columns)
        show_board(data.board, data.rows)

        # Fechando Socket
    sock.close()


def put_bombs(bombs, row, column):
    while bombs > (row * column):
        print ('A quantidade de bombas não pode ser superior ao total de espaços.')
        bombs = int(input("Digite a quantidade de bombas: "))
        return bombs

    array_of_bombs = []
    for i in range(bombs):  # quantidade de bombas
        i = random.randint(0, row - 1)  # y -1
        j = random.randint(0, column - 1)  # x -1
        if [i, j] not in array_of_bombs:
            array_of_bombs.append([i, j])
    return array_of_bombs


def bombs_around(row, column, bombs):
    count = 0
    if [row + 1, column] in bombs:
        count += 1
    if [row - 1, column] in bombs:
        count += 1
    if [row, column - 1] in bombs:
        count += 1
    if [row - 1, column - 1] in bombs:
        count += 1
    if [row + 1, column - 1] in bombs:
        count += 1
    if [row - 1, column + 1] in bombs:
        count += 1
    if [row + 1, column + 1] in bombs:
        count += 1
    if [row, column + 1] in bombs:
        count += 1
    return count


# Cria o tabuleiro
def make_board(rows, columns):
    board = [[" " for i in range(rows)] for j in range(columns)]
    return board


# Exibe o Tabuleiro
def show_board(board, rows):
    for i in range(rows):
        print(" ")
        print(board[i])

server()