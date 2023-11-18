import uvicorn

# from constants import BOOKS
from fastapi import FastAPI


def create_app():
    app = FastAPI(docs_url='/')

    @app.on_event("startup")
    async def startup_event():
        # Логика, которая выполняется при старте приложения
        pass

    @app.get("/qwerty")
    async def read_root():
        return {"message": "Hello, World!"}

    return app


def main():
    uvicorn.run(
        f"{main_app}:create_app",
        host='0.0.0.0', port=8888,
        debug=True,
    )


if __name__ == '__main__':
    main()
