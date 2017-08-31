import random

class campominado(object):
    def __init__(self):
        self.tabuleiro = [["A" for j in range(5)] for i in range(5)]
        self.numJogadas = 3
        if self.existeJogoSalvo():
            self.carregarTabuleiro()
            self.carregarJogadas()
        else:
            self.preencherTabuleiro()

    def preencherTabuleiro(self):
        for i in range(2):
            x = random.randint(0, 4)
            y = random.randint(0, 4)
            if self.tabuleiro[x][y] == "B":
                i -= 1
            else:
                print(str(x) + "-" + str(y))
                self.tabuleiro[x][y] = "B"

    def existeJogoSalvo(self):
        arq = open("tabuleiro.txt", "r")
        if arq.readline() == "":
            existe = False
        else:
            existe = True
        return existe

    def salvarJogadas(self):
        self.arq = open("jogadas.txt", "w")
        self.arq.write(str(self.numJogadas))
        self.arq.close()

    def salvarTabuleiro(self, eixoX, eixoY, valor):
        self.arq = open("tabuleiro.txt", "w")
        self.arq.write(str(eixoX) + "-" + str(eixoY) + "-" + str(valor) + "\n")
        self.arq.close()

    def carregarJogadas(self):
        arq = open("jogadas.txt", "r")
        for linha in arq:
            self.numJogadas = int(linha)
        arq.close()

    def carregarTabuleiro(self):
        arq = open("tabuleiro.txt", "r")
        for linha in arq:
            valor = linha.split("-")
            self.tabuleiro[int(valor[0])][int(valor[1])] = "B"
        arq.close()


    def jogada(self, jogadaEixoX, jogadaEixoY):
        if self.tabuleiro[jogadaEixoX][jogadaEixoY] == "B":
            self.tabuleiro[jogadaEixoX][jogadaEixoY] = "X"
            msn = "Explosão da Bomba!"
            self.numJogadas -= 1

        elif self.tabuleiro[jogadaEixoX][jogadaEixoY] == "A":
            msn = "Bomba não encontrada!"
            self.numJogadas -= 1
        else:
            msn = "posição já usada!"

        return msn

    def limparLogs(self):
        self.arq = open("jogadas.txt", "w")
        self.arq.close()
        self.arq = open("tabuleiro.txt", "w")
        self.arq.close()