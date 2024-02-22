from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.types_for_models import intpk

from datetime import datetime

from src.database import Base

class Operation(Base):
    __tablename__ = "operation"

    id: Mapped[intpk] = mapped_column()
    quantity: Mapped[str] = mapped_column()
    figi: Mapped[str] = mapped_column()
    instrument_type: Mapped[str] = mapped_column() 
    created_date: Mapped[datetime] = mapped_column()

    type: Mapped[str] = mapped_column()