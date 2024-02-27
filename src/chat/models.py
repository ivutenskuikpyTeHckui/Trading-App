from src.database import Base
from sqlalchemy.orm import Mapped
from src.types_for_models import intpk


class Message(Base):
    __tablename__ = "message"
    id: Mapped[intpk] 
    message: Mapped[str]

    def as_dict(self):
        return {c.name:getattr(self, c.name) for c in self.__table__.columns}
