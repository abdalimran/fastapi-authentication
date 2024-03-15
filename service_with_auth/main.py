import contextlib
from fastapi import FastAPI
from routes import auth_router
from routes import text_router
from database import create_all_tables


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    await create_all_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(text_router, prefix="/text", tags=["Text Operations"])
