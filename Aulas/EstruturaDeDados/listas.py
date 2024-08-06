# notas = [8, 10, 8.5] # O primeiro item da lista tem o índice 0. Listas tem estrutura de dados ordenada
# notas.append(9)
# notas.sort(reverse=True) # Decrescente
# print(notas)

# x = notas.pop()
# print(notas)
# print("X ->", x)

# notas.insert(0, 12)
# print("Após inserção: ")
# print(notas)

# notas.pop(0)
# print(notas)

# pessoa = ["Vitor", 20, "1606"]

# print("Meu nome é:", pessoa[0])
# print("Minha idade é:", pessoa[1])

# pessoas = [
#     ["Vitor", 20],
#     ["Aruana", 21]
    
# ]

notas = [8, 9, 10, 7.5, 4, 6]

i = 0
total = 0
qtd = len(notas)

while i < qtd:
    total = total + notas[i]
    i = i + 1
    
print("O total das notas é: ", total)

media = total / qtd
print("A média das notas é:", media)
    