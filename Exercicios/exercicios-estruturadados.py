# 1. Escreva um programa que lê números inteiros positivos do usuário, um após o outro, e monta uma lista a partir desses números e depois imprime a lista montada.
# O programa deve continuar solicitando por números até que o elemento digitado seja um número negativo (que não deve ser inserido na lista).

# print("Digite números positivos para montar uma lista! Para finalizar o programa, digite um número negativo!\n")
# n = 0
# lista = []
# while n >= 0:
#     n = int(input("Digite um número:\n"))
#     if n >= 0:
#         lista.append(n)
#         print("Número Registrado!\n")
#     else:
#         print("Finalizando o programa...")
#         break
    
# print(lista) 

# 2. Dada uma lista de números inteiros, escreva um programa que calcula a soma de todos os números na lista.

# print("Digite números positivos para ficarem registrados em uma lista! Quando quiser finalizar e somar todos eles, digite um número negativo!\n")

# i = 0
# lista = []
# while i >= 0:
#     i = int(input("Digite um número:\n"))
#     if i >= 0:
#         lista.append(i)
#         print("Número Registrado!\n")
#     else:
#         print("Finalizando o programa...")
#         break

# soma = sum(lista)    
# print(soma) 

# 3. Data uma lista de números inteiros, escreva um programa que calcula a média dos números na lista. O resultado não deve incluir números decimais. P.S -> // é usado para divisão inteiros

# print("Digite números inteiros positivos! Para encerrar o programa e mostrar a média dos números, digite um número negativo!\n")

# i = 0
# lista = []
# while i >= 0:
#     i = int(input("Digite um número:\n"))
#     if i >= 0:
#         lista.append(i)
#         print("Número Registrado!\n")
#     else:
#         print("Finalizando o programa...")
#         break

# soma = sum(lista) 
# media = soma // len(lista)   
# print("A média dos", len(lista), "números digitados é:", media)

# 4. Suponha o seguinte programa:
# Alunos e suas respectivas notas:
# alunos = [
#  ("Alice", 8),
#  ("Bob", 7),
#  ("Carlos", 9),
#  ]

# Escreva uma programa que calcula a média das notas de todos os alunos.

# print(len(alunos))
# soma = 0
# numero_alunos = len(alunos)

# for i in alunos:
#     soma = soma + i[1]
#     media = soma / numero_alunos
# print("A média das notas dos alunos foi de:", media)

# 5. # Alunos e suas notas representados através de dicionários
# alunos = [
# {
# "nome": "Alice",
# "nota": 8,
# },
# {
# "nome": "Bob",
# "nota": 7,
# },
# {
# "nome": "Carlos",
# "nota": 9,
# }
# ]
# Escreva uma programa que calcula a média das notas de todos os alunos.

# quantidade = len(alunos)
# soma = 0
# for i in alunos:
#     soma = soma + i["nota"]
#     media = soma / quantidade

# print("A média das notas dos alunos foi de:", media)

# 6.  DESAFIO. Escreva um programa que dado uma lista de números inteiros, imprime o maior número dessa lista.

# print("Digite números inteiros positivos! Irei te dizer qual foi o maior número digitado. Para encerrar o programa digite um número negativo!\n")

# i = 0
# lista = []
# while i >= 0:
#     i = int(input("Digite um número:\n"))
#     if i >= 0:
#         lista.append(i)
#         print("Número Registrado!\n")
#     else:
#         print("Finalizando o programa...")
#         break
    
# lista.sort()
# ultimo_numero = (len(lista) - 1)
# print(lista[ultimo_numero])

# 7. (ESSA DEMOROU MAIS DO QUE PRECISAVA)
# Exemplo
# for x in "abc":
#     print(x)
# Vai imprimir:
# a
# b
# c
# Escreva um programa que solicite uma string para o usuário e imprima quantas vezes cada letra aparece na palavra. Por exemplo:
# "banana"
# O resultado deve ser:
# {
# 'a': 3,
# 'b': 1,
# 'n': 2
# }

# texto = input("Digite uma palavra ou frase e contaremos quantas vezes cada letra aparece\t")

# Dicionário do alfabeto
# alfabetos ={'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0,
# 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}

# for b in texto.lower():
#     if ((b=='a') or (b=='A')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='b') or (b=='B')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='c') or (b=='C')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='d') or (b=='D')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='e') or (b=='E')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='f') or (b=='F')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='g') or (b=='G')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='g') or (b=='G')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='h') or (b=='H')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='i') or (b=='I')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='j') or (b=='J')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='k') or (b=='K')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='l') or (b=='L')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='m') or (b=='M')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='n') or (b=='N')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='o') or (b=='O')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='p') or (b=='P')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='q') or (b=='Q')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='r') or (b=='R')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='s') or (b=='S')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='t') or (b=='T')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='u') or (b=='U')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='v') or (b=='V')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='w') or (b=='W')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='x') or (b=='X')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='y') or (b=='Y')):
#         alfabetos[b]=alfabetos[b]+1
#     elif ((b=='z') or (b=='Z')):
#         alfabetos[b]=alfabetos[b]+1

# Variavel que contem as chaves e conteúdo do dicionario
# lista=list(alfabetos.items())

# Printando
# print(lista)

# 8. (Demorou mas deu certo também) 
# Escreva um programa que declara uma lista com elementos dediferentes tipos e imprime na tela essa lista invertida.
# Não é permitido utilizar métodos como reverse ou sort .

def inverte_lista(lista):
    tamanho = len(lista)
    nova_lista = []
    while tamanho > 0:
        tamanho = tamanho - 1
        nova_lista.append(lista[tamanho])
    print(nova_lista)
       
    
        
lista = ["a", 5, {1}]
lista_invertida = inverte_lista(lista)

# [{1}, 5, "a"]
#   0   1   2