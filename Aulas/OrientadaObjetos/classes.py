class Evento:
    def __init__(self, nome):  #Construtor
        self.nome = nome
        self.local = "Brasil"
    
    def altera_nome_evento(self, novo_nome):
        print("Alterando nome do evento")
        self.nome = novo_nome

ev = Evento("Aula de Python") #... Evento.__init__()
ev2 = Evento("Aula de JavaScript")

print(ev.nome)
print(ev2.nome) 
