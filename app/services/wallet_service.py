from app.api.schemas.wallet import NewWallet, WalletFromDB
from app.utils.unitofwork import IUnitOfWork


class WalletService:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def create_wallet(self, wallet: NewWallet):
        cur_dict: dict = wallet.model_dump()
        async with self.uow:
            wallet_from_db = await self.uow.wallet.add_one(cur_dict)
            wallet_to_return = WalletFromDB.model_validate(wallet_from_db)

            await self.uow.commit()

            return wallet_to_return

    async def get_balance(self, data: str):
        wallet_id = data
        async with self.uow:
            wallet_from_db = await self.uow.wallet.find_one(id=wallet_id)

            return wallet_from_db.balance
