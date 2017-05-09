# coding: utf-8
import socket, pickle
import threading, random
import os, os.path


ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000  # Porta que o Servidor esta
HOST = ''  # Endereco IP do Servidor

""" Forma Orientado a objeto """
def server_thread_oo():
    # Abrindo uma porta UDP
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)
    while True:
        # recebi dados
        data, address = sock.recvfrom(MAX_BYTES)

        # Criação de thread orientada a objeto
        tratador = ThreadTratador(sock, data, address)
        tratador.start()


""" Forma Procedural """
def server_thread_procedural():
    # Abrindo uma porta UDP
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)
    while True:
        # recebi dados
        data, address = sock.recvfrom(MAX_BYTES)
        # Criação de thread procedural
        t = threading.Thread(target=conexao, args=tuple([sock, data, address]))
        t.start()


def conexao(sock, data, address):
    text = pickle.loads(data)
    cod, *dados = text

    if cod == "I":                      #inicializa um novo jogo e envia para o cliente
        criaCampo(sock, dados, address)
    elif cod == "M":                    #distribui as minas no tabuleiro
        poeMinas(sock, dados, address)
    elif cod == "S":                    #salva os dados no arquivo de forma codificada
        salvar(dados)
    elif cod == "F":                    #finaliza o jogo deletando o arquivo existente salvo
        finaliza(dados)
    elif cod == "C":                    #carrega um jogo salvo e envia para o cliente
        carrega_jogo_salvo(sock, address)


def criaCampo(sock, dados, address):
    linha, coluna, _ = dados
    campo = []
    for i in range(0, int(linha)):
        linha = []
        for j in range(0, int(coluna)):
            linha.append(0)

        campo.append(linha)
    data = pickle.dumps(campo)
    sock.sendto(data, address)

def poeMinas(sock, dados, address):
    linha, coluna, minas, matriz = dados
    for i in range(1,minas+1):
        p = random.randint(0,linha-1)#escolhe uma posição na linha aleatória
        q = random.randint(0,coluna-1)#escolhe uma posição na coluna aleatória
        if matriz[p][q] != 'B':
            matriz[p][q] = 'B'

    data = pickle.dumps(matriz)
    sock.sendto(data, address)

def salvar(dados):
    fileObject = open('salvo.pkl','wb')
    pickle.dump(dados, fileObject)
    fileObject.close()

def carrega_jogo_salvo(sock, address):
        fileObject = open('salvo.pkl', 'rb')
        dados = pickle.load(fileObject)

        data = pickle.dumps(dados)
        sock.sendto(data, address)


def finaliza(dados):
    print("\t\t Jogo finalizado!!!")
    print("\tVocê acertou uma mina em %s jogadas." % dados)
    os.unlink('salvo.pkl')
    print("Jogo salvo foi deletado pelo Server!!")


class ThreadTratador(threading.Thread):
    def __init__(self, a, b, c):
        threading.Thread.__init__(self)
        self.sock = a
        self.data = b
        self.address = c

    def run(self):
        tratar_conexao(self.sock, self.data, self.address)

if __name__ == "__main__":
    server_thread_procedural()