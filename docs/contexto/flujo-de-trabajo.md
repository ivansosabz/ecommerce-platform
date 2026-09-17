# Flujo de trabajo actual

## Preparar el frontend

```powershell
cd frontend
npm install
npm run dev
```

Comprobaciones disponibles:

```powershell
npm run lint
npm run build
```

## Preparar el backend

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
Copy-Item .env.example .env
# Ajustar DATABASE_URL y crear previamente la base PostgreSQL.
python -m alembic upgrade head
python -m uvicorn app.main:app --loop app.core.event_loop:create_event_loop --reload
```

Ejecutar pruebas:

```powershell
python -m pytest
python -m ruff check app tests migrations
python -m ruff format --check app tests migrations
```

## Checklist mínimo de terminado

Para ejecutar también las nueve pruebas de integración, configurar `TEST_DATABASE_URL` con una base exclusiva de pruebas previamente migrada. Se comprueban restricciones de integridad, datos históricos y acceso ORM asíncrono; las operaciones de cada prueba se revierten.

Para cambios de esquema: modificar los modelos, generar una revisión con `python -m alembic revision --autogenerate -m 'descripcion'`, revisar sus operaciones y validar `upgrade`, `downgrade` y `python -m alembic check` en una base de pruebas. Verificar manualmente el ciclo de vida de enums PostgreSQL, ya que la autogeneración no agrega necesariamente su eliminación.

- El proyecto afectado compila o arranca.
- Las pruebas existentes pasan.
- El lint del frontend pasa cuando se modifica TypeScript.
- La documentación relacionada refleja el cambio.
- No se agregan secretos ni archivos ignorados.

## Deploy

[PENDIENTE: no existe configuración ni procedimiento de despliegue.]
