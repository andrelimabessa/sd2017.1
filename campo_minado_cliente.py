from campo_minado_servidor import *
import random

def main():
    
    perdeu = False;
    jogadas = 0;

    linhasMatriz = int(input("Digite quantas linhas deseja >> "))
    colunasMatriz = int(input("Digite quantas colunas deseja >> "))
    quantidadeBombas = int(input("Digite a quantidade de bombas >> "))

    matriz = gerarMatriz(linhasMatriz,colunasMatriz)
    mostrarMatriz(matriz,linhasMatriz)
    posBombas = sortearBombas(quantidadeBombas,linhasMatriz,colunasMatriz)

    historico = {"matriz" : matriz , "posBombas":posBombas, "jogadas" : jogadas}


    while (perdeu==False):
        linha = int(input("\nDigite a linha >> "))
        coluna = int(input("Digite a coluna >> "))
        if ([linha,coluna] in posBombas):
            print("\nBOOM!!! Você perdeu.")
            break
        else:
            matriz[linha][coluna] = str(bombasAoRedor(linha,coluna,posBombas))
            mostrarMatriz(matriz,linhasMatriz)
            jogadas += 1
            
            file = open("log.txt",w)
            file.write(str(historico))
            file.close()
            if (((linhasMatriz*colunasMatriz)-jogadas)==len(posBombas)):
                print("\nPARABÉNS!!! Você ganhou o desafio.")
                break;                
        
main()