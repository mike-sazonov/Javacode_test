from abc import ABC, abstractmethod

from app.db.database import async_session_maker
from tests.db_test import async_session_maker_test
from app.repositories.wallet_repository import WalletRepository


class IUnitOfWork(ABC):
    wallet: WalletRepository

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, *args):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...


class UnitOfWork(IUnitOfWork):
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()

        self.wallet = WalletRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await  self.session.rollback()

# UOW for tests
class UnitOfWorkTest(UnitOfWork):
    def __init__(self):
        super().__init__()
        self.session_factory = async_session_maker_test     # override session factory

