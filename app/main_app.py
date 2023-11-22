import uvicorn
import asyncio
import aioredis

from constants import BOOKS
from fastapi import FastAPI
from datetime import datetime


def create_app():
    app = FastAPI(docs_url='/')

    def read_file(file_path):
        with open(file_path, 'r') as file:
            return file.readlines()

    @app.on_event("startup")
    async def startup_event():
        # Логика, которая выполняется при старте приложения
        # pass
        content = read_file(BOOKS)
        for i in content:
            await asyncio.sleep(3)
            print(i)



    return app


async def main():
    uvicorn.run(
        f"{main_app}:create_app",
        host='0.0.0.0', port=8888,
        debug=True,
    )


if __name__ == '__main__':
    asyncio.run(main())
