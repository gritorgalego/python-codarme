class Evento:
    def metodo_instancia(self):
        return("Método de instância chamado", self)
    
    @classmethod
    def metodo_classe(cls):
        return("Método de classe chamado", cls)
    
    @staticmethod
    def metodo_estatico():
        return "Método estático chamado"
    
ev = Evento()
a = ev.metodo_estatico()
print(a)

# a = ev.metodo_instancia() # Evento.metodo_instancia(ev)
# print(a)

# b = Evento.metodo_classe() # Evento.metodo_classe(Evento)
# print(b)

# c = Evento.metodo_estatico() #Evento.metodo_estatico()
# print(c)