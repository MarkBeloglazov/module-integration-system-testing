"""
calculator.py - реализация базового консольного калькулятора

Содержит базовые арифметические операции и функцию запуска интерфейса
"""

def add(a, b):
    """
    Сложение двух чисел.

    Аргументы:
        a (float): первое слагаемое
        b (float): второе слагаемое

    Возвращает:
        (float): сумма a и b
    """
    return a + b

def subtract(a, b):
    """
    Вычитание второго числа из первого

    Аргументы:
        a (float): уменьшаемое
        b (float): вычитаемое

    Возвращает:
        (float): разность a и b
    """
    return a - b

def multiply(a, b):
    """
    Умножение двух чисел.

    Аргументы:
        a (float): первый множитель
        b (float): второй множитель

    Возвращает:
        (float): произведение a и b
    """
    return a * b

def divide(a, b):
    """
    Деление первого числа на второе.

    Аргументы:
        a (float): делимое
        b (float): делитель

    Возвращает:
        (float): частное a и b

    Выдаёт:
        ValueError: если b равно 0 (деление на ноль)
    """
    if b == 0:
        raise ValueError("Нет решений при делении на ноль")
    return a / b

def main():
    """
    Основная функция - запускает консольный интерфейс калькулятора.
    Позволяет пользователю вводить операции и получать результаты.
    """
    print("Базовый калькулятор. Доступные операции: '+', '-', '*', '/'")
    print("Для выхода введите 'quit'")

    while True:
        try:
            user_input = input("\nВведите выражение: ").strip()

            # Проверка на выход
            if user_input.lower() == 'quit':
                print("Выход.")
                break

            parts = user_input.split()
            if len(parts) != 3:
                print("Ошибка: должно быть три аргумента: первое число, операция и второе число.")
                print("Выражения без пробелов не поддерживаются.")
                print("Чтобы выйти, введите quit.")
                continue

            num1 = float(parts[0])
            operation = parts[1]
            num2 = float(parts[2])

            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            else:
                print(f"Ошибка: операция '{operation}' не поддерживается")
                continue
            
            print(f"Результат: {num1} {operation} {num2} = {result}")

        except ValueError as e:
            if "could not convert!" in str(e):
                print("Ошибка: введите корректные числа")
            else:
                print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Исключение: {e}")

if __name__ == "__main__":
    main()
