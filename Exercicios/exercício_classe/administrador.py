from usuario import Usuario

class Administrador(Usuario):
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        Usuario.quantidade += 1
    
    def imprime_usuario(self):
        print(f"{self.nome}({self.email}) - Administrador")
        