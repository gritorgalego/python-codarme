from datetime import timedelta, datetime


class Tarefa:
    def __init__(self, titulo, descricao="", data=None, data_notificacao=None):
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.data_notificacao = data_notificacao
        self.concluida = False
        self.atraso = False

    def concluir(self):
        """
        Define essa tarefa como concluida.
        """
        self.concluida = True

    def adicionar_descricao(self, descricao):
        """
        Adiciona uma descrição para a tarefa.
        """
        self.descricao = descricao

    def adiar_notificacao(self, minutos):
        """
        Adia a notificação em uma certa quantidade de minutos.

        Notificacao: 25/02/2022, 14h30
        adiar_notificacao(15)
        => Notificacao 25/02/2022 14h45
        """
        if self.data_notificacao is None:
            return
        self.data_notificacao = self.data_notificacao + timedelta(minutes=minutos)

    def atrasada(self):
        """
        Diz se a tarefa está atrasada. Ou seja, data < hoje.
        """
        if self.data and not self.concluida:
            return datetime.now() > self.data
        return False
