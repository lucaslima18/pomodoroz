from datetime import datetime

from typing import Optional
from sqlmodel import SQLModel, Field


class Project(SQLModel, table=True):
    __tablename__ = "project"
    __table_args__ = {"extend_existing": True}

    id: int = Field(default=None, primary_key=True, index=True)
    name: str = Field(default=None, nullable=True)
    description: str = Field(default=None, nullable=True)
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now())
