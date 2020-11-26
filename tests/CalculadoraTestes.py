import unittest
from pyunitreport import HTMLTestRunner
from pageobjects.Calc import Calculator
from webdriver.Webdriver import Driver


class CalculadoraTestes(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = Driver()

    def test_soma(self):
        calculadora = Calculator(self.driver)
        calculadora.somando(1, 2)

    def test_subtracao(self):
        calculadora = Calculator(self.driver)
        calculadora.subtraindo(3, 2)

    def test_multiplicacao(self):
        calculadora = Calculator(self.driver)
        calculadora.multiplicando(4, 5)

    def test_divisao(self):
        calculadora = Calculator(self.driver)
        calculadora.dividindo(8, 4)

    @classmethod
    def tearDown(self):
        self.driver.instance.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='..\\reports'))
