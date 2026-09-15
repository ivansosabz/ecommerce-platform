# Ecommerce Platform

Proyecto universitario de comercio electrónico orientado inicialmente a productos tecnológicos y electrónicos.

El proyecto se desarrollará de forma incremental durante el semestre. Actualmente se encuentra en su etapa inicial de configuración.

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
- `backend`: API mínima con FastAPI.
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
fastapi dev app/main.py
```

La API expone temporalmente `GET /health` para comprobar que el backend está disponible.

## Estado

Frontend y backend inicializados. La base de datos, el ORM y las funcionalidades del comercio electrónico todavía no han sido implementados.

## Documentación

- [Documentación académica del proyecto](docs/documentacion-proyecto.md)
- [Modelo inicial de base de datos](docs/database/ecommerce.dbml)
- [Contexto técnico del repositorio](docs/contexto/arquitectura.md)
