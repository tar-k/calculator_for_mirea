#!/bin/bash

# Проверка ввода параметров
if [ -z "$1" ]; then
    echo "Не указан первый параметр: URL репозитория GitHub."
    exit 1
fi

if [ -z "$2" ]; then
    echo "Не указан второй параметр: версия проекта."
    exit 1
fi

# Параметры
GIT_URL=$1
VERSION=$2
PROJECT_NAME=$(basename "$GIT_URL" .git)
WORK_DIR="/tmp/$PROJECT_NAME"

# Вывод параметров для отладки
echo "URL репозитория: $GIT_URL"
echo "Версия проекта: $VERSION"
echo "Рабочая директория: $WORK_DIR"

# Шаг 1. Загрузка актуального состояния с GitHub
if [ ! -d "$WORK_DIR" ]; then
    echo "Клонирование репозитория..."
    git clone "$GIT_URL" "$WORK_DIR" || { echo "Ошибка при клонировании репозитория!"; exit 1; }
else
    echo "Обновление репозитория..."
    cd "$WORK_DIR" || exit 1
    git pull || { echo "Ошибка при обновлении репозитория!"; exit 1; }
fi
#Установка зависимостей
echo "Установка зависимостей из requirements.txt..."
if [ -f "$WORK_DIR/requirements.txt" ]; then
    pip install -r "$WORK_DIR/requirements.txt" || { echo "Ошибка при установке зависимостей!"; exit 1; }
else
    echo "Файл requirements.txt не найден, пропуск установки зависимостей."
fi

# Шаг 2. Сборка проекта
echo "Сборка проекта..."
cd "$WORK_DIR" || exit 1

# Шаг 3. Запуск pytests 
echo "Запуск тестов с помощью pytest..."
pytest "$WORK_DIR/test.py" || {
    echo "Тесты завершились с ошибкой!"
    exit 1
}

# Шаг 4. Создание установщика
echo "Создание установщика..."
pyinstaller --onefile "$WORK_DIR/calculator.py" || { echo "Ошибка при создании установщика!"; exit 1; }


# Шаг 5. Установка приложения
INSTALLER_PATH="$WORK_DIR/dist/calculator"
if [ -f "$INSTALLER_PATH" ]; then
    echo "Установщик создан: $INSTALLER_PATH"
    echo "Установка приложения..."
    sudo cp "$INSTALLER_PATH" /usr/local/bin/calculator || { echo "Ошибка при установке приложения!"; exit 1; }
else
    echo "Установщик не найден!"
    exit 1
fi



# Финализация
echo "CI процесс успешно завершён."
