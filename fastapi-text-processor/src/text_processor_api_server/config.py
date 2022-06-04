from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    from text_processor_api_server.jp_router import router as jp_router
    app.include_router(jp_router, prefix='/jp')

    @app.get("/")
    async def root():
        return {"msg": "Hello World"}

    return app
