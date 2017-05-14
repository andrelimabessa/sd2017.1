from jsonrpclib import Server
import os

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


def main():
    proxy = Server('http://localhost:7002')

    game = True
    cont = 0

    linhas = 0
    colunas = 0
    minas = 0

    campoComMinas = []
    campoSemMinas = []

    print("\t---- Bem vindo ao Campo Minado!! ----")
    if os.path.exists('salvo.pkl') == True:
        print("\a\a\a\a Carregando Jogo Salvo...")
        print("\t\tJogo Carregado, Continue...")
        cont, campoComMinas, campoSemMinas, linhas, colunas = proxy.carregaJogo()

    else:
        print("\t\t------- Carregando Novo Jogo -------")
        linhas = int(input('Digite a quantidade de linhas: '))
        colunas = int(input('Digite a quantidade de colunas: '))
        minas = int(input('Digite a qtd de Minas: '))

        campoSemMinas = proxy.criaCampo(linhas, colunas)
        campoComMinas = proxy.poeMinas(campoSemMinas, linhas, colunas, minas)

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
            proxy.salvar(str(cont), campoComMinas, linhas, colunas)
            continue
        elif game == 2:                                                        #caso seja escolhido uma letra ao invés de numero ele salva
            os.system("cls")
            os.system("color 0F")
            proxy.salvar(str(cont), campoComMinas, linhas, colunas)
            print("\n\tJogo salvo, Jogo encerado!!!")
            break
        else:
            os.system("cls")
            os.system("color 0C")
            print("\t\t Jogo finalizado!!!")
            print("\tVocê acertou uma mina em %d jogadas." % cont)
            mostraCampoComMinas(campoComMinas, linhas, colunas)
            proxy.finaliza()                                             #executa a função de finalização do game
            print("\n\a\a\a....Arquivo salvo, deletado com sucesso...\a\a\a")
            print('------ Obrigado por jogar -----')
            break


if __name__ == '__main__':
    main()