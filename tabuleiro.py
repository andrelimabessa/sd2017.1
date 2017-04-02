class Jogo():

    def criar_tabuleiro(self):
        self.tabuleiro = [[0 for j in range(5)] for j in range(5)]
        for linha in self.tabuleiro:
            print(linha)

        return self.tabuleiro

    def vetor_tab(self):
        self.vetor_tab = [[0 for i in range(5)] for i in range(5)]
        self.vetor_tab[1][3] = 1
        self.vetor_tab[2][2] = 1
        self.vetor_tab[3][0] = 1
        self.vetor_tab[0][4] = 1
        self.vetor_tab[0][2] = 1
        self.vetor_tab[1][1] = 1


    def inicio(self):
        print("\n======== C A M P O  M I N A D O ==========")
        print("Bem ao vindo Campo Minado.\n Existem 10 bombas no tabuleiro.\n Boa sorte!\n") 

    def jogada(self):
        self.x = int(input("Escolha a linha do tabuleiro: "))
        self.y = int(input("Escolha a coluna do tabuleiro: "))
        print ("Voce jogou em: %d, %d"%(self.x,self.y))
        if self.tabuleiro[self.x][self.y] == 0:
            if self.vetor_tab[self.x][self.y] == 0:
                print("\nBoa jogada ! Continue..")
                self.tabuleiro[self.x][self.y] == 'x'
                
                
            else:
                print("\n MINA !\n ...::GAME OVER::...")


            