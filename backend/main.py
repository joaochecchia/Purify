from fastapi import FastAPI
from contextlib import asynccontextmanager

from configs.db import engine, Base

from routes import user_routes

@asynccontextmanager
async def lifespan(app: FastAPI):
    print(Base.metadata.tables.keys())

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    await engine.dispose()

app = FastAPI(
    title="Purify API",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(user_routes.router)

@app.get("/")
async def root():
    return {"message": "API rodando com FastAPI + PostgreSQL async"}