# Ecommerce Platform

Proyecto universitario de comercio electrónico orientado inicialmente a productos tecnológicos y electrónicos.

El proyecto se desarrolla de forma incremental durante el semestre. Cuenta con la estructura inicial del frontend, un backend por capas y la persistencia del MVP.

## Estructura inicial

```text
ecommerce-platform/
├── backend/
├── docs/
├── frontend/
├── .gitignore
└── README.md
```

## Proyectos

- `frontend`: aplicación React con TypeScript y Vite.
- `backend`: FastAPI con capas HTTP, servicios y repositorios, modelos SQLAlchemy asíncronos y migraciones Alembic.
- `docs`: documentación técnica y de contexto.

## Inicio rápido

### Frontend

```powershell
cd frontend
npm install
npm run dev
```

### Backend

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
Copy-Item .env.example .env
# Editar DATABASE_URL en .env y crear previamente una base PostgreSQL vacía.
python -m alembic upgrade head
python -m uvicorn app.main:app --loop app.core.event_loop:create_event_loop --reload
```

Se requiere Python 3.12 o posterior y PostgreSQL. La implementación fue verificada con Python 3.14.3 y PostgreSQL 17. El bucle explícito permite usar psycopg asíncrono en Windows.

La API expone `GET /health` para comprobar que el backend está disponible. Este endpoint no consulta la base de datos.

### Verificación del backend

Desde `backend`:

```powershell
python -m pytest
python -m ruff check app tests migrations
python -m ruff format --check app tests migrations
```

Las pruebas de integración requieren una base exclusiva de pruebas, previamente creada y migrada:

```powershell
$env:DATABASE_URL='postgresql+psycopg://usuario:contrasena@localhost:5432/ecommerce_test'
python -m alembic upgrade head
$env:TEST_DATABASE_URL=$env:DATABASE_URL
python -m pytest
python -m alembic check
```

Sin `TEST_DATABASE_URL`, las nueve pruebas de integración se omiten. No utilizar una base de producción para estas comprobaciones.

## Estado

Frontend inicializado. Backend con 15 tablas del MVP implementadas en SQLAlchemy y una migración inicial reversible. Las funcionalidades de negocio, sus endpoints y la conexión del frontend siguen pendientes. Las dos tablas de facturación permanecen únicamente en el diagrama como extensión futura.

## Documentación

- [Documentación académica del proyecto](docs/documentacion-proyecto.md)
- [Modelo inicial de base de datos](docs/database/ecommerce.dbml)
- [Contexto técnico del repositorio](docs/contexto/arquitectura.md)
