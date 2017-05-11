
import random

class CampMinado:
#Inicializa os valores nas variáveis
    def __init__(self, linha=0, coluna=0, minas=0):
        self.linha = linha
        self.coluna = coluna
        self.minas = minas

#faz a inserção das variáveis
    def insereDados(self, linha, coluna, minas):
        self.linha = linha
        self.coluna = coluna
        self.minas = minas

#cria um tabuleiro vazio com as dimensões especificadas
    def criaCampo(self, matriz):
        for i in range(0, self.linha):
            linha = []
            for j in range(0,self.coluna):
                linha.append(0)

            matriz.append(linha)
        return matriz

#insere as minas em um tabuleiro específicado
    def poeMinas(self, matriz):

        for i in range(1,self.minas+1):
            p = random.randint(0,self.linha-1)#escolhe uma posição na linha aleatória
            q = random.randint(0,self.coluna-1)#escolhe uma posição na coluna aleatória
            if matriz[p][q] != 'B':
                matriz[p][q] = 'B'

        return matriz


#mostra o campo sobreposto ao campo minado com as jogadas feitas
    def mostraCampoSMinas(self, campo):
        cont = 1
        col = "\a| "
        lin = ""
        for i in range(1, self.coluna + 1):
            col += ("\t%s" % i)
            lin += ("_"*i)
        print(col)
        print(lin)

        for i in campo:
            linha = i
            l1 = ("%d| " % cont)
            for j in linha:
                l1 += ("\t%s" % j)
            print(l1)
            cont += 1

# tabuleiro onde vai estar as minas e as jogadas
    def mostraCampoComMinas(self, campo):
        cont = 1
        col = "\a| "
        for i in range(1, self.coluna + 1):
            col += ("\t%s" % i)
        print(col)
        for i in campo:
            linha = i
            l1 = ("%d| " % cont)
            for j in linha:
                l1 += ("\t%s" % j)
            print(l1)
            cont += 1

#verifica se existe jogo salvo e retorna um flag
    def verificaArq(self):

        arq = open("salvo.txt", 'r')
        linha = int(arq.readline())
        if linha != 0:
            return True
        else:
            return False
        arq.close()

#jogadas que são realizadas no principal
    def escolha(self,linha, coluna, matrizB, matrizM):

        if linha.isnumeric() and coluna.isnumeric():

            if matrizM[int(linha)-1][int(coluna)-1] == "B":#verifica se nas coordenadas existe mina
                return 0
            else:
                matrizM[int(linha)-1][int(coluna)-1] = "*"
                matrizB[int(linha)-1][int(coluna)-1] = "*"
                return 1
        else:
            return 2


#zera o arquivo e põe o valor de 0 na primeira linha
    def zeraArquivo(self):
        arq = open("salvo.txt", 'w')
        arq.write('0')
        arq.close()

#salva as jogadas em arquivo texto
    def salvar(self, jogadas, campo):

        arq = open("salvo.txt", 'w')
        arq.write(jogadas)
        arq.write('\n')
        arq.write("%d" %self.linha)
        arq.write(',')
        arq.write("%d" %self.coluna)
        arq.write(',')
        arq.write('\n')
        for i in campo:
            linha = ""
            for j in i:
                linha += ("%s" %j)
            arq.write(linha)
            arq.write('\n')
        arq.close()

#após a confirmação do arquivo ele carrega as informações do arquivo txt
    def carregaJogo(self):

        campo = []
        camp2 = []
        arq = open("salvo.txt", 'r')
        linha1 = arq.readline()#lê a primeira linha que está as jogadas
        linha2 = arq.readline()#lê a segunda linha que esta as linhas e colunas
        linha2 = linha2.split(",")#cria uma lista dividida da linha 2
        self.linha = int(linha2[0])#pega a primeira posição e joga em linha
        self.coluna = int(linha2[1])#pega a segunda posição e joga em coluna

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

        return int(linha1), campo, campSobrePosto#retorna as jogadas e os campos

