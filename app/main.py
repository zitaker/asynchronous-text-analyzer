import uvicorn
import asyncio
import subprocess

from fastapi import FastAPI
from endpoint_uploading_and_sending import load_data
from result_endpoint import taking_from_database
from create_table import create_table


def create_app():
    app = FastAPI(docs_url='/')

    @app.on_event("startup")
    async def startup_event():
        global redis_server_process
        redis_server_process = subprocess.Popen(["redis-server"])
        return await create_table()

    @app.get("/endpoint")
    async def get_endpoint():
        await load_data()

    @app.get("/stats")
    async def get_stats():
        return await taking_from_database()
    return app


async def main():
    uvicorn.run(
        f"{__name__}:create_app",
        host='0.0.0.0', port=8888,
        reload=True,
    )


if __name__ == '__main__':
    asyncio.run(main())
