import zmq
import sys
import random, os

port = "5559"
context = zmq.Context()
print ("Conectando com o servidor...")

socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port)
client_id = random.randrange(1,10005)

def start_game():
    game = True
    cont = 0

    linhas = ''
    colunas = ''
    minas = ''

    campoComMinas = []
    campoSemMinas = []
    print("\tBem vindo ao Campo minado!!")
    if os.path.exists('salvo.zmq') == True:
        print("\a\a\a\a Carregando Jogo Salvo!")
        print("\t\tJogo Carregado, Continue!")
        dados = ["C", 'salvo.pkl']
        socket.send_json(dados)

        data = socket.recv_json()
        cont, linhas, colunas, campoComMinas, campoSemMinas = data
        cont = int(cont)
        print(data)



    else:
        print("\a\a\a\a Iniciando Novo Jogo...")
        linhas = input('Digite a quantidade de linhas: ')
        colunas = input('Digite a quantidade de colunas: ')
        minas = input('Digite a qtd de Minas: ')

        #cria um tabuleiro em branco
        dados = ["I", linhas, colunas]
        socket.send_json(dados)
        campoSemMinas = socket.recv_json()

        #põe minas escondidas no tabuleiro
        dados = ["M", linhas, colunas, minas, campoSemMinas]
        socket.send_json(dados)
        campoComMinas = socket.recv_json()


    while game:
        mostraCampoSMinas(campoSemMinas, linhas, colunas)

        print("\nJogadas: %d" % cont)
        cont += 1

        print("Se desejar encerrar o jogo digite uma letra, no lugar da linha!")
        hitL = input('\tEscolha a linha: ')
        hitC = input("\tEscolha a Coluna: ")

        game = escolha(hitL, hitC, campoSemMinas, campoComMinas)                #executa a função escolha e retorna um valor de opção
        if game == 1:
            os.system("cls")
            #salvar(str(cont), linhas, colunas, campoComMinas)
            continue
        elif game == 2:                                                        #caso seja escolhido uma letra ao invés de numero ele salva
            os.system("cls")
            os.system("color 0F")
            salvar(str(cont), linhas, colunas, campoComMinas)
            print("\n\tJogo salvo, Jogo encerado!!!")
            break
        else:
            os.system("cls")
            os.system("color 0C")
            print("\t\t Jogo finalizado!!!")
            print("\tVocê acertou uma mina em %d jogadas." % cont)
            mostraCampoComMinas(campoComMinas, linhas, colunas)
            finaliza_jogo(cont)                                             #executa a função de finalização do game
            print("\n\a\a\a....Arquivo salvo deletado com sucesso...\a\a\a")
            break



def mostraCampoSMinas(campo, linha, coluna):
    cont = 1
    col = "\a| "

    for i in range(1, int(coluna) + 1):
        col += ("\t%s" % i)
    print(col)

    for i in campo:
        linha = i
        l1 = ("%d| " % cont)
        for j in linha:
            l1 += ("\t%s" % j)
        print(l1)
        cont += 1

def mostraCampoComMinas(campo, linha, coluna):
    cont = 1
    col = "\a| "
    for i in range(1, int(coluna) + 1):
        col += ("\t%s" % i)
    print(col)
    for i in campo:
        linha = i
        l1 = ("%d| " % cont)
        for j in linha:
            l1 += ("\t%s" % j)
        print(l1)
        cont += 1

def escolha(linha, coluna, matrizB, matrizM):

    if linha.isnumeric() and coluna.isnumeric():       #verifica se os dois valores são numéricos

        if matrizM[int(linha)-1][int(coluna)-1] == "B":#verifica se nas coordenadas existe mina
            return 0
        else:
            matrizM[int(linha)-1][int(coluna)-1] = "*"
            matrizB[int(linha)-1][int(coluna)-1] = "*"
            return 1
    else:
        return 2

#Envia o arquivo para ser salvo no server

def salvar(jogadas, linha, coluna, campo):
    dados = ["S", jogadas, linha, coluna, campo]
    socket.send_json(dados)

#executa a finalização do jogo no server
def finaliza_jogo(jogadas):
    dados = ["F", jogadas]
    socket.send_json(dados)


if __name__ == '__main__':
    start_game()