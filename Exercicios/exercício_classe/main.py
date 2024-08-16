from usuario import Usuario
from administrador import Administrador

user = Usuario("Vitor", "Vitor@exemplo.com")
admin = Administrador("Admin", "admin@exemplo.com")
user.imprime_usuario()
admin.imprime_usuario()
print(Usuario.quantidade)
