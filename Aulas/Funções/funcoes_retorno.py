def calcular_conta(consumo, taxa_servico=0.1, desconto_fidelidade=0):  # É possível definir um valor padrão para os argumentos, assim só é necessário digitar caso exista alguma exceção
    if taxa_servico == 0 and desconto_fidelidade == 0:
        return consumo

    servico = consumo * taxa_servico
    desconto = consumo * desconto_fidelidade
    valor = consumo + servico
    valor = valor - desconto
    return valor


print(calcular_conta(consumo=100))
