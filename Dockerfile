# Используйте официальный образ Python
FROM python:3.8

# Устанавливаем зависимости
RUN apt-get update && \
    apt-get install -y redis-server && \
    pip install python-dotenv fastapi uvicorn redis psycopg2-binary databases[postgresql]



# Копируем код приложения в контейнер
COPY app/main.py /app/main.py
COPY app/creating_table.py /app/creating_table.py
COPY app/endpoint_uploading_and_sending.py /app/endpoint_uploading_and_sending.py
COPY app/result_endpoint.py /app/result_endpoint.py
COPY app/constants.py /app/constants.py
COPY .env /app/.env

# Задаем рабочую директорию
WORKDIR /app

# Устанавливаем PYTHONPATH
ENV PYTHONPATH /app

# Открываем порт, на котором будет работать FastAPI
EXPOSE 8888

# Запускаем приложение
CMD ["python", "main.py"]
