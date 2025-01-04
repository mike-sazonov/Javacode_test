from pydantic import BaseModel, ConfigDict, model_validator


class NewWallet(BaseModel):
    balance: int

    @model_validator(mode='after')
    def balance_validator(self):
        if self.balance < 0:
            raise ValueError("Negative value")
        return self


class WalletFromDB(NewWallet):
    model_config = ConfigDict(from_attributes=True)

    id: str


class Operation(BaseModel):
    operationType: str = 'DEPOSIT'
    amount: int

    @model_validator(mode='after')
    def operation_type_validator(self):
        if self.operationType not in ('DEPOSIT', 'WITHDRAW'):
            raise ValueError("Unknown operation type")
        return self

    @model_validator(mode='after')
    def amount_validator(self):
        if self.amount < 0:
            raise ValueError("Negative value")
        return self