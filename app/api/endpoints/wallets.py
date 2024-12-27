from fastapi import APIRouter


wallets_router = APIRouter(
    prefix="/wallets"
)

@wallets_router.get("/")
async def hello_world():
    return {"message": "Hello world!"}
