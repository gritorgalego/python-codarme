from calculadora import somar, dividir, multiplicar, subtrair
import unittest


class TestSomar(unittest.TestCase):
    def test_soma_de_dois_numeros_inteiros(self):
        self.assertEqual(somar(2, 4), 6)

    def test_soma_de_numero_com_zero(self):
        self.assertEqual(somar(2, 0), 2)


class TestDividir(unittest.TestCase):
    def test_divide_numero_por_1_retorna_o_numero(self):
        self.assertEqual(dividir(10, 1), 10)

    def test_divide_numero_por_zero(self):
        self.assertEqual(dividir(10, 0), "Não é um número")


class TestMultiplicar(unittest.TestCase):
    def test_multiplica_numero_por_1(self):
        self.assertEqual(multiplicar(3, 1), 3)

    def test_multiplica_numero_por_zero(self):
        self.assertEqual(multiplicar(50, 0), 0)

    def test_multiplica_numeros_decimais(self):
        self.assertEqual(multiplicar(2, 2.5), 5)

    def test_ordem_dos_fatores(self):
        self.assertEqual(multiplicar(2, 3), (3 * 2))


class TestSubtrair(unittest.TestCase):
    def test_subtrair_positivo_com_negativo(self):
        self.assertEqual(subtrair(2, -2), 4)

    def test_subtrair_por_zero(self):
        self.assertEqual(subtrair(5, 0), 5)


unittest.main()
