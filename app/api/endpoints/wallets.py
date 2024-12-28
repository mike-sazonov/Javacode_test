from fastapi import APIRouter, Body


wallets_router = APIRouter(
    prefix="/wallets"
)

@wallets_router.get("/{wallet_uuid}")
async def get_balance(wallet_uuid):
    return {"uuid": wallet_uuid}


@wallets_router.post("/{wallet_uuid}/operation")
async def wallet_operation(wallet_uuid, params: dict = Body()):
    return {
        "uuid": wallet_uuid,
        "operation_type": params.get("operationType"),
        "amount": params.get("amount")
            }
