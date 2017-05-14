from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
import random, os

def criaCampo(linha, coluna):
    print('Criando Tabuleiro do jogo')
    campo = []
    for i in range(0, linha):
        lin = []
        for j in range(0, coluna):
            lin.append(0)

        campo.append(lin)

    return campo

def poeMinas(matriz, linha, coluna, minas):
    print('Função põe minas')
    for i in range(1,minas+1):
        p = random.randint(0,linha-1)#escolhe uma posição na linha aleatória
        q = random.randint(0,coluna-1)#escolhe uma posição na coluna aleatória
        if matriz[p][q] != 'B':
            matriz[p][q] = 'B'

    return matriz

#salva as jogadas em arquivo texto
def salvar(jogadas, campo, linha, coluna):
    print('Salvando Jogo no server...')
    arq = open("salvo.pkl", 'w')
    arq.write(jogadas)
    arq.write('\n')
    arq.write("%d" %linha)
    arq.write(',')
    arq.write("%d" %coluna)
    arq.write(',')
    arq.write('\n')
    for i in campo:
        linha = ""
        for j in i:
            linha += ("%s" %j)
        arq.write(linha)
        arq.write('\n')
    arq.close()

def carregaJogo():
    print('Carregando jogo no server...')
    campo = []
    camp2 = []
    arq = open("salvo.pkl", 'r')
    jogadas = arq.readline()#lê a primeira linha que está as jogadas
    linha2 = arq.readline()#lê a segunda linha que esta as linhas e colunas
    linha2 = linha2.split(",")#cria uma lista dividida da linha 2
    qtdlinha = int(linha2[0])#pega a primeira posição e joga em linha
    qtdcoluna = int(linha2[1])#pega a segunda posição e joga em coluna

    for lin in arq:#pega o arquivo salvo e transforma em matriz
        linhas = []
        for i in lin:
            if i != '\n':
                linhas.append(i)
        campo.append(linhas)
        camp2.append(linhas)

    #faz a verificação do campo que foi carregado e cria um novo campo
    #sobreposto para mascarar as minas
    def mapeamento(x):
        if x == "B":#troca as minas por "0" quando verdadeiro
            x = '0'
            return x
        else:
            return str(x)

    #carrega o campo sobreposto
    campSobrePosto = []
    for lin in camp2:
        linha = []
        for i in lin:
            linha.append(mapeamento(i))
        campSobrePosto.append(linha)

    return int(jogadas), campo, campSobrePosto, qtdlinha, qtdcoluna#retorna as jogadas e os campos


def finaliza():
    print("\t\t Jogo finalizado!!!")
    if os.path.exists('salvo.pkl') == True:
        os.unlink('salvo.pkl')
        print("Jogo salvo, foi deletado pelo Server!!")
    else:
        print('Jogo Finalizado no Cliente')

def main():
    server = SimpleJSONRPCServer(('localhost', 7002))
    server.register_function(criaCampo)
    server.register_function(poeMinas)
    server.register_function(salvar)
    server.register_function(finaliza)
    server.register_function(carregaJogo)
    print("Start Server")
    server.serve_forever()

if __name__ == '__main__':
    main()