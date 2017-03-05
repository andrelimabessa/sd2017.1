tabuleiro = [ [ 0 for j in range(3) ] for i in range(5)]

tabuleiro [0][0] = 'B'
tabuleiro [1][2] = 'B'
tabuleiro [2][0] = 'B'
tabuleiro [4][2] = 'B'
tabuleiro [3][1] = 'B'



for linha in tabuleiro:
	print(linha)

print('\n')


for x in range(5):
	linha = input("\nLinha : ")
	coluna = input("\nColuna : ")
	if tabuleiro[linha][coluna] == 'B':
		print("Morreu")
		break
	else:
		print("Sucesso")
