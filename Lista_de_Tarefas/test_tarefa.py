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


class TestTarefaAtrasada(unittest.TestCase):
    def test_tarefa_atrasada(self):
        data_passada = datetime.now() - timedelta(days=1)
        tarefa = Tarefa(titulo="Tarefa atrasada", data=data_passada)
        self.assertTrue(tarefa.atrasada())

    def test_tarefa_nao_atrasada(self):
        data_futura = datetime.now() + timedelta(days=1)
        tarefa = Tarefa(titulo="Tarefa no prazo", data=data_futura)
        self.assertFalse(tarefa.atrasada())

    def test_tarefa_concluida_nao_atrasada(self):
        data_passada = datetime.now() - timedelta(days=1)
        tarefa = Tarefa(titulo="Tarefa concluída", data=data_passada)
        tarefa.concluida = True
        self.assertFalse(tarefa.atrasada())


unittest.main()
