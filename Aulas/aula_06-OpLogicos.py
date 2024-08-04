# Operadores Lógicos
# not
# and
# or


#not

idade = 16
maior_de_idade = idade >= 18
menor_de_idade = not maior_de_idade

print("Idade da pessoa:", idade)
print("Maior de idade:", maior_de_idade)
print("Menor de idade:", menor_de_idade)


# and

usuario_correto = True
senha_correta = False
sucesso = usuario_correto and senha_correta

print("Login bem sucedido:", sucesso)


# or

idade = 14
idade_minima = 16
acompanhada_pelos_pais = False
pode_assistir = idade >= idade_minima or acompanhada_pelos_pais

print("Pode assistir ao filme:", pode_assistir)

