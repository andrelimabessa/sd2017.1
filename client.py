# -*- coding: utf-8 -*-
import base64
import socket
import json
from datetime import datetime

from server import show_board, put_bombs, make_board, bombs_around

ENCODE = "UTF-8"
HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta
MAX_BYTES = 65535  # Quantidade de Bytes a serem ser recebidos


def client():
    """ Procedimento responsável por enviar dados para o servidor e 
    receber alguma resposta por conta disso """
    rows = int(input("Digite a quantidade de linhas que deseja: "))
    columns = int(input("Digite a quantidade de colunas que deseja: "))
    bombs = int(input("Digite a quantidade de bombas: "))

    # data = text.encode(ENCODE)  # Codifica para BASE64 os dados de entrada
    data = {
        'rows': rows,
        'columns': columns,
        'bombs': bombs
    }
    encoded_data = json.dumps(data)

    lose = True
    attempts = 0

    board = make_board(rows, columns)
    bombs = put_bombs(bombs, rows, columns)
    show_board(board, rows)

    while lose:
        user_row = int(input("\nDigite a linha: "))
        user_column = int(input("Digite a colunas: "))
        if [user_row, user_column] in bombs:
            print("Você perdeu.")
            break
        else:
            board[user_row][user_column] = str(bombs_around(user_row, user_column, bombs))
            show_board(board, rows)
            attempts += 1
            if ((rows * columns) - attempts) == len(bombs):
                print("Você ganhou.")
                break


client()
