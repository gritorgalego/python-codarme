from django.db import models


# Create your models here.
class Evento:
    def __init__(self, nome, categoria, local=None, link=None):
        self.nome = nome
        self.categoria = categoria
        self.local = local
        self.link = link


aula_python = Evento("Aula de Python", "Backend", "Santa Catarina")
aula_js = Evento("Aula de JavaScript", "Fullstack", link="https://tamarcado.com")
eventos = [aula_python, aula_js]
