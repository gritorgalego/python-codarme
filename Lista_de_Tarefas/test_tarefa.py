from datetime import datetime, timedelta
import unittest
from tarefa import Tarefa


class TestConcluir(unittest.TestCase):
    def test_concluir_tarefa_altera_concluido_para_true(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)

    def test_concluir_tarefa_concluida_mantem_concluida_como_true(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)


class TestDescricao(unittest.TestCase):
    def test_adicionar_descricao_para_tarefa(self):
        descricao_tarefa = Tarefa(titulo="Estudar Python na Codarme")
        descricao_esperada = "Estudar ao menos 1 hora e fazer exercícios"
        descricao_tarefa.adicionar_descricao(descricao_esperada)
        self.assertEqual(descricao_tarefa.descricao, descricao_esperada)


class TestAdiarNotificacao(unittest.TestCase):
    def test_adia_notificacao_em_N_minutos(self):
        dt_original = datetime(2024, 6, 16, 12, 40)
        tarefa = Tarefa("Estudar Python", data_notificacao=dt_original)
        minutos_adiados = 15
        tarefa.adiar_notificacao(minutos_adiados)
        dt_esperado = dt_original + timedelta(minutes=minutos_adiados)
        self.assertEqual(tarefa.data_notificacao, dt_esperado)


unittest.main()
