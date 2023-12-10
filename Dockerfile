FROM python:3.8

RUN apt-get update && \
    apt-get install -y redis-server && \
    pip install python-dotenv fastapi uvicorn redis psycopg2-binary databases[postgresql]

COPY tests/fixtures/O_Genri_Testovaya_20_vmeste.txt /tests/fixtures/O_Genri_Testovaya_20_vmeste.txt
COPY app/main.py /app/main.py
COPY app/create_table.py /app/create_table.py
COPY app/endpoint_uploading_and_sending.py /app/endpoint_uploading_and_sending.py
COPY app/result_endpoint.py /app/result_endpoint.py
COPY app/constants.py /app/constants.py
COPY .env /app/.env

WORKDIR /app

ENV PYTHONPATH /app

EXPOSE 8888

CMD ["python", "main.py"]
