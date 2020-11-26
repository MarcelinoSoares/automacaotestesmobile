from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from tests import CalculadoraTestes

calculadora_tests = TestLoader().loadTestsFromTestCase(CalculadoraTestes)

suite = TestSuite([calculadora_tests])
kwargs = {
    "output": reports,
    "report_name": resultados,
    "failfast": True
}
runner = HTMLTestRunner(**kwargs)
runner.run(suite)