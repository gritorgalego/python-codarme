# {key: value}

# Vitor = {
#     "nome": "Vitor",
#     "idade": 20,
#     "admin": True
# }

# Aruana = {
#     "nome": "Aruana",
#     "idade": 21,
#     "admin": False
# }

# print(Vitor["admin"])
# print(Aruana["admin"])

Vitor = {
    "Nome": "Vitor",
    "Endereço": {
        "Rua": "Rendeiras",
        "Número": 1606
    } 
}

Aruana = {
    "Nome": "Aruana",
    "Endereço": {
        "Rua": "Cavalo Marinho",
        "Número": 1704 
    }
}

print(Vitor["Nome"])
print(Vitor["Endereço"])
print(Vitor["Endereço"]["Número"])