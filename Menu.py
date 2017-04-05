#Campo Minado
from CriarCampoMinado import criarCampoMinado

criar = criarCampoMinado()

class menu (object):

	def criarMenu (self):

		global tpJogo
		condicao = True

		print ()
		print ("----Campo minado----")
		print ("1) Novo jogo:")
		print ("2) Carregar jogo:")
		print ("3) Sair:")
		print ()

		while condicao:
			tpJogo = int (input ("Informe a opção entre 1 e 3: "))
			print ()

			if (tpJogo >= 1 and tpJogo <= 3):
				condicao = False

		if tpJogo == 1:

			condicao = True

			print ("Novo Jogo")
			print ("1) Nível 1: 10 minas, grade 9 x 9")
			print ("2) Nível 2: 40 minas, grade 16 x 16")
			print ()

			while condicao:
				nivel = input ("Informe o nível 1 ou 2: ")
				print ()

				if (nivel == "1" or nivel == "2"):
					condicao = False

			criar.verificarTamanhoCampo (nivel)

			self.jogo(nivel)

		elif tpJogo == 2:
			print ("Continuando jogo....")
			print ()
			nivel = criar.abrirArquivo()
			self.jogo(nivel)
		else:
			print ("Até a próxima!!!!")
	pass

	def jogo (self, nivel):
		condicao = True

		while condicao:
			print ("Vamos jogar???")
			print ("1) Jogar")
			print ("2) Sair")
			print ()

			while condicao:
				opcao = input ("Informe a opção 1 ou 2: ")
				print ()

				if (opcao == "1" or opcao == "2"):
					condicao = False

			if opcao == "1":
				resultado = criar.jogada (nivel)
				if resultado == 0:
					print ("Acertou um campo vazio....")
					print ()
					condicao = True
				else:
					print ("Perdeu, você acertou uma bomba....")
					print ()	
				
			else:
				criar.salvarArquivo(nivel)

				condicao = False
				print ("Jogo salvo, até a próxima!!!!")
	pass