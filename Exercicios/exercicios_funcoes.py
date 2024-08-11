# 1. Escreva uma função que recebe um número inteiro positivo e retorna True caso ele seja primo e False , caso contrário.

# def e_primo(numero):
#     i = 0
#     contador_divisoes = 0
#     while i <= numero:
#         i = i + 1
#         if numero % i == 0:
#             contador_divisoes = contador_divisoes + 1

#     if contador_divisoes == 2:
#             return True
#     else:
#             return False
# resposta = e_primo(1559)
# print(resposta)

# 2. Implemente uma função que recebe uma lista de números inteiros e retorna uma tupla (pos, num) , onde pos é a posição (ou índice) do maior número na lista e num é o valor desse número.

# def maior_numero(lista):
#     maior_da_lista = max(lista)
#     pos_maior_da_lista = lista.index(maior_da_lista)
#     tupla_maior_numero = (pos_maior_da_lista, maior_da_lista)
#     print(tupla_maior_numero)
# lista_numeros = [15, 250, 520, 3451320, 2345022435, 523045 ,540 ,54]
# maior_numero(lista_numeros)

# 3. Implemente uma função maior_idade(pessoa) que receba uma tupla representando uma pessoa com nome e idade e imprime na tela se a pessoa é maior de idade ou não.

# def maior_idade(pessoa):
#     if idade >= 18:
#         print(nome, "é maior de idade!")
#     else:
#         print(nome, "é menor de idade!")
# dados_pessoa = ("João", 18)
# nome, idade = dados_pessoa
# maior_idade(dados_pessoa)

# 4. Adapte a função maior_idade(pessoa) de forma que ela possa receber tanto uma tupla quanto um dicionário. Dica: método type pode te ajudar.

# def maior_idade(pessoa):
#     tupla_teste = ()
#     dict_teste = {}
#     if type(dados_pessoa) == type(tupla_teste):
#         if idade >= 18:
#             print(nome, "é maior de idade!")
#         else:
#             print(nome, "é menor de idade!")
#     if type(dados_pessoa) == type(dict_teste):
#         if dados_pessoa["idade"] >= 18:
#             print(dados_pessoa["nome"], "é maior de idade!")
#         else:
#             print(dados_pessoa["nome"], "é menor de idade!")
# dados_pessoa = {'idade': 20, 'nome': "Vitor"}
# nome, idade = dados_pessoa
# maior_idade(dados_pessoa)

# 5. Implemente uma função que recebe dois argumentos, uma lista e um elemento , e retorna True caso elemento seja encontrado na lista , e False caso contrário. 
# Não é permitido utilizar o método in

# def comparador(lista_recebida, elemento_recebido):
#     i = 0
#     contador = 0
#     while i < len(lista):
#         if lista[i] == elemento:
#             contador = contador + 1
#         i = i + 1
    
#     if contador >= 1:
#         return True
#     else:
#         return False
        
# lista = ["Vitor", 20, "Kobrasol"]
# elemento = 20
# print(comparador(lista, elemento))

# 6.  DESAFIO. Uma função fatorial calcula o valor da multiplicação de um certo número inteiro não-negativo por todos os números positivos menores que ele.
# A exceção é o fatorial de zero que é igual a 1. Por exemplo:
'''
fatorial(3) = 3 * 2 * 1 = 6
fatorial(1) = 1
fatorial(0) = 1

'''
# Ou seja, podemos definir a função fatorial como:
# Exercícios – Funções 2
# fatorial(n) = n * n-1 * n-2 * ... * 1
# Implemente a função fatorial(n) de modo que ela retorne o valor do fatorial de n.

# def fatorial(numero_fatorial):
#     i = 2
#     total = 1
#     while i <= numero_fatorial:
#         total = total * i
#         i = i + 1
#     return total
        
# numero = fatorial(10)
# print(numero)