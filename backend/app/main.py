from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.health import router as health_router
from app.core.config import Settings
from app.db.session import Database


@asynccontextmanager
async def lifespan(app: FastAPI):
    database = Database(Settings())
    app.state.database = database
    try:
        yield
    finally:
        await database.dispose()


app = FastAPI(title="Ecommerce Platform API", lifespan=lifespan)
app.include_router(health_router)
