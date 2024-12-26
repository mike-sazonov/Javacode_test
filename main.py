import uvicorn
from fastapi import FastAPI

from app.api.endpoints.wallets import wallet_router

app = FastAPI()

app.include_router(wallet_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)