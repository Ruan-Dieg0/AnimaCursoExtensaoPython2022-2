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

'''
//
//Aula 3:
//

Laços
Comando while para sequenciar (laço)
Laço for: for fruta in frutas:
              print(fruta)

Lista: ["morango", "laranja", "pera"]
       print(frutas[3])

Adicionar item à lista: frutas.append("")
Quantidade de itens na lista: (len())   *length = tamanho




##Código Aula 3:
contador = 1

while(contador <= 10):
  print(contador)
  contador = contador+1

frutas = ["morango", "laranja", "pera"]
print(frutas[2])
print(len(frutas))
frutas.append("manga")

#i é uma variável
i=0
while(i<4):
  print(frutas[i])
  i = i + 1

for fruta in frutas:
  print(fruta)

'''
#Criando funções
#calcular 5% de imposto, guardar na variável imposto
preco = 200
imposto = preco * 0.05
print(imposto)

#Criar função para calcular o imposto que calcula um imposto de 5% e retorna a quem pediu

def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto

preco = 100
imposto = calcular_imposto(preco)
print(imposto)

















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


#Joguinho da velha
def menu():
    continuar=1
    while continuar:
        continuar = int(input("0. Sair \n"+
                              "1. Jogar novamente\n"))
        if continuar:
            game()
        else:
            print("Saindo...")

def game():
    jogada=0

    while ganhou() == 0:
        print("\nJogador ", jogada%2 + 1)
        exibe()
        linha  = int(input("\nLinha :"))
        coluna = int(input("Coluna:"))

        if board[linha-1][coluna-1] == 0:
            if(jogada%2+1)==1:
                board[linha-1][coluna-1]=1
            else:
                board[linha-1][coluna-1]=-1
        else:
            print("Nao esta vazio")
            jogada -=1

        if ganhou():
            print("Jogador ",jogada%2 + 1," ganhou apos ", jogada+1," rodadas")

        jogada +=1
    
def ganhou():
    #checando linhas
    for i in range(3):
        soma = board[i][0]+board[i][1]+board[i][2]
        if soma==3 or soma ==-3:
            return 1

     #checando colunas
    for i in range(3):
        soma = board[0][i]+board[1][i]+board[2][i]
        if soma==3 or soma ==-3:
            return 1

    #checando diagonais
    diagonal1 = board[0][0]+board[1][1]+board[2][2]
    diagonal2 = board[0][2]+board[1][1]+board[2][0]
    if diagonal1==3 or diagonal1==-3 or diagonal2==3 or diagonal2==-3:
        return 1

    return 0

def exibe():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                print(" _ ", end=' ')
            elif board[i][j] == 1:
                print(" X ", end=' ')
            elif board[i][j] == -1:
                print(" O ", end=' ')

        print()
                

board= [ [0,0,0],
         [0,0,0],
         [0,0,0] ]

menu()
'''



#Comandos da aula de Git
#--help
#git clone + link do repositório do github (Botão direito para colar)
#git init (Criar repositório Git vazio)
#git status ()


