from fastapi import APIRouter, Depends

from app.api.schemas.wallet import NewWallet, WalletFromDB, Operation
from app.services.wallet_service import WalletService
from app.utils.unitofwork import UnitOfWork, IUnitOfWork

wallets_router = APIRouter(
    prefix="/wallets"
)

async def get_wallet_service(uow: IUnitOfWork = Depends(UnitOfWork)):
    return WalletService(uow)

@wallets_router.get("/{wallet_uuid}")
async def get_balance(wallet_uuid: str, wallet_service: WalletService = Depends(get_wallet_service)):
    return await wallet_service.get_balance(wallet_uuid)


@wallets_router.post("/{wallet_uuid}/operation")
async def wallet_operation(wallet_uuid: str, params: Operation, wallet_service: WalletService = Depends(get_wallet_service)):
    return await wallet_service.wallet_operation(wallet_uuid, params)


@wallets_router.post("/create_wallet", response_model=WalletFromDB)
async def create_wallet(wallet_data: NewWallet, wallet_service: WalletService = Depends(get_wallet_service)):
    return await wallet_service.create_wallet(wallet_data)
