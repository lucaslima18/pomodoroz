from datetime import datetime

from typing import Optional
from sqlmodel import SQLModel, Field


class Pomodoro(SQLModel, table=True):
    __table_args__ = {"extend_existing": True}

    id: int = Field(default=None, primary_key=True, index=True)
    task_id: int = Field(foreign_key="project.id", nullable=False, default=None)
    done: bool = Field(default=None, nullable=True)
    break_time: int = Field(default=None, nullable=True)
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now())
