# Arquitectura actual

## Stack observado

- Frontend: React 19, TypeScript 6 y Vite 8.
- Backend: Python y FastAPI.
- Pruebas backend: pytest y httpx.
- Persistencia: PostgreSQL, SQLAlchemy asíncrono, psycopg 3 y Alembic. El diagrama contiene 17 tablas; las 15 del MVP tienen modelos y migración inicial. Facturas y detalles de factura se implementarán después.
- Python: 3.12 o posterior; verificado con 3.14.3 y PostgreSQL 17.

## Mapa de carpetas

```text
backend/
├── app/
│   ├── main.py
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   └── services/
├── migrations/
├── alembic.ini
├── .env.example
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
└── tests/

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

El navegador inicia React desde `src/main.tsx` y renderiza `App.tsx`. El backend crea FastAPI en `app/main.py`, registra el router de salud y administra el motor asíncrono mediante el ciclo de vida de la aplicación. `GET /health` sigue devolviendo `{"status": "ok"}` sin consultar PostgreSQL. Los dos proyectos todavía no están conectados.

## Arquitectura por capas

```text
Rutas HTTP (api) y contratos Pydantic (schemas)
  -> Servicios de negocio (services)
  -> Repositorios de datos (repositories)
  -> Modelos SQLAlchemy (models), sesiones (db)
  -> PostgreSQL
```

- Las rutas validarán solicitudes, resolverán dependencias y traducirán resultados o errores a HTTP.
- Los servicios contendrán los casos de uso, las reglas del dominio y los límites de transacción; no dependerán de FastAPI.
- Los repositorios recibirán `AsyncSession` y ejecutarán consultas; no harán commits ni aplicarán reglas de negocio.
- Los contratos públicos serán modelos Pydantic separados de las entidades ORM.
- `core` contiene configuración por entorno y el bucle asíncrono compatible con psycopg en Windows. `db` contiene la base declarativa y el motor y fábrica de sesiones.

En esta etapa, servicios, repositorios y schemas son paquetes preparados para las próximas funcionalidades. No hay CRUD genérico ni casos de uso ficticios. La dependencia `get_session` entrega una sesión por solicitud, cierra sus recursos y revierte las operaciones en caso de error; el servicio deberá confirmar explícitamente las transacciones exitosas.

Las relaciones ORM usan carga explícita (`lazy="raise"`) para evitar consultas implícitas incompatibles con el flujo asíncrono. Los repositorios cargarán las relaciones necesarias con consultas explícitas. Las acciones de eliminación corresponden a las claves foráneas del DBML. El campo `actualizado_en` se actualiza en operaciones emitidas por SQLAlchemy; no existe un trigger para SQL externo.

Alembic administra el esquema. No se ejecuta `create_all` ni se aplican migraciones al iniciar la API. La migración inicial crea las tablas y el enum de pedidos; su reversión elimina ambos. Los catálogos iniciales de roles y métodos de pago todavía no tienen un proceso de carga.

## Modelo de datos diseñado

El DBML organiza las 17 tablas en cinco grupos: identidad y acceso, catálogo, funciones de usuario, ventas y facturación futura. Los roles y métodos de pago son catálogos independientes. Pedidos, detalles de pedido, facturas y detalles de factura conservan copias históricas para que los cambios posteriores del catálogo no modifiquen documentos anteriores.

La facturación electrónica es únicamente una simulación inspirada en SIFEN. Su diseño existe en el diagrama, pero no hay integración con la DNIT ni emisión de documentos tributarios válidos.

## Qué no existe

No hay una base compartida o desplegada configurada, autenticación, API comercial versionada, catálogo funcional, carrito funcional, pedidos funcionales, facturación funcional, Docker, CI ni despliegue. La migración y el acceso asíncrono fueron verificados en una instancia PostgreSQL temporal independiente.

[PENDIENTE: documentar el flujo completo cuando frontend y backend se conecten.]
