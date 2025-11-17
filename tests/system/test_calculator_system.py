"""
test_calculator_system.py - системные тесты

Проверяет работу всей программы
"""

import unittest
import io
import sys
from unittest.mock import patch
from src.calculator import main

class TestCalculatorSystem(unittest.TestCase):
    """Набор системных тестов для проверки работы калькулятора как единого приложения."""


    @patch('builtins.input', side_effect=['5 + 3', 'quit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_basic_operation_and_exit(self, mock_stdout, mock_input):
        """Проверка выполнения простой операции и выхода."""
        main()
        output = mock_stdout.getvalue()

        self.assertIn("Базовый калькулятор. Доступные операции: '+', '-', '*', '/'", output)
        self.assertIn("Для выхода введите 'quit'", output)
        self.assertIn("Результат: 5.0 + 3.0 = 8.0", output)
        self.assertIn("Выход.", output)


    @patch('builtins.input', side_effect=['10 - 4', '2 * 6', 'quit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_multiple_operations(self, mock_stdout, mock_input):
        """Проверка последовательного выполнения нескольких операций."""
        main()
        output = mock_stdout.getvalue()

        self.assertIn("Результат: 10.0 - 4.0 = 6.0", output)
        self.assertIn("Результат: 2.0 * 6.0 = 12.0", output)


    @patch('builtins.input', side_effect=['invalid input', '5 / 0', 'quit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_error_handling(self, mock_stdout, mock_input):
        """Проверка обработки некорректного ввода и деления на ноль."""
        main()
        output = mock_stdout.getvalue()


        self.assertIn("Ошибка: должно быть три аргумента: первое число, операция и второе число.", output)
        self.assertIn("Выражения без пробелов не поддерживаются.", output)
        self.assertIn("Чтобы выйти, введите quit.", output)
        self.assertIn("Ошибка: Нет решений при делении на ноль", output)


    @patch('builtins.input', side_effect=['3.5 + 2.7', 'quit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_float_operations(self, mock_stdout, mock_input):
        """Проверка работы с дробными числами."""
        main()
        output = mock_stdout.getvalue()

        self.assertIn("Результат: 3.5 + 2.7 = 6.2", output)

    @patch('builtins.input', side_effect=['-5 * -3', '10 / -2', 'quit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_negative_numbers(self, mock_stdout, mock_input):
        """Проверка работы с отрицательными числами."""
        main()
        output = mock_stdout.getvalue()


        self.assertIn("Результат: -5.0 * -3.0 = 15.0", output)
        self.assertIn("Результат: 10.0 / -2.0 = -5.0", output)


    @patch('builtins.input', side_effect=['   8   +   2   ', 'quit'])  # пробелы вокруг
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_whitespace_tolerance(self, mock_stdout, mock_input):
        """Проверка устойчивости к лишним пробелам во вводе."""
        main()
        output = mock_stdout.getvalue()


        self.assertIn("Результат: 8.0 + 2.0 = 10.0", output)


    @patch('builtins.input', side_effect=['quit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_immediate_exit(self, mock_stdout, mock_input):
        """Проверка немедленного выхода без операций."""
        main()
        output = mock_stdout.getvalue()


        self.assertIn("Базовый калькулятор. Доступные операции: '+', '-', '*', '/'", output)
        self.assertIn("Для выхода введите 'quit'", output)
        self.assertIn("Выход.", output)

        # Убедимся, что нет лишних сообщений об ошибках до выхода
        self.assertNotIn("Ошибка", output.split("Выход.")[0])


    @patch('builtins.input', side_effect=['5 ? 3', 'quit'])  # неизвестный оператор
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_unknown_operator(self, mock_stdout, mock_input):
        """Проверка обработки неизвестного оператора."""
        main()
        output = mock_stdout.getvalue()

        self.assertIn("Ошибка: операция '?' не поддерживается", output)


    @patch('builtins.input', side_effect=['abc + def', 'quit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_non_numeric_input(self, mock_stdout, mock_input):
        """Проверка обработки нечислового ввода."""
        main()
        output = mock_stdout.getvalue()

        self.assertIn("Ошибка: could not convert string to float: 'abc'", output)

    @patch('builtins.input', side_effect=['', 'quit'])  # пустой ввод
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_empty_input(self, mock_stdout, mock_input):
        """Проверка обработки пустого ввода."""
        main()
        output = mock_stdout.getvalue()

        self.assertIn("Ошибка: должно быть три аргумента: первое число, операция и второе число.", output)
        self.assertIn("Выражения без пробелов не поддерживаются.", output)



if __name__ == '__main__':
    unittest.main()
