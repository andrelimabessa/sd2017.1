import socket, pickle
import os


ENCODE = "UTF-8"
HOST = "127.0.0.1"
PORT = 5000
MAX_BYTES = 65535


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

#envia o comando para o server por as minas no campo
def poeMinas(campo, linha, coluna, minas):
    dados = ["M", linha, coluna, minas, campo]
    data = pickle.dumps(dados)

#Envia para o server aplicar as minas e retorna a matriz com minas
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (HOST, PORT)
    sock.sendto(data, dest)

#Retorna a matriz com as minas
    data, address = sock.recvfrom(MAX_BYTES)
    dados = pickle.loads(data)
    return dados

#executa as jogadas no cliente
def escolha(linha, coluna, matrizB, matrizM):

    if linha.isnumeric() and coluna.isnumeric():       #verifica se os dois valores são numéricos

        if matrizM[int(linha)-1][int(coluna)-1] == "B":#verifica se nas coordenadas existe mina
            return 0
        else:
            matrizM[int(linha)-1][int(coluna)-1] = "*"
            matrizB[int(linha)-1][int(coluna)-1] = "*"
            return 1
    else:
        return 2                                       #se um dos dois for letra ele salva o jogo

#Envia o arquivo para ser salvo no server
def salvar(jogadas, campo, linha, coluna):
    dados = ["S", jogadas, linha, coluna, campo]
    data = pickle.dumps(dados)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (HOST, PORT)
    sock.sendto(data, dest)

#executa a finalização do jogo no server
def finaliza_jogo(jogadas):
    dados = ["F", jogadas]
    data = pickle.dumps(dados)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (HOST, PORT)
    sock.sendto(data, dest)

def start_game():
    game = True
    cont = 0

    linha = ''
    colunas = ''
    minas = ''

    campoComMinas = []
    CampoSemMinas = []
    print("\tBem vindo ao Campo minado!!")
    if os.path.exists('salvo.pkl') == True:                                 #faz uma verificação se o path do arquivo existe
        print("\a\a\a\a Carregando Jogo Salvo...")
        print("\t\tJogo Carregado, Continue...")
        dados = ["C", 'salvo.pkl']
        data = pickle.dumps(dados)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(data, (HOST, PORT))                                    #faz uma requisição no server do jogo salvo

        data, address = sock.recvfrom(MAX_BYTES)
        dados = pickle.loads(data)
        cont, linha, colunas, campoComMinas = dados
        cont = int(cont)

        def mapeamento(x):
            if x == "B":                                                     # troca as minas por "0" quando verdadeiro
                x = '0'
                return x
            else:
                return str(x)


        for lin in campoComMinas:                                             # carrega o campo sem minas
            linha = []
            for i in lin:
                linha.append(mapeamento(i))
            CampoSemMinas.append(linha)

    else:
        print("\a\a\a\a Iniciando Novo Jogo...")
        linha = input('Digite a quantidade de linhas: ')
        colunas = input('Digite a quantidade de colunas: ')
        minas = input('Digite a qtd de Minas: ')

        dados = ["I", linha, colunas, minas]                                    #Inicializa um novo jogo no server
        data = pickle.dumps(dados)

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dest = (HOST, PORT)
        sock.sendto(data, dest)

        print(sock.getsockname())
        data, address = sock.recvfrom(MAX_BYTES)
        dados = pickle.loads(data)                                              #retorna a matriz contando o campo vazio
        CampoSemMinas = dados                                                   #preenche a matriz campoSemMinas
        campoComMinas = poeMinas(dados, int(linha), int(colunas), int(minas))   #põe as minas

    while game:
        mostraCampoSMinas(CampoSemMinas, linha, colunas)

        print("\nJogadas: %d" % cont)
        cont += 1

        print("Se desejar encerrar o jogo digite uma letra, no lugar da linha!")
        hitL = input('\tEscolha a linha: ')
        hitC = input("\tEscolha a Coluna: ")

        game = escolha(hitL, hitC, CampoSemMinas, campoComMinas)                #executa a função escolha e retorna um valor de opção
        if game == 1:
            os.system("cls")
            salvar(str(cont), campoComMinas, linha, colunas)
            continue
        elif game == 2:                                                        #caso seja escolhido uma letra ao invés de numero ele salva
            os.system("cls")
            os.system("color 0F")
            salvar(str(cont), campoComMinas, linha, colunas)
            print("\n\tJogo salvo, Jogo encerado!!!")
            break
        else:
            os.system("cls")
            os.system("color 0C")
            print("\t\t Jogo finalizado!!!")
            print("\tVocê acertou uma mina em %d jogadas." % cont)
            mostraCampoComMinas(campoComMinas, linha, colunas)
            finaliza_jogo(cont)                                             #executa a função de finalização do game
            print("\n\a\a\a....Arquivo salvo deletado com sucesso...\a\a\a")
            break

if __name__ == '__main__':
    start_game()
