import uvicorn
import asyncio

from fastapi import FastAPI
from app.broker_message import load
from app.test import taking_from_db


def create_app():
    app = FastAPI(docs_url='/')

    @app.on_event("startup")
    async def startup_event():
        # await load()
        pass

    @app.get("/stats")
    def stats():
        # return {"Hello": "World"}
        return taking_from_db()
    return app


async def main():
    uvicorn.run(
        f"{main_app}:create_app",
        host='0.0.0.0', port=8888,
        debug=True,
    )


if __name__ == '__main__':
    asyncio.run(main())
