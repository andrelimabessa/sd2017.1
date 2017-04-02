from tabuleiro import *

t = Jogo()
t.inicio()

print("Menu:\n")
print("1. Iniciar jogo;")
print("2. Visualizar tabuleiro;")
print("3. Realizar jogada;")
print("4. Retornar partida anterior;")
print("5. Finalizar jogo;\n")

print("Escolha de acordo com a numeracao do Menu, a acao desejada.")
escolha = int(input("Digite sua escolha:"))
print("")



if escolha == 1:
	t.criar_tabuleiro()
	t.vetor_tab()
	t.jogada()

elif escolha == 2:
	t.visualiza_tabuleiro()
	t.menu()
elif escolha == 3:
	t.jogada()
	t.menu()
elif escolha == 4:
	t.finaliza_jogo()


# criar tabuleiro ; escolher jogada  
# mostrar resultado : 
		# JOGADA : OK -> escolher jogada...
		# MINA! : GAME OVER -> Novo jogo?

# finalizar jogo