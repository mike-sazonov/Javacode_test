import uuid

from sqlalchemy import Integer, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base

class Wallet(Base):
    __tablename__: str = "wallet"

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    balance: Mapped[int] = mapped_column(Integer, nullable=False)
