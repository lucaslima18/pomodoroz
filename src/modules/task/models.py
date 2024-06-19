from datetime import datetime

from typing import Optional
from sqlmodel import SQLModel, Field


class Task(SQLModel, table=True):
    __table_args__ = {"extend_existing": True}

    id: int = Field(default=None, primary_key=True, index=True)
    project_id: int = Field(foreign_key="project.id", nullable=False, default=None)
    Name: str = Field(default=None, nullable=True)
    Description: str = Field(default=None, nullable=True)
    time_for_pomodoro: int = Field(default=None, nullable=True)
    init_time: datetime = Field(default=None, nullable=True)
    end_time: datetime = Field(default=None, nullable=True)
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now())
