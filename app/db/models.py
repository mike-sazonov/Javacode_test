import uuid

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Wallet(Base):
    __tablename__: str = "wallet"

    @staticmethod
    def generate_uuid():
        return str(uuid.uuid4())

    id: Mapped[str] = mapped_column(String, primary_key=True, default=generate_uuid)
    balance: Mapped[int] = mapped_column(Integer, nullable=False)
