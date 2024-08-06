# Assim como na matemática, conjuntos não tem ordem

usuarios = {"Vitor", "Aruana","Tesla"}
usuarios_2 = set(["Vitor", "Aruana","Younes"])

# print(usuarios.union(usuarios_2)) # Pode ser utilizado o pipe também | 

# EXEMPLO USO DO PIPE
# e_igual = usuarios.union(usuarios_2) == usuarios | usuarios_2
# print(e_igual)

# print(usuarios.intersection(usuarios_2))
# e_igual = usuarios.intersection(usuarios_2) == usuarios & usuarios_2   # INTERSEÇÃO É AQUILO QUE TEM EM COMUM NAS QUE FORAM COMPRADAS
# print(e_igual)

print(usuarios.difference(usuarios_2))
e_igual = usuarios.difference(usuarios_2) == usuarios - usuarios_2       # DIFERENÇA É O QUE TEM EM UM E NO OUTRO NÃO
print(e_igual)


# REMOVENDO DUPLICATAS
# usuarios = ["Vitor", "Aruana", "Vitor"]
# usuarios_unicos = set(usuarios)
# print(usuarios)
# print(usuarios_unicos)