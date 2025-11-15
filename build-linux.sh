#!/bin/sh
# Очистка предыдущих сборок
rm -rf dist/ build/ calculator.spec

# Сборка
pyinstaller --onefile src/calculator.py


# Проверка результата
if [ -f "dist/calculator" ]; then
    echo "Сборка завершена: dist/calculator"
else
    echo "Ошибка сборки!"
fi

