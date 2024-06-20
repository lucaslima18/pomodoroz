from datetime import datetime

from typing import Optional
from sqlmodel import SQLModel, Field
from src.modules.project.models import Project


class Task(SQLModel, table=True):
    __tablename__ = "task"
    __table_args__ = {"extend_existing": True}

    id: int = Field(default=None, primary_key=True, index=True)
    project_id: int = Field(foreign_key="project.id", nullable=False, default=None)
    Name: str = Field(default=None, nullable=True)
    Description: str = Field(default=None, nullable=True)
    time_for_pomodoro: int = Field(default=None, nullable=True)
    init_time: Optional[datetime] = Field(default=None, nullable=True)
    end_time: Optional[datetime] = Field(default=None, nullable=True)
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now())
