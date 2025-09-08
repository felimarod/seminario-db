"""
Utilidades para la conexión a la base de datos Oracle.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from typing import Any

def get_engine(user: str, password: str, host: str = "localhost", port: int = 1521, service: str = "xe") -> Any:
    """
    Retorna un engine de SQLAlchemy para OracleDB.
    """
    url = f"oracle+oracledb://{user}:{password}@{host}:{port}/{service}"
    return create_engine(url)

def create_tables(engine: Any) -> None:
    """
    Crea todas las tablas en la base de datos.
    """
    Base.metadata.create_all(engine)

def drop_tables(engine: Any) -> None:
    """
    Elimina todas las tablas en la base de datos.
    """
    Base.metadata.drop_all(engine)

def get_session(engine: Any) -> Any:
    """
    Retorna una sesión de SQLAlchemy.
    """
    Session = sessionmaker(bind=engine)
    return Session()
