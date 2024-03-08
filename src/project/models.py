from typing import List

from src.database import Base
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.types_for_models import intpk, created_at as time_creation
from datetime import datetime
from src.auth.models import User




class Project(Base):
    __tablename__ = "project"

    id: Mapped[intpk]
    description: Mapped[] = mapped_column(nullable=False) 
    created_at: Mapped[time_creation] = mapped_column(nullable=False)
    finished_at: Mapped[datetime.datetime] = mapped_column(nullable=False)
    project_manager_id:Mapped[int] = mapped_column(ForeignKey("user.id"))
    project_manager: Mapped["User"] = relationship(back_populates="project")
    employee: Mapped[int] = mapped_column(ForeignKey("user.id"))
    chaine_of_stages: Mapped[] = mapped_column()
    files: Mapped[] = mapped_column()
    checkbox: Mapped[] = mapped_column()
    trade_name: Mapped[] = mapped_column()
    international_nonproprietary_name: Mapped[] = mapped_column()
    chemical_name: Mapped[] = mapped_column()
    type: Mapped[] = mapped_column()

    