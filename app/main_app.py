import uvicorn
import asyncio
# import aioredis

from fastapi import FastAPI
from broker_message import broker_message


def create_app():
    app = FastAPI(docs_url='/')

    @app.on_event("startup")
    async def startup_event():
        # # Логика, которая выполняется при старте приложения
        # # pass
        # content = read_file(BOOKS)
        # for i in content:
        #     await asyncio.sleep(3)
        #     print(i)
        print(broker_message())



    return app


async def main():
    uvicorn.run(
        f"{main_app}:create_app",
        host='0.0.0.0', port=8888,
        debug=True,
    )


if __name__ == '__main__':
    asyncio.run(main())
