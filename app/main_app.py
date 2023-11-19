import uvicorn
import asyncio

from constants import BOOKS
from fastapi import FastAPI


def create_app():
    app = FastAPI(docs_url='/')

    def read_file(file_path):
        with open(file_path, 'r') as file:
            return file.readlines()

    @app.on_event("startup")
    async def startup_event():
        # Логика, которая выполняется при старте приложения
        pass

    @app.get("/qwerty")
    async def sending_data():
        content = read_file(BOOKS)
        # отправлять данные в топик брокера сообщение вида {"datetime": "15.11.2023 15:00:25.001", "title": "Very fun book", "text": "...Rofl...lol../n..ololo..." }
        for i in content:
            await asyncio.sleep(1)
            print(i)

        return content

    return app


async def main():
    uvicorn.run(
        f"{main_app}:create_app",
        host='0.0.0.0', port=8888,
        debug=True,
    )


if __name__ == '__main__':
    asyncio.run(main())
