import zmq
import sys, os
import random
from ast import literal_eval

try:
    ######### Configurações #########
    port = "5560"
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.connect("tcp://localhost:%s" % port)
    ############## FIM ##############
    '''
    message = socket.recv() #Recebe dados do Cliente
    data = text.encode("UTF-8") #Codifica os dados
    socket.send(data) #Envia dados para o cliente
    '''

    def verifyFile():
        arquivo = open('log_game.txt', 'r')
        dados = literal_eval(arquivo.read())
        arquivo.close()
        return dados



except:
    for val in sys.exc_info():
        print(val)

def server():
    aux = socket.recv()
    id = aux.get('id')
    data = aux.get('data')
    print("Cheguei ate aqui")

server()