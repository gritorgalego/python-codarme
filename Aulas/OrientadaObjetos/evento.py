class Evento:
    def __init__(self, nome, local=""):
        self.nome = nome
        self.local = local

    def imprime_informacoes(self):
        print("Nome do evento:", self.nome)
        print("Local do evento:", self.local)
        
    @classmethod
    def cria_evento_online(cls, nome):
        evento = cls(nome, local="https://tamarcado.com/eventos?id=1")
        return evento
    
    @staticmethod
    def calcula_limite_pessoas_area(area):
        if 5 <= area < 10:
            return 5
        elif 10 <= area < 20:
            return 15
        elif area >= 20:
            return 30
        else:
            return 0
        
        
# ev = Evento("Aula de Python")
# ev2 = Evento("Aula de JavaScript", "Santa Catarina")

# ev_online = Evento.cria_evento_online("Live de Python")
# ev_online.imprime_informacoes()

print(Evento.calcula_limite_pessoas_area(20))