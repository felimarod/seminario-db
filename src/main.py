"""
Punto de entrada principal del proyecto seminario-db.
"""

from db import get_engine, create_tables, drop_tables
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    user = os.getenv("ORACLE_USER") or ""
    password = os.getenv("ORACLE_PASSWORD") or ""
    host = os.getenv("ORACLE_HOST", "localhost")
    port = int(os.getenv("ORACLE_PORT", "1521"))
    service = os.getenv("ORACLE_SERVICE", "xe")

    engine = get_engine(user, password, host, port, service)

    opcion = input("¿Qué acción deseas realizar?\n1. Crear tablas\n2. Eliminar tablas\n3. Recrear tablas\nSelecciona (1/2/3): ")
    if opcion == "1":
        create_tables(engine)
        print("✅ Tablas creadas exitosamente en OracleDB.")
    elif opcion == "2":
        confirm = input("¿Seguro que deseas eliminar TODAS las tablas? (escribe 'SI' para confirmar): ")
        if confirm == "SI":
            drop_tables(engine)
            print("⚠️ Todas las tablas han sido eliminadas.")
        else:
            print("Operación cancelada.")
    elif opcion == "3":
        confirm = input("¿Seguro que deseas eliminar TODAS las tablas y crearlas desde cero? (escribe 'SI' para confirmar): ")
        if confirm == "SI":
            drop_tables(engine)
            create_tables(engine)
            print("✅ Tablas recreadas exitosamente en OracleDB.")
        else:
            print("Operación cancelada.")
    else:
        print("Opción no válida.")
