import uvicorn
import asyncio
import json
import aioredis

from constants import BOOKS
from fastapi import FastAPI

def create_app():
    app = FastAPI(docs_url='/')

    async def send_hello_world():
        # Подключение к серверу Redis
        redis = await aioredis.create_redis('redis://127.0.0.1:6379')

        try:
            # Отправка сообщения "hello world" в ключ "my_key"
            await redis.set('my_key', 'hello world')

            # Получение значения из ключа "my_key"
            result = await redis.get('my_key')
            print(f'Received from Redis: {result.decode()}')
        finally:
            # Закрытие соединения с сервером Redis
            redis.close()
            await redis.wait_closed()

    def read_file(file_path):
        with open(file_path, 'r') as file:
            return file.readlines()



    @app.on_event("startup")
    async def startup_event():
        return send_hello_world()
        # Логика, которая выполняется при старте приложения
        # pass
        # content = read_file(BOOKS)
        # for i in content:
        #     await asyncio.sleep(1)
        #     print(i)



    return app


async def main():
    uvicorn.run(
        f"{main_app}:create_app",
        host='0.0.0.0', port=8888,
        debug=True,
    )


if __name__ == '__main__':
    asyncio.run(main())
