def dar_boas_vindas(nome, sobrenome, nome_curso):
    print("Olá, me chamo", nome, sobrenome, "!")
    print("Bem-vindo ao meu repositório de", nome_curso,"!")
    
# dar_boas_vindas("Vitor", "Galego" ,"Python") Aqui a posição importa
# dar_boas_vindas(nome="Vitor", sobrenome="Galego" ,nome_curso="Python") # Aqui a posição não importa. São os chamados keyword arguments. Usar em todos ou deixar no final para dar certo

# def soma():
#     ...
    
# soma(10, 5)

def calcular_conta(consumo, taxa_servico, desconto_fidelidade):
    servico = consumo * taxa_servico 
    desconto = consumo * desconto_fidelidade 
    valor = consumo + servico 
    valor = valor - desconto
    return valor
    
valor = calcular_conta(consumo=200, taxa_servico=0.1, desconto_fidelidade=0.05)
print("O valor a ser pago é de R$", valor)

"""
consumo = 100
serviço = consumo * taxa_servico # 10
desconto = consumo * desconto_fidelidade # 5

valor = consumo + servico # 100 + 10 = 110
valor = valor - desconto # 110 - 5 

=> 105
"""

