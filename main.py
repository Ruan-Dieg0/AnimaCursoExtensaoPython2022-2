''' 
Meu primeiro projeto Python :D

//Aula 1:
//

print() = Comando de saida
Para guardar uma string (Frase): nome = "Ruan Diego" ou idade = 19
Para exibir string nome/idade: print(nome) ou print(idade)
Para exibir uma frase + string: print ("Meu nome e idade são: "+str(idade))
   ou print (f"Meu nome e idade são {nome} {idade}\n")
.
str: conversão de inteiro para string

Para exibir string e frase alternados: print("Meu nome é {} e tenho {} anos".format(nome, idade))

#Código Aula 1:
print ("Hello World")
nome = "Ruan Diego"
idade = 19
print (nome, idade)
print ("Meu nome e idade são: "+nome, idade)
print (f"Meu nome e idade são: {nome} {idade}\n")
print("Meu nome é {} e tenho {} anos".format(nome, idade))

//
//Aula 2:
//

Comando para permitir que o usuário digite: nome = input("texto")
Comando para exibir o texto digitado: print(nome)
Para transformar o digitado em interiro:
idade = int(input("Digite sua idade: "))

Para mostrar o dobro da idade informada:
dobro = idade * 2 e print("O dobro da sua idade é: {}".format(dobro))

Estrutura condicional (if): if idade >= 18:
If e And juntos em um input: if idade >= 18 and genero == "M":
Elif para condicionais extras

##Código Aula 2:
nome = input("Informe seu nome: ")
idade = int(input("Digite sua idade: "))
genero = input("Informe seu gênero, M= Masculino e F= Feminino: ")
print("\nSeu nome é {} e você tem {} anos".format(nome, idade))
dobro = idade * 2
#print("\nO dobro da sua idade é: {}".format(dobro))
if idade >= 18:
  print("e já pode beber")
else:
  print("e não use drogas")
if idade >= 18 and genero == "M":
  print("\nServiço militar obrigatório")

##Extra:
nome = input("Informe seu nome: ")
nota = float(input("Digite sua nota: "))
if nota == 10:
  print("\nNada mais que o mínimo")
elif nota >= 7 and nota < 10:
  print("Ta safe po, da pra passar")
if nota >= 6 and nota < 7:
  print("Passou que nem nija")
else:
  print("\nRelaxa po, só fazer ano que vem")
'''












#Implementação do estudando em uma única extrutura
print("Olá, bem vindo a sua interface privada do usuário ✨")
nome = input("\nInforme seu nome: ")
senha = input("Escreva sua senha: ")
if senha == "ruan":
  print("\nAcesso liberado")
else:
  print("\nSenha incorreta. Tente novamente.")
if senha == "ruan":
  navbar = input("\nNotas   Faltas   Histórico\n->")

if navbar == "notas" or navbar == "Notas":
  print("\nNotas:\nPython: 9.8\nGithub: 9.9")
elif navbar == "Faltas" or navbar == "faltas":
  print("\nNenhuma falta registrada.")
elif navbar == "Histórico" or navbar == "Historico" or navbar == "histórico" or navbar == "historico":
  print("\nVocê ainda não possui notas registradas.")
else:
  print("\nOpção não identificada, escolha uma das listadas acima.")