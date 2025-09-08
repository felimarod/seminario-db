
"""
Punto de entrada principal del proyecto seminario-db.
"""

from db import get_engine, create_tables
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
    create_tables(engine)
    print("✅ Tablas creadas exitosamente en OracleDB.")
