import unittest
from Calculadora import Calculadora, ErrorAlDividirEntreZero


class MyTestCase(unittest.TestCase):
    def test_sumar_2_y_2_regresa_4(self):
        calculadora = Calculadora()
        resultado = calculadora.sumar(2, 2)
        self.assertEqual(resultado, 4)

    def test_sumar_3_y_5_regresa_8(self):
        calculadora = Calculadora()
        resultado = calculadora.sumar(3, 5)
        self.assertEqual(resultado, 8)

    def test_restar_8_y_2_regresa_6(self):
        calculadora = Calculadora()
        resultado = calculadora.restar(8, 2)
        self.assertEqual(resultado, 6)

    def test_restar_5_y_5_regresa_0(self):
        calculadora = Calculadora()
        resultado = calculadora.restar(5, 5)
        self.assertEqual(resultado, 0)

    def test_dividir_10_y_0_regresa_mensaje_error(self):
        calculadora = Calculadora()
        with self.assertRaises(ErrorAlDividirEntreZero):
            resultado = calculadora.dividir(10, 0)

    def test_dividir_5_y_5_regresa_1(self):
        calculadora = Calculadora()
        resultado = calculadora.dividir(5, 5)
        self.assertEqual(resultado, 1)


if __name__ == '__main__':
    unittest.main()
