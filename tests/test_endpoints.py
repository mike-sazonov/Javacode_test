import pytest
from fastapi import Depends
from fastapi.testclient import TestClient

from app.services.wallet_service import WalletService
from app.api.endpoints.wallets import get_wallet_service
from app.utils.unitofwork import IUnitOfWork, UnitOfWorkTest
from main import app
from .db_test import drop_test_db, engine_test
from app.db.database import Base


client = TestClient(app)

async def get_wallet_service_test(uow: IUnitOfWork = Depends(UnitOfWorkTest)):
    return WalletService(uow)



class TestDB:
    test_dct = {}   # for wallet uuid

    app.dependency_overrides[get_wallet_service] = get_wallet_service_test   # override wallet_service with test DB


    @pytest.mark.asyncio
    async def test_start(self):
        async with engine_test.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)


    # create new wallet
    @pytest.mark.asyncio
    async def test_create_wallet(self):
        data = {"balance": 500,}
        response = client.post(
            "/api/v1/wallets/create_wallet",
            json=data)
        assert response.status_code == 200
        assert response.json()["balance"] == 500
        self.test_dct["wallet_uuid"] = response.json()["id"]

    @pytest.mark.asyncio
    async def test_get_balance(self):
        response = client.get(f"/api/v1/wallets/{self.test_dct.get('wallet_uuid')}")
        assert response.status_code == 200
        assert response.json() == {"message": "Balance 500"}


    @pytest.mark.asyncio
    async def test_operation_deposit(self):
        data = {
            "operationType": 'DEPOSIT',
            "amount": 100
        }
        response = client.post(
            f"/api/v1/wallets/{self.test_dct.get('wallet_uuid')}/operation",
            json=data
        )
        assert response.status_code == 200
        assert response.json() == {"message": "Funds successfully credited, balance 600"}


    @pytest.mark.asyncio
    async def test_operation_withdraw(self):
        data = {
            "operationType": 'WITHDRAW',
            "amount": 300
        }
        response = client.post(
            f"/api/v1/wallets/{self.test_dct.get('wallet_uuid')}/operation",
            json=data
        )
        assert response.status_code == 200
        assert response.json() == {"message": "Funds successfully written off, balance 300"}


    # attempt to withdraw more funds than in wallet
    @pytest.mark.asyncio
    async def test_operation_withdraw_too_many(self):
        data = {
            "operationType": 'WITHDRAW',
            "amount": 301   # balance 300
        }
        response = client.post(
            f"/api/v1/wallets/{self.test_dct.get('wallet_uuid')}/operation",
            json=data
        )
        assert response.status_code == 200
        assert response.json() == {"message": "Insufficient funds to write off"}


    @pytest.mark.asyncio
    async def test_operation_withdraw_all(self):
        data = {
            "operationType": 'WITHDRAW',
            "amount": 300  # balance 300
        }
        response = client.post(
            f"/api/v1/wallets/{self.test_dct.get('wallet_uuid')}/operation",
            json=data
        )
        assert response.status_code == 200
        assert response.json() == {"message": "Funds successfully written off, balance 0"}


    @pytest.mark.asyncio
    async def test_finish(self):
        await drop_test_db()

