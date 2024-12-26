from fastapi import APIRouter


wallet_router = APIRouter(
    prefix="/wallet"
)

@wallet_router.get("/")
async def hello_world():
    return {"message": "Hello world!"}