# seminario-db

Sistema de gestión de recursos y reservas para seminario usando PostgreSQL y SQLAlchemy.

## Características
- Modelos ORM separados por entidad
- Conexión a PostgreSQL mediante variables de entorno
- Estructura moderna y limpia (PEP8, Poetry, .env, .gitignore)
- Fácil de extender y mantener

## Requisitos
- Python >= 3.10
- PostgreSQL accesible
- [Poetry](https://python-poetry.org/) instalado

## Instalación
```sh
poetry install
```

## Configuración
Crea un archivo `.env` en la raíz del proyecto con las credenciales

## Uso
Para crear las tablas en la base de datos:
```sh
poetry run python src/main.py
```

## Estructura del proyecto
```
seminario-db/
├── src/
│   ├── main.py
│   ├── db/
│   │   └── __init__.py
│   └── models/
│       ├── __init__.py
│       ├── base.py
│       ├── unidad.py
│       ├── tipo_recurso.py
│       ├── recurso.py
│       ├── usuario.py
│       ├── reserva.py
│       ├── prestamo.py
│       ├── devolucion.py
│       └── calificacion.py
├── .env
├── .gitignore
├── pyproject.toml
```

## Comentarios
- Los modelos están organizados en archivos individuales para facilitar la mantenibilidad.
- El archivo `.env` nunca debe subirse al repositorio (ver `.gitignore`).
- Se recomienda usar VS Code y seleccionar el intérprete de Poetry para evitar problemas de importación.
- Puedes agregar tests en una carpeta `tests/` y usar `pytest`.

## Licencia
MIT
