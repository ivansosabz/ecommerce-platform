# Arquitectura actual

## Stack observado

- Frontend: React 19, TypeScript 6 y Vite 8.
- Backend: Python y FastAPI.
- Pruebas backend: pytest y httpx.
- Persistencia: no existe todavía.

## Mapa de carpetas

```text
backend/
├── app/main.py
├── requirements.txt
├── requirements-dev.txt
└── tests/test_health.py

frontend/
├── public/
├── src/
├── package.json
└── vite.config.ts

docs/contexto/
```

## Flujo disponible

El navegador inicia React desde `src/main.tsx` y renderiza `App.tsx`. El backend crea una aplicación FastAPI en `app/main.py` y expone `GET /health`. Los dos proyectos todavía no están conectados.

## Qué no existe

No hay PostgreSQL, ORM, migraciones, autenticación, API versionada, catálogo, carrito, pedidos, Docker, CI ni despliegue.

[PENDIENTE: documentar el flujo completo cuando frontend y backend se conecten.]
