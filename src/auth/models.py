from datetime import datetime

from typing import Any, List

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from fastapi_users.db import SQLAlchemyBaseUserTable
from src.types_for_models import intpk, str_100, created_at

from src.database import Base
from src.project.models import Project, Stage, Task, Subtask

class User(Base):
    __tablename__ = "user"

    id: Mapped[intpk]
    email: Mapped[str]
    username: Mapped[str_100]
    registered_at: Mapped[created_at]
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_project_manager: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("role.id"))
    role: Mapped["Role"] = relationship()
    project_id_for_manager: Mapped[int] = mapped_column(ForeignKey("project.id"))
    project_for_manager: Mapped["Project"] = relationship(back_populates="project_manager")
    project_id_for_employee: Mapped[int] = mapped_column(ForeignKey("project.id"))
    stage_id: Mapped[int] = mapped_column(ForeignKey("stage.id"))
    task_id: Mapped[int] = mapped_column(ForeignKey("task.id"))
    subtask_id: Mapped[int] = mapped_column(ForeignKey("subtask.id"))



class Role(Base):
    __tablename__ = "role"

    id: Mapped[intpk]
    name: Mapped[str_100]
    permissions: Mapped[dict|list] = mapped_column(type_=JSON, nullable=True)
    user: Mapped[List["User"]] = relationship()

