import uvicorn
import asyncio
import subprocess

from fastapi import FastAPI
from app.endpoint_uploading_and_sending import load
from app.result_endpoint import taking_from_db


def create_app():
    app = FastAPI(docs_url='/')

    @app.on_event("startup")
    async def startup_event():
        global redis_server_process
        redis_server_process = subprocess.Popen(["redis-server"])

    @app.get("/begin")
    async def begin():
        await load()

    @app.get("/stats")
    async def stats():
        return await taking_from_db()
    return app


async def main():
    uvicorn.run(
        f"{main_app}:create_app",
        host='0.0.0.0', port=8888,
        debug=True,
    )


if __name__ == '__main__':
    asyncio.run(main())
