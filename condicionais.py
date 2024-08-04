idade = input("Digite a sua idade:\n")
idade = int(idade)

if idade > 120:
    print("Caso ninguém tenha te contado, você é um ser místico!")
elif idade >= 100:
    print("Sua hora está chegando...")
elif idade >= 18:
    print("Você é um adulto")
elif idade >=12:
    print("Você é um adolescente")
else:
    print("Você é uma criança")
    
# Truthy  ->  Qualquer número que não seja zero. Porém, a string "0", é True
# Falsy   ->  0, "", None