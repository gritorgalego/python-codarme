# Condicionais (if/else/elif)

# 1. “FizzBuzz” é um problema clássico de programação. O programa recebe um
# número inteiro e imprime:
# a. “Fizz", caso o número seja múltiplo de 3.
# b. “Buzz", caso o número seja múltiplo de 5.
# c. “FizzBuzz", caso o número seja múltiplo de 3 e de 5.

# numero = int(input("Digite um número inteiro\n"))

# if numero % 3 == 0 and numero % 5 == 0:
#     print("FizzBuzz")
# elif numero % 3 == 0:
#     print("Fizz")
# elif numero % 5 == 0:
#     print("Buzz")
# else:
#     print("Não é divisível por 3 nem por 5")

# 2. Implemente uma calculadora que recebe 3 valores do usuário:
# a. Operando a (pode ser um inteiro ou float).
# b. Operando b (pode ser um inteiro ou float).
# c. Operador op .
# i. op pode ser uma string representando o operador, por exemplo, "+" ou "-
# ". Outra opção é utilizar números, por exemplo, 1 para soma , 2 para
# subtração , etc.
# O seu programa deve receber esses 3 valores e imprimir o resultado da operação.
# Caso o operador seja de divisão e o segundo operando seja o valor zero, o
# programa deve imprimir uma mensagem: “Não é possível realizar divisão por zero!”.

# print("Bem-vindo a sua calculadora!\n")
# n1 = float(input("Digite o primeiro operando:\n"))
# n2 = float(input("Digite o segundo operando\n"))
# operador = int(input("Digite a operação que deseja fazer:\n1 para soma\n2 para subtração\n3 para multiplicação\n4 para divisão:\n"))

# if operador == 4 and n2 == 0:
#     print("Não é possível realizar divisão por zero!")
# elif operador == 1:
#     print("O resultado é:", n1 + n2)
# elif operador == 2:
#     print("O resultado é:", n1 - n2)
# elif operador == 3:
#     print(n1*n2)
# elif operador == 4:
#     print(n1/n2)

# #3. Escreva um programa de autenticação que receba um nome de usuário e senha ( input ) e informe se:

# Autenticação foi bem-sucedida.
# Se o nome de usuário não existe.
# Se a senha está incorreta.

# USUARIO = "admin"
# SENHA = "1606"

# nome_usuario = input("Informe o seu nome de usuário:\n")
# senha_usuario = input("Informe a sua senha:\n")

# if nome_usuario != USUARIO:
#     print("O nome de usuário não existe")
# elif senha_usuario != SENHA:
#     print("A senha está incorreta")
# else:
#     print("Autenticação bem-sucedida")

# Repetição (while)

# 1. Escreva um programa que receba um número inteiro n e imprima a soma de todos os números de 1 até n (inclusive n).

# n = int(input("Digite um número inteiro qualquer e mostraremos a soma de todos os números de 1 até o número que foi informado (Incluindo ele mesmo):\n"))
# soma = 0
# i = 0
# while i < n:
#     i = i + 1
#     soma = soma + i 

# print("A soma de todos os números até o informado é:", soma)

# 2  Escreva um programa que receba um número inteiro n e imprima todos os números pares de 1 até n (inclusive n ).

# n = int(input("Digite um número inteiro qualquer e mostraremos a soma de todos os números pares de 1 até o número que foi informado (Incluindo ele mesmo):\n"))
# i = 0

# while i < n:
#     i = i + 2
#     print(i)

# 3. Escreva um programa que receba um número n e informe se esse número é primo ou não.
# Um número primo é um número que é divisível apenas por 1 e por ele mesmo.

# n = int(input("Digite um número e diremos se ele é primo ou não:\n"))
# i = 0 
# contador_divisoes = 0
# while i <= n:
#     i = i + 1
#     if n % i == 0:
#         contador_divisoes = contador_divisoes + 1
        
# if contador_divisoes == 2:
#     print("É primo!")
# else:
#     print("Não é primo!")

# 4.  O jogo “Acerte o número” funciona da seguinte maneira:
# a. Existe um certo número inteiro declarado dentro do programa que o usuário desconhece.  Por exemplo: numero = 8
# b. O usuário tem 3 tentativas para acertar o número.
# c. A cada tentativa, é informado ao usuário se o número que ele digitou é maior, menor, ou igual ao número correto.
# d. O jogo termina quando o usuário erra 3 vezes (perdeu) ou quando o usuário acerta o número (ganhou).

# print("Bem vindo ao jogo Acerte o número. Você tem 3 tentativas para advinhar um número de 1 a 10. Boa sorte!\n")
# n = 6
# tentativas = 0

# while tentativas < 3:
#     chute = int(input("Digite um número:\n"))
#     if chute == n:
#         print("Parabéns, você ganhou!")
#         break
#     elif chute < n:
#         print("Mais pra cima!\n")
#     elif chute > n:
#         print("Mais pra baixo!\n")
#     tentativas = tentativas + 1
    
# if tentativas == 3:
#     print("Acabaram suas tentativas! O número secreto era:", n)