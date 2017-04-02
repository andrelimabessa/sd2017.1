import socket
import CampoMinado
from datetime import datetime

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000            
HOST = ''     	       
a = ''

def enviar(address, text):
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)

    
    data = text.encode(ENCODE)  
    sock.sendto(data, address)  


def server():
    
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)

    while True:
        
        data, address = sock.recvfrom(MAX_BYTES) 
        text = data.decode(ENCODE) 
        

        if int(text) == 1:
            a = CampoMinado.campominado()
            
            text = "1"
            data = text.encode(ENCODE) 
            sock.sendto(data, address) 
        elif int(text) == 2:
            text = "2"
            if a.numJogadas == 0:
                text = "0"
                data = text.encode(ENCODE)  
                sock.sendto(data, address)
            else:
                data = text.encode(ENCODE)  
                sock.sendto(data, address)

                data, address = sock.recvfrom(MAX_BYTES)  
                text = data.decode(ENCODE)


                xy = text.split(",")
                text = a.jogada(int(xy[0]), int(xy[1]))
                data = text.encode(ENCODE)  
                sock.sendto(data, address)  


