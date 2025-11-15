"""
test_calculator_integration.py - интеграционные тесты

Проверяет взаимодействия между функциями калькулятора,
корректность передачи данных и последовательное выполнение операций.
"""
import unittest
from src.calculator import add, subtract, multiply, divide

class TestCalculatorIntegration(unittest.TestCase):
    """Набор интеграционных тестов для проверки взаимодействия функций калькулятора."""

    def test_chain_operations_add_multiply(self):
        """Сложение-умножение"""
        intermediate = add(2, 3)
        result = multiply(intermediate, 4)
        self.assertEqual(result, 20)

    def test_chain_operations_subtract_divide(self):
        """Вычитание-деление"""
        intermediate = subtract(10, 4)
        result = divide(intermediate, 2)
        self.assertEqual(result, 3)

    def test_complex_chain_all_operations(self):
        """Все операции"""
        step1 = add(5, 3)
        step2 = multiply(step1, 2)
        step3 = subtract(step2, 4)
        result = divide(step3, 3)
        self.assertEqual(result, 4)

    def test_negative_intermediate_results(self):
        """Отрицательные промежуточные результаты"""
        step1 = subtract(2, 5)
        result = multiply(step1, 4)
        self.assertEqual(result, -12)

    def test_error_in_chain_operations(self):
        """Ноль в цепи операций"""
        step1 = add(5, 0)
        step2 = multiply(step1, 0)
        result = add(step2, 10)
        self.assertEqual(result, 10)

    def test_error_propagation_division_by_zero(self):
        """Распространение ошибки деления на ноль в цепи"""
        intermediate = subtract(10, 2)

        with self.assertRaises(ValueError) as context:
            divide(intermediate, 0)

        self.assertEqual(str(context.exception), "Нет решений при делении на ноль")

    def test_mixed_signs_in_chain(self):
        """Цепь с числами разных знаков"""
        step1 = add(-4, 6)
        step2 = multiply(step1, -3)
        result = subtract(step2, -2)
        self.assertEqual(result, -4)

    def test_float_operations_chain(self):
        """Цепь с дробными числами"""
        step1 = add(2.5, 1.5)
        step2 = multiply(step1, 0.5)
        result = divide(step2, 4.0)
        self.assertAlmostEqual(result, 0.5, places=7)

    def test_large_numbers_chain(self):
        """Цепь с большими числами"""
        step1 = add(1000000, 2000000)
        step2 = multiply(step1, 3)
        result = subtract(step2, 1000000)
        self.assertEqual(result, 8000000)

if __name__ == '__main__':
    unittest.main()
