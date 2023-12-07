#FROM python:3
#
#ENV PYTHONDONTWRITEBYTECODE=1
#ENV PYTHONUNBUFFERED=1
#
## Устанавливаем зависимости
#RUN pip install fastapi uvicorn
#
## Задаем рабочую директорию
#WORKDIR /app
#
## Копируем код приложения в контейнер
#COPY requirements.txt /app/
#
#RUN pip install -r requirements.txt
#
#COPY . /app/
#
## Команда для запуска приложения
##CMD ["uvicorn", "app.main_app:app", "--host", "0.0.0.0", "--port", "8888", "--reload"]
##CMD ["uvicorn", "app.main_app:create_app", "--host", "0.0.0.0", "--port", "8888", "--reload"]
#CMD ["uvicorn", "main_app:create_app", "--host", "0.0.0.0", "--port", "8888", "--reload"]
##uvicorn app.main_app:create_app --host 0.0.0.0 --port 8888 --reload


# Используйте официальный образ Python
FROM python:3.8

## Устанавливаем зависимости
#RUN apt-get update && \
#    apt-get install -y redis-server && \
#    pip install python-dotenv fastapi uvicorn redis psycopg2

# Устанавливаем зависимости
RUN apt-get update && \
    apt-get install -y redis-server && \
    pip install python-dotenv fastapi uvicorn redis psycopg2 databases[postgresql]



# Копируем код приложения в контейнер
COPY app/main.py /app/main.py
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
