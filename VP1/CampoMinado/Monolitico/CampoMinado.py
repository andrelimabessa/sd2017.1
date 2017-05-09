import os
from classeMinado import *


os.system("color 0E")
os.system("cls")

game = True
cont = 0

campoMinado = CampMinado()
campoComMinas = []
campoSemMinas = []

print("\t\t------- Jogo Campo Minado -------")
flag = campoMinado.verificaArq()

if flag == True:
    print("Existe um jogo em abeto...")
    cont, campoComMinas, campoSemMinas = campoMinado.carregaJogo()
else:
    linha = int(input('Digite a quantidade de linhas: '))
    colunas = int(input('Digite a quantidade de colunas: '))
    minas = int(input('Digite a qtd de Minas: '))
    campoMinado.insereDados(linha, colunas, minas)

    campoComMinas = campoMinado.criaCampo(campoComMinas)
    campoSemMinas = campoMinado.criaCampo(campoSemMinas)
    campoComMinas = campoMinado.poeMinas(campoComMinas)


while game:
    campoMinado.mostraCampoSMinas(campoSemMinas)

    print("\nJogadas: %d" % cont)
    cont += 1

    #jogas de linha e coluna, e são armazenadas nas variáveis
    print("Se desejar encerrar o jogo digite uma letra, no lugar da linha!")
    hitL = input('\tEscolha a linha: ')
    hitC = input("\tEscolha a Coluna: ")

    game = campoMinado.escolha(hitL, hitC, campoSemMinas, campoComMinas)
    if game == 1:
        os.system("cls")
        campoMinado.salvar(str(cont), campoComMinas)
        continue
    elif game == 2:
        os.system("cls")
        os.system("color 0F")
        campoMinado.salvar(str(cont), campoComMinas)
        print("\n\tJogo salvo, Jogo encerado!!!")
        break
    else:
        os.system("cls")
        os.system("color 0C")
        print("\n---- \a Você Acertou uma mina em %d jogadas\n" %cont)
        campoMinado.mostraCampoComMinas(campoComMinas)
        campoMinado.zeraArquivo()
        break

print('------ Obrigado por jogar -----')


