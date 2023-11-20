from constants import BOOKS

# Укажите путь к вашему файлу
file_path = BOOKS

# Открываем файл на чтение
with open(file_path, 'r', encoding='utf-8') as file:
    # Читаем все строки файла
    lines = file.readlines()

# Ищем заголовки с двумя пустыми строками после них
index = 0
while index < len(lines):
    # Если строка является заголовком
    if lines[index].strip():
        print(f'Заголовок: {lines[index].strip()}')

        # Ищем две пустые строки после заголовка
        index += 1  # Переходим к следующей строке
        empty_line_count = 0

        while index < len(lines) and empty_line_count < 2:
            if not lines[index].strip():
                empty_line_count += 1
            else:
                empty_line_count = 0  # Сбрасываем счетчик, если найдена не пустая строка
            index += 1  # Переходим к следующей строке

        # Выводим две пустые строки
        print()
    else:
        index += 1  # Переходим к следующей строке

