num = 13
nome = "Samuel"
hello = "Hello"

print(hello)
print(hello + "Word")#concatenação
print(hello*3)#repetição
print(hello[0])#Primeiro Indice
print(hello[-1])#Último indice
print(len(hello))
print('e' in hello)
var = "Centro Universitário 7 de Setembro - UNI7"
print(var[1:7])
print(var[1:7:2])
print(var[::-1])
print(var.split())
print(var.count("7"))
var2 = var.split()
print("/".join(var2))
tupla = ("Bom", "Dia")  #Imutável
lista = ["Boa","Noite",["Boa", "tarde"],2] #Mutável
lista.append("texto")
#tupla.append("texto") #Inviável
print(lista[1])       #Suporta a slicing
a = list(range(5))
print(a)
a.insert(0,42)        #<Índice>,<valor inserido>
print (a)
a.reverse()
print (a)
a.sort()
print (a)






input("Digite Enter")