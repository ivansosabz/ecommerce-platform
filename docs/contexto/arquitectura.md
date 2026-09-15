# Arquitectura actual

## Stack observado

- Frontend: React 19, TypeScript 6 y Vite 8.
- Backend: Python y FastAPI.
- Pruebas backend: pytest y httpx.
- Persistencia: modelo conceptual PostgreSQL de 17 tablas diseñado en DBML, todavía no implementado.

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
docs/database/ecommerce.dbml
docs/documentacion-proyecto.md
```

## Flujo disponible

El navegador inicia React desde `src/main.tsx` y renderiza `App.tsx`. El backend crea una aplicación FastAPI en `app/main.py` y expone `GET /health`. Los dos proyectos todavía no están conectados.

## Modelo de datos diseñado

El DBML organiza las 17 tablas en cinco grupos: identidad y acceso, catálogo, funciones de usuario, ventas y facturación futura. Los roles y métodos de pago son catálogos independientes. Pedidos, detalles de pedido, facturas y detalles de factura conservan copias históricas para que los cambios posteriores del catálogo no modifiquen documentos anteriores.

La facturación electrónica es únicamente una simulación inspirada en SIFEN. Su diseño existe en el diagrama, pero no hay integración con la DNIT ni emisión de documentos tributarios válidos.

## Qué no existe

No hay una base PostgreSQL conectada, ORM, migraciones, autenticación, API versionada, catálogo funcional, carrito funcional, pedidos funcionales, facturación funcional, Docker, CI ni despliegue.

[PENDIENTE: documentar el flujo completo cuando frontend y backend se conecten.]
