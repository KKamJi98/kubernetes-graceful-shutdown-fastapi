from contextlib import asynccontextmanager
from fastapi import FastAPI
import asyncio

# 애플리케이션 상태를 관리할 글로벌 플래그
shutdown_event = asyncio.Event()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("FastAPI application is starting up...")  # Startup logic
    yield
    print("FastAPI application is shutting down...")  # Shutdown logic
    await asyncio.sleep(5)  # Graceful Shutdown 작업 (ex: DB Connection 등)
    print("FastAPI application shutting down complete!")

# Lifespan을 사용하는 FastAPI 애플리케이션
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI"}
