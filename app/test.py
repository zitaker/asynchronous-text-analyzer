import psycopg2
import os


DATABASE_URL = os.getenv('DATABASE_URL')


conn = psycopg2.connect(DATABASE_URL)

# # Параметры подключения к базе данных
# conn_params = {
#     'host': 'localhost',
#     'port': 5432,
#     'user': 'georg',
#     'password': 'postgres',
#     'database': 'db'
# }
#
# # Установка соединения
# conn = psycopg2.connect(**conn_params)

# Создание курсора
cursor = conn.cursor()

# # Пример данных для вставки
# book_data = {
#     'datetime': 'qwer',
#     'title': 'qqqq',
#     'text': 'www'
# }
with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
    # SQL-запрос для вставки данных
    curs.execute(
        "INSERT INTO book (datetime, title, text) VALUES ('qwer', 'qqqq', 'www')"
    )

    # Подтверждение изменений и закрытие соединения
    conn.commit()
    cursor.close()
    conn.close()