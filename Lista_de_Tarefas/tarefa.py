class Tarefa:
    def __init__(
        self, titulo, descricao="", data=None, notificacao=None, concluida=False
    ):
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.notificacao = notificacao
        self.concluida = False

    def concluir(self):
        """
        Define essa tarefa como concluida.
        """
        self.concluida = True

    def adicionar_descricao(self, descricao):
        """
        Adiciona uma descrição para a tarefa.
        """

    def adiar_notificacao(self, minutos):
        """
        Adia a notificação em uma certa quantidade de minutos.
        """

    def atrasada(self):
        """
        Diz se a tarefa está atrasada. Ou seja, data < hoje.
        """
