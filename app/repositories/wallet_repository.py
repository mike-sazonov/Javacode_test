

from app.repositories.base_repository import SQLAlchemyRepository
from app.db.models import Wallet


class WalletRepository(SQLAlchemyRepository):
    model = Wallet


