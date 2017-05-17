import zmq
import time
import sys
import random, pickle
import os, os.path


port = "5560"
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:%s" % port)
server_id = random.randrange(1,10005)

while True:

    message = socket.recv_json()
    cod, *dados = message

    # inicializa um novo jogo e envia para o cliente
    if cod == "I":
        linha, coluna = dados
        campo = []
        for i in range(0, int(linha)):
            linha = []
            for j in range(0, int(coluna)):
                linha.append(0)

            campo.append(linha)
        data = campo
        socket.send_json(data)

    # distribui as minas no tabuleiro
    elif cod == "M":
        linha, coluna, minas, matriz = dados
        for i in range(1, int(minas) + 1):
            p = random.randint(0, int(linha) - 1)  # escolhe uma posição na linha aleatória
            q = random.randint(0, int(coluna) - 1)  # escolhe uma posição na coluna aleatória
            if matriz[p][q] != 'B':
                matriz[p][q] = 'B'
        data = matriz
        socket.send_json(data)

    # salva os dados no arquivo de forma codificada
    elif cod == "S":
        jogadas, linhas, colunas, campo = dados
        arq = open("salvo.zmq", 'w')
        arq.write("%s" %jogadas)
        arq.write('\n')
        arq.write("%s" %linhas)
        arq.write(',')
        arq.write("%s" %colunas)
        arq.write(',')
        arq.write('\n')
        for i in campo:
            linha = ""
            for j in i:
                linha += ("%s" % j)
            arq.write(linha)
            arq.write('\n')
        arq.close()

    # finaliza o jogo deletando o arquivo existente salvo
    elif cod == "F":
        if os.path.exists("salvo.zmq"):
            print("\t\t Jogo finalizado!!!")
            os.unlink('salvo.zmq')
            print("Jogo salvo foi deletado pelo Server!!")

    # carrega um jogo salvo e envia para o cliente
    elif cod == "C":
        campo = []
        camp2 = []
        arq = open("salvo.zmq", 'r')
        linha1 = arq.readline()  # lê a primeira linha que está as jogadas
        linha2 = arq.readline()  # lê a segunda linha que esta as linhas e colunas
        linha2 = linha2.split(",")  # cria uma lista dividida da linha 2
        linha = linha2[0]  # pega a primeira posição e joga em linha
        coluna = linha2[1]  # pega a segunda posição e joga em coluna

        for lin in arq:  # pega o arquivo salvo e transforma em matriz
            linhas = []
            for i in lin:
                if i != '\n':
                    linhas.append(i)
            campo.append(linhas)
            camp2.append(linhas)

            # faz a verificação do campo que foi carregado e cria um novo campo
            # sobreposto para mascarar as minas

        def mapeamento(x):
            if x == "B":  # troca as minas por "0" quando verdadeiro
                x = '0'
                return x
            else:
                return str(x)

        # carrega o campo sobreposto
        campSobrePosto = []
        for lin in camp2:
            linhas = []
            for i in lin:
                linhas.append(mapeamento(i))
            campSobrePosto.append(linhas)

        arq.close()
        dados = linha1, linha, coluna, campo, campSobrePosto  # retorna as jogadas e os campos
        socket.send_json(dados)





