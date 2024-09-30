from datetime import datetime, timedelta
import unittest
from tarefa import Tarefa
from lista_de_tarefas import ListaDeTarefas


class TestAdicionarTarefa(unittest.TestCase):
    def test_adiciona_tarefa_a_lista_de_tarefas(self):
        tarefa = Tarefa("Tarefa Teste")
        lista = ListaDeTarefas()

        lista.adicionar_tarefa(tarefa)

        self.assertEqual(lista.get_tarefas()[0], tarefa)


class TestGetTarefa(unittest.TestCase):
    def test_retorna_lista_de_tarefas_adicionadas(self):
        tarefa_um = Tarefa("Tarefa Teste 1")
        tarefa_dois = Tarefa("Tarefa Teste 2")
        lista = ListaDeTarefas()
        lista.adicionar_tarefa(tarefa_um)
        lista.adicionar_tarefa(tarefa_dois)
        self.assertEqual(lista.get_tarefas(), [tarefa_um, tarefa_dois])


class TestAtrasoTarefa(unittest.TestCase):
    def test_retorna_lista_de_tarefas_atrasadas(self):
        tarefa_atrasada = Tarefa(
            "Tarefa Atrasada",
            data=datetime.now() - timedelta(days=1),
        )
        tarefa_nao_atrasada = Tarefa(
            "Tarefa Não Atrasada", data=datetime.now() + timedelta(days=1)
        )
        lista = ListaDeTarefas()
        lista.adicionar_tarefa(tarefa_atrasada)
        lista.adicionar_tarefa(tarefa_nao_atrasada)
        self.assertEqual(lista.get_tarefas_atrasadas(), [tarefa_atrasada])


class TestTarefasHoje(unittest.TestCase):
    def test_retorna_lista_de_tarefas_para_hoje(self):
        tarefa_hoje = Tarefa("Tarefa para Hoje", data=datetime.now())
        tarefa_futura = Tarefa("Tarefa Futura", data=datetime.now() + timedelta(days=1))
        lista = ListaDeTarefas()
        lista.adicionar_tarefa(tarefa_hoje)
        lista.adicionar_tarefa(tarefa_futura)

        self.assertEqual(lista.get_tarefas_para_hoje(), [tarefa_hoje])


unittest.main()
