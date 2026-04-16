from fastapi import FastAPI
from contextlib import asynccontextmanager

from configs.db import engine, Base

from models import (region
, user
, sanitation_record
, sanitation_occurrence
, water_quality_record
, alert)

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

@app.get("/")
async def root():
    return {"message": "API rodando com FastAPI + PostgreSQL async"}