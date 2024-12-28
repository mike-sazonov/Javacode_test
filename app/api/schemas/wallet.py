from pydantic import BaseModel, ConfigDict


class NewWallet(BaseModel):
    balance: int

class WalletFromDB(NewWallet):
    model_config = ConfigDict(from_attributes=True)

    id: str