from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Usuario(Base):
    __tablename__ = "usuario"
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    rol = Column(String(20), nullable=False)
    reservas = relationship("Reserva", back_populates="usuario")
