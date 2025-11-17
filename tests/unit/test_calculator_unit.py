"""
test_calculator_unit.py - модульные тесты

Проверяет корректность работы отдельных функций (add, subtract, multiply, divide) в изоляции.
"""

import unittest
from src.calculator import add, subtract, multiply, divide

class TestCalculatorUnit(unittest.TestCase):
    """Набор модульных тестов для базовых арифметических операций."""

    def test_add_positive_numbers(self):
        """Сложение положительных чисел"""
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(4, 5), 9)

    def test_add_negative_numbers(self):
        """Сложение отрицательных чисел"""
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(-4, -5), -9)
    
    def test_add_mixed_numbers(self):
        """Сложение чисел с разными знаками"""
        self.assertEqual(add(-1, 2), 1)
        self.assertEqual(add(3, -5), -2)
    
    def test_add_with_zero(self):
        """Сложение с нулём"""
        self.assertEqual(add(0, 1), 1)
        self.assertEqual(add(2, 0), 2)
        self.assertEqual(add(0, -1), -1)
        self.assertEqual(add(-2, 0), -2)
        self.assertEqual(add(0, 0), 0)

    def test_subtract_positive_numbers(self):
        """Вычитание положительных чисел"""
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(9, 5), 4)
        
    def test_subtract_negative_numbers(self):
        """Вычитание отрицательных чисел"""
        self.assertEqual(subtract(-3, -2), -1)
        self.assertEqual(subtract(-9, -5), -4)

    def test_subtract_mixed_numbers(self):
        """Вычитание чисел с разными знаками"""
        self.assertEqual(subtract(1, -2), 3)
        self.assertEqual(subtract(-1, 2), -3)

    def test_subtract_with_zero(self):
        """Вычитание с нулём"""
        self.assertEqual(subtract(0, 1), -1)
        self.assertEqual(subtract(2, 0), 2)
        self.assertEqual(subtract(0, -1), 1)
        self.assertEqual(subtract(-2, 0), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply_positive_numbers(self):
        """Умножение положительных чисел"""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(4, 5), 20)


    def test_multiply_negative_numbers(self):
        """Умножение отрицательных чисел"""
        self.assertEqual(multiply(-1, -2), 2)
        self.assertEqual(multiply(-3, -4), 12)

    def test_multiply_mixed_numbers(self):
        """Умножение чисел с разными знаками"""
        self.assertEqual(multiply(-1, 2), -2)
        self.assertEqual(multiply(-3, 4), -12)

    def test_multiply_with_zero(self):
        """Умножение на ноль"""
        self.assertEqual(multiply(1, 0), 0)
        self.assertEqual(multiply(0, 2), 0)
        self.assertEqual(multiply(-1, 0), 0)
        self.assertEqual(multiply(0, -2), 0)
        self.assertEqual(multiply(0, 0), 0)

    def test_divide_positive_numbers(self):
        """Деление положительных чисел"""
        self.assertEqual(divide(2, 1), 2)
        self.assertEqual(divide(10, 5), 2)

    def test_divide_negative_numbers(self):
        """Деление отрицательных чисел"""
        self.assertEqual(divide(-2, -1), 2)
        self.assertEqual(divide(-10, -5), 2)

    def test_divide_mixed_numbers(self):
        """Деление чисел с разными знаками"""
        self.assertEqual(divide(-6, 3), -2)
        self.assertEqual(divide(6, -3), -2)

    def test_divide_by_one(self):
        """Деление на единицу"""
        self.assertEqual(divide(2, 1), 2)
        self.assertEqual(divide(-2, 1), -2)

    def test_divide_with_remainder(self):
        """Деление с остатком"""
        self.assertAlmostEqual(divide(7, 3), 7/3, places=7)
        self.assertAlmostEqual(divide(1, 4), 0.25, places=7)

    def test_divide_by_zero(self):
        """Деление на ноль"""
        with self.assertRaises(ValueError) as context:
            divide(1, 0)
        self.assertEqual(str(context.exception), "Нет решений при делении на ноль")

        with self.assertRaises(ValueError):
            divide(-1, 0)

    def test_divide_zero_by_number(self):
        """Деление нуля на число"""
        self.assertEqual(divide(0, 2), 0)
        self.assertEqual(divide(0, -2), 0)

if __name__ == '__main__':
    unittest.main()
