@echo off
REM Очистка предыдущих сборок
if exist dist\ rmdir /s /q dist
if exist build\ rmdir /s /q build
if exist calculator.spec del /f /q calculator.spec

REM Сборка
pyinstaller --onefile src\calculator.py

REM Проверка результата
if exist dist\calculator.exe (
    echo Сборка завершена: dist\calculator.exe
) else (
    echo Ошибка сборки!
    exit /b 1
)

REM Пауза, чтобы пользователь увидел результат (опционально)
pause

