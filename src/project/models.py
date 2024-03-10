from typing import List

from src.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.types_for_models import intpk, created_at as time_creation
import datetime
from src.auth.models import User


class Project(Base):
    __tablename__ = "project"

    id: Mapped[intpk]
    description: Mapped[str] = mapped_column(nullable=False) 
    created_at: Mapped[time_creation] = mapped_column(nullable=False)
    finished_at: Mapped[datetime.datetime] = mapped_column(nullable=False)
    project_manager_col: Mapped["Project_manager"] = relationship(back_populates="project")
    employee_col: Mapped[List["Employee"]] = relationship()
    stage: Mapped[List["Stage"]] = relationship()
    file: Mapped[bytes] = mapped_column(nullable=True)
    pharmaceutical_substances: Mapped[str] = mapped_column(nullable=True)
    checkbox: Mapped[bool] = mapped_column(nullable=True)
    trade_name: Mapped[str] = mapped_column(nullable=True)
    international_nonproprietary_name: Mapped[str] = mapped_column(nullable=True)
    chemical_name: Mapped[str] = mapped_column(nullable=True)
    type: Mapped[str] = mapped_column(nullable=True)


class Extension_project(Base):
    __tablename__ = "extension_project"

    id: Mapped[intpk]
    additional_column: Mapped[str] = mapped_column(nullable=False)
    additional_value: Mapped[str] = mapped_column(nullable=False)

class Stage(Base):
    __tablename__ = "stage"

    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(nullable=False)
    previous_stage: Mapped[int] = mapped_column(nullable=True)
    next_stage: Mapped[int] = mapped_column(nullable=True)
    status: Mapped[str] = mapped_column(nullable=False)
    performer: Mapped[List["Employee"]] = relationship()
    created_at: Mapped[time_creation] = mapped_column(nullable=False)
    finished_at: Mapped[datetime.datetime] = mapped_column()
    description: Mapped[str] = mapped_column()
    file: Mapped[bytes] = mapped_column(nullable=True)
    task: Mapped[List["Task"]] = relationship()
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"))

class Task(Base):
    __tablename__ = "task"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[time_creation]
    finished_at: Mapped[datetime.datetime] = mapped_column(nullable=False)
    performer: Mapped[List["Employee"]] = relationship()
    comm: Mapped[List["Comment"]] = relationship()
    subtask: Mapped[List["Subtask"]] = relationship()
    stage_id: Mapped[int] = mapped_column(ForeignKey("task.id"))

class Subtask(Base):
    __tablename__ = "subtask"

    id:Mapped[intpk]
    name: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[time_creation]
    performer: Mapped[List["Employee"]] = relationship()
    comm: Mapped[List["Comment"]] = relationship()
    task_id: Mapped[int] = mapped_column(ForeignKey("task.id"))


class Comment(Base):
    __tablename__ = "comment"

    id:Mapped[intpk]
    comm:Mapped[str] = mapped_column(nullable=False)
    task_id: Mapped[int] = mapped_column(ForeignKey("task.id"), nullable=True)
    subtask_id: Mapped[int] = mapped_column(ForeignKey("subtask.id"), nullable=True)

class Employee(Base):
    __tablename__ = "employee"

    id: Mapped[intpk]
    username: Mapped[str] = mapped_column(nullable=False)
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"))
    stage_id: Mapped[int] = mapped_column(ForeignKey("stage.id"))
    task_id: Mapped[int] = mapped_column(ForeignKey("task.id"))
    subtask_id: Mapped[int] = mapped_column(ForeignKey("subtask.id"))


class Project_manager(Base):
    __tablename__ = "project_manager"

    id: Mapped[intpk]
    username: Mapped[str] = mapped_column(nullable=False)
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"))
    project: Mapped["Project"] = relationship(back_populates="project_manager_col")

