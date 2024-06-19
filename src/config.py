import os

from typing import Optional

from dotenv import find_dotenv, load_dotenv
from pydantic import BaseModel

load_dotenv(find_dotenv())


class GeneralConfig(BaseModel):
    DB_TYPE: str = os.getenv("DB_TYPE")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_DATABASE: str = os.getenv("DB_DATABASE")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_DRIVER: Optional[str] = os.getenv("DB_DRIVER", default="")
    DB_SCHEMA: Optional[str] = os.getenv("DB_SCHEMA", default="")
    LOG_LEVEL: Optional[str] = os.getenv("LOG_LEVEL", default="info")


def get_config() -> GeneralConfig:
    return GeneralConfig()
