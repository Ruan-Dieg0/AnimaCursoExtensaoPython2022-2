''' 
Meu primeiro projeto Python :D

//Aula 1:

print() = Comando de saida
Para guardar uma string (Frase): nome = "Ruan Diego" ou idade = 19
Para exibir string nome/idade: print(nome) ou print(idade)
Para exibir uma frase + string: print ("Meu nome e idade são: "+str(idade))
   ou print (f"Meu nome e idade são {nome} {idade}\n")
.
str: conversão de inteiro para string

Para exibir string e frase alternados: print("Meu nome é {} e tenho {} anos".format(nome, idade))

//Aula 2:

Comando para permitir que o usuário digite: nome = input("texto")
Comando para exibir o texto digitado: print(nome)
Para transformar o digitado em interiro:
idade = int(input("Digite sua idade: "))

Para mostrar o dobro da idade informada:
dobro = idade * 2 e print("O dobro da sua idade é: {}".format(dobro))


'''

#Aula 1:
'''
print ("Hello World")
nome = "Ruan Diego"
idade = 19
print (nome, idade)
print ("Meu nome e idade são: "+nome, idade)
print (f"Meu nome e idade são: {nome} {idade}\n")
print("Meu nome é {} e tenho {} anos".format(nome, idade))
'''

#Aula 2:
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print("\nSeu nome é {} e você tem {} anos".format(nome, idade))
dobro = idade * 2
print("\nO dobro da sua idade é: {}".format(dobro))