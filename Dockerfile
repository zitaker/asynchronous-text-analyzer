FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Устанавливаем зависимости
RUN pip install fastapi uvicorn

# Задаем рабочую директорию
WORKDIR /app

# Копируем код приложения в контейнер
COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

# Команда для запуска приложения
CMD ["uvicorn", "main_app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]