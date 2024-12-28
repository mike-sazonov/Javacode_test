import uuid

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base

class Wallet(Base):
    __tablename__: str = "wallet"

    id: Mapped[str] = mapped_column(String, primary_key=True, index=True, unique=True, default=str(uuid.uuid4()))
    balance: Mapped[int] = mapped_column(Integer, nullable=False)
