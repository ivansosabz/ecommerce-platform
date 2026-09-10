# Decisiones detectadas

## Frontend con React y Vite

El proyecto `frontend` usa React, TypeScript y Vite. La configuración activa el plugin oficial de React.

[PENDIENTE: registrar en el repositorio el motivo de elegir React y lo descartado.]

## Backend con FastAPI

El proyecto `backend` declara `fastapi[standard]` y crea una aplicación mínima en `app/main.py`.

[PENDIENTE: registrar el motivo de elegir FastAPI y la versión de Python soportada.]

## Dependencias separadas

El backend separa dependencias de ejecución y desarrollo. `pytest` y `httpx` solo aparecen en `requirements-dev.txt`.

[PENDIENTE: decidir una estrategia de versionado o bloqueo de dependencias.]

## Prueba de disponibilidad

La API expone `GET /health`, cubierto por una prueba que ejecuta la aplicación mediante transporte ASGI.

## Persistencia

No existe una decisión implementada sobre modelos, ORM o migraciones.
