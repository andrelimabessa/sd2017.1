from random import*

matriz = []

class criarCampoMinado (object):

	#função para verificar tamanho do campo
	def verificarTamanhoCampo(self, nivel):
		#inicializa a matriz
		if nivel == "1":
			self.criarCampo (9, 10)
			
		else:
			self.criarCampo (16, 40)	
	pass 

	#criar campo minado
	def criarCampo (self, tamanho, bombas):

		#condição para preencher campo
		condicao = True

		#criar matriz para campo minado
		global matriz
		matriz = [[ "0" for j in range(tamanho) ] for i in range(tamanho)]

		#estrutura para colocar as bombas
		for i in range (bombas):
			#verificar possível repetição da bomba
			while condicao:

				x = randint(0, tamanho-1)
				y = randint(0, tamanho-1)

				if matriz [x][y] == "0": 
					matriz [x][y] = "1"
					condicao = False
			condicao = True
	pass

	#realizar jogada
	def jogada (self, nivel):

		condicao = True

		#inicializa a matriz
		if nivel == "1":
			tamanho = 8
			
		else:
			tamanho = 15

			
		while condicao:
			textTamanho =  str(8)

			texto =  ("Informe uma linha entre 0-" + textTamanho + ": ")
			linha = int (input (texto))
			print ()
			texto =  ("Informe uma coluna entre 0-" + textTamanho + ": ")
			coluna = int (input (texto))
			print ()

			if ((linha >= 0 and linha <= tamanho) and (coluna >= 0 and coluna <= tamanho)):
				condicao = False

		if matriz [linha] [coluna] == "0":
			matriz [linha] [coluna] = "2"
			return 0
		else:
			return -1
	pass


	def salvarArquivo (self, nivel):

		arq = open("texto.txt", 'w')
		arqNivel = open("nivel.txt", 'w')
		arqNivel.write(nivel)
		for i in range (len(matriz)):
			for j in range (len(matriz)):
				arq.write(matriz [i] [j])

		arq.close()	
	pass

	def abrirArquivo (self):

		arq = open("texto.txt", 'r')
		arqNivel = open("nivel.txt", 'r')
		nivel = arq.readlines()

		global matriz

		#inicializa a matriz
		print (nivel)
		if nivel == "1":
			matriz = [[ "0" for j in range(9) ] for i in range(9)]
			
		else:
			matriz = [[ "0" for j in range(16) ] for i in range(16)]
	
		linha = 0
		coluna = 0

		for linha in arq:
			matriz [linha] [coluna] = linha
			coluna = coluna + 1
			if coluna == len(matriz):
				linha = linha + 1

		arq.close()

		return nivel
	pass