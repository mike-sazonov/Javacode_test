from app.api.schemas.wallet import NewWallet, WalletFromDB, Operation
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
        wallet_uuid = data
        async with self.uow:
            wallet_from_db = await self.uow.wallet.find_one(id=wallet_uuid)

            return wallet_from_db.balance

    async def wallet_operation(self, data: str, params: Operation):
        new_values = dict()
        async with self.uow:
            balance = await self.get_balance(data)
            if params.operationType == 'DEPOSIT':
                new_values['balance'] = balance + params.amount
                await self.uow.wallet.update_one(new_values, id=data)
                await self.uow.commit()

                message = f"Средства успешно зачислены, баланс {new_values['balance']}"
            elif params.operationType == 'WITHDRAW':
                if balance >= params.amount:
                    new_values['balance'] = balance - params.amount
                    await self.uow.wallet.update_one(new_values, id=data)
                    await self.uow.commit()

                    message = f"Средства успешно списаны, баланс {new_values['balance']}"
                else:
                    message = "Недостаточно средств для списания"


            return {"message": message}



