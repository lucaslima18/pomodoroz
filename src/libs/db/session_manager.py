from typing import Generator

from src.libs.db.database_handler import DatabaseHandler
from src.config import get_config

config = get_config()
db = DatabaseHandler()


def get_session() -> Generator:
    with db as session:
        try:
            yield session

        except Exception:
            session.rollback()
    print("exit")
    yield True


def instance_session() -> DatabaseHandler:
    return DatabaseHandler()
