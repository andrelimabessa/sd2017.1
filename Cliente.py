import socket
from datetime import datetime




ENCODE = "UTF-8"
HOST = '127.0.0.1'   
PORT = 5000         
MAX_BYTES = 65535   


def client():
   
    while True:
        print ("1 - Novo Jogo")
        print("2 - Fazer jogada")
        text = input("Digite uma opcao: ")  
        data = text.encode(ENCODE)  

    
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
        dest = (HOST, PORT) 
        sock.sendto(data, dest)  

     
        data, address = sock.recvfrom(MAX_BYTES)  
        text = data.decode(ENCODE)  

        if int(text) == 0:
            text = "Fim do jogo!"

        elif int(text) == 1:
            text = "Novo Jogo Iniciado"

        elif int(text) == 2:
            x = input("Digite a posicao do eixo X:")
            y = input("Digite a posicao do eixo Y:")
            text = x+","+y
            data = text.encode(ENCODE)
            sock.sendto(data, dest)  
            data, address = sock.recvfrom(MAX_BYTES)  
            text = data.decode(ENCODE)  



        print("\n\n"+text+"\n")  