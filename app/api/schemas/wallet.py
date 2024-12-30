from pydantic import BaseModel, ConfigDict, model_validator


class NewWallet(BaseModel):
    balance: int

class WalletFromDB(NewWallet):
    model_config = ConfigDict(from_attributes=True)

    id: str

class Operation(BaseModel):
    operationType: str
    amount: int
