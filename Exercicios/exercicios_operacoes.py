#1. Escreva um programa que receba um número inteiro do usuário e imprima True caso o número seja par e False, caso o número seja ímpar

numero = input("Digite um número e te direi se é par ou ímpar:\n")
numero = int(numero)
par = numero % 2 == 0
impar = numero % 2 == 1

print("Seu número é par", par)
print("Seu número é ímpar", impar)


#2. O que vai ser impresso na tela ao executar o programa abaixo? (são 2 prints !) - R: True e False

a = 10
b = 5
x = True
y = False

print((x or y) and (a < b))
print((x or y) and not (a < b))

#3. Considere o programa abaixo

# resultado = 2 + 3 * 2 ** 2
# print(resultado)

# Utilize parênteses de modo que o programa imprima os seguintes resultados:

# 14
resultado = 2 + 3 * (2 ** 2)
print(resultado)

# 38
resultado = 2 + (3 * 2) ** 2
print(resultado)


# 100
resultado = ((2 + 3) * 2) ** 2
print(resultado)

#4. Alice é responsável por escrever um programa que verifica se um cupom dedesconto pode ser utilizado. 
#    O programa recebe 3 valores e retorna True caso o cupom possa ser utilizado, ou False , caso contrário.
#    Os três valores que o programa recebe são:
#        1. Valor de compra (float)
#        2. Valor do frete (float)
#        3. Cliente é cadastrado no programa de fidelidade (string “s” (sim) ou “n” (não))
#    O cupom tem a seguinte regra:
#    Caso o valor da compra somado ao frete seja superior a R$ 100, ou o cliente seja cadastrado no programa de fidelidade, o cupom de desconto pode ser utilizado. 
#    Caso contrário, o cupom não pode ser utilizado.

valor_compra = input("Insira o valor da compra:\n")
valor_compra = float(valor_compra)
valor_frete = input("Insira o valor do frete:\n")
valor_frete = float(valor_frete)
fidelidade = input("Digite s para sim ou n para não:\n")
cupom = valor_frete + valor_compra > 100.0 or fidelidade == "s"

print("O cliente está apto a usar o cupom de desconto?\n", cupom)
