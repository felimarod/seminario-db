#!/usr/bin/env python3
"""
Punto de entrada principal del proyecto seminario-db.
"""

import os
import sys
from pathlib import Path

# Agregar el directorio raíz al path
sys.path.append(str(Path(__file__).parent.parent))

from src.database import engine
from src.models.base import Base
import os
from dotenv import load_dotenv

def create_tables():
    """Crear todas las tablas en la base de datos"""
    Base.metadata.create_all(bind=engine)

def drop_tables():
    """Eliminar todas las tablas de la base de datos"""
    Base.metadata.drop_all(bind=engine)

if __name__ == "__main__":
    load_dotenv()
    
    print("=== Seminario DB - Gestión de Base de Datos ===")
    print("Usando PostgreSQL")

    opcion = input("¿Qué acción deseas realizar?\n1. Crear tablas\n2. Eliminar tablas\n3. Recrear tablas\nSelecciona (1/2/3): ")

    if opcion == "1":
        create_tables()
        print("✅ Tablas creadas exitosamente en PostgreSQL.")
    elif opcion == "2":
        confirm = input("¿Seguro que deseas eliminar TODAS las tablas? (escribe 'SI' para confirmar): ")
        if confirm == "SI":
            drop_tables()
            print("⚠️ Todas las tablas han sido eliminadas.")
        else:
            print("Operación cancelada.")
    elif opcion == "3":
        confirm = input("¿Seguro que deseas eliminar TODAS las tablas y crearlas desde cero? (escribe 'SI' para confirmar): ")
        if confirm == "SI":
            drop_tables()
            create_tables()
            print("✅ Tablas recreadas exitosamente en PostgreSQL.")
        else:
            print("Operación cancelada.")
    else:
        print("Opción no válida.")
