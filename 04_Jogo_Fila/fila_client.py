import zmq
import sys, os, pickle
import random
from ast import literal_eval

######### Configurações #########
port = "5559"
context = zmq.Context()
print ("Conectando com o servidor...")
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port)
############## FIM ##############

#Main definition - constants
menu_actions = {}

'''
data = text.encode("UTF-8") #Encoda texto
socket.send (data)#Envia para o Servidor
message = socket.recv() #Recebe do Servidor
'''
# Main menu
def main_menu():
    if os.path.exists("log_game.txt") == True:
        waiter = {"id": 'VF', "data": "log_game.txt"}
        socket.send(waiter)  # Envia para o Servidor
        dict = socket.recv()  # Recebe do Servidor
        if (dict.get('without') == "-1"):
            #layout()
            choice = input(" >> ")
            exec_menu(choice)
            return
        else:
            #restartGame()
            print("Restart Game")
    else:
        #layout()
        choice = input(" >> ")
        exec_menu(choice)
        return

def exec_menu(choice):
    os.system("cls")
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Seleção inválida, por favor tentar novamente. \n")
            os.system("pause")
            menu_actions['main_menu']()
    return

# Back to main menu
def back():
    menu_actions['main_menu']()

# Exit program
def exit():
    print("\nMuito Obrigado!!!\nVolte sempre! ")
    os.system("pause")
    sys.exit()

menu_actions = {
    'main_menu': main_menu,
    #'1': newGame,
    #'2': restartGame,
    '9': back,
    '0': exit,
}

# Main program
if __name__ == "__main__":
    # Launch main menu
    main_menu()

input("Saida Enter")