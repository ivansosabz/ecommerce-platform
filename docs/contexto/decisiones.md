# Decisiones detectadas

## Frontend con React y Vite

El proyecto `frontend` usa React, TypeScript y Vite. La configuración activa el plugin oficial de React.

[PENDIENTE: registrar en el repositorio el motivo de elegir React y lo descartado.]

## Backend con FastAPI

El proyecto `backend` declara `fastapi[standard]` y crea una aplicación mínima en `app/main.py`.

[PENDIENTE: registrar el motivo de elegir FastAPI.]

## Dependencias separadas

El backend separa dependencias de ejecución y desarrollo. `pytest` y `httpx` solo aparecen en `requirements-dev.txt`.

Las dependencias nuevas declaran rangos de versiones; el bloqueo completo de dependencias permanece pendiente.

## Prueba de disponibilidad

La API expone `GET /health`, cubierto por una prueba que ejecuta la aplicación mediante transporte ASGI.

## Persistencia

El modelo conceptual se documenta en `docs/database/ecommerce.dbml`. Incluye 17 tablas en español para identidad, catálogo, favoritos, carrito, pedidos y el diseño futuro de facturación.

Decisiones aprobadas:

- PostgreSQL con UUID y marcas de tiempo con zona horaria.
- Nombres de tablas, columnas, enums, índices, restricciones y notas en español, con `snake_case` y sin tildes.
- Roles normalizados mediante la tabla `roles`, con un único rol por usuario. Los valores iniciales previstos son `usuario` y `administrador`.
- Categorías jerárquicas mediante `categoria_padre_id`, limitadas inicialmente a dos niveles por la aplicación.
- Especificaciones normalizadas como definición, valor textual y unidad opcional.
- Un carrito persistente por usuario autenticado.
- Métodos de pago normalizados como catálogo y referenciados por cada pedido.
- Dirección de entrega almacenada como copia histórica del pedido.
- Una moneda configurable, conservando su código ISO en cada pedido.
- Factura electrónica paraguaya simulada con cabecera y detalles independientes, diseñada para una fase posterior.
- CDC simulado de 44 dígitos y numeración por establecimiento, punto de expedición y número de documento.
- IVA registrado por detalle y resumido en la cabecera de la factura.
- Aplicación pragmática de tercera forma normal: los catálogos se separan, mientras que los datos históricos de pedidos y facturas permanecen como copias deliberadas.
- Eliminación lógica para usuarios, categorías, marcas y productos.
- Implementación con SQLAlchemy asíncrono, psycopg 3 y Alembic.

La simulación no se conecta con SIFEN, no firma documentos y no produce comprobantes con validez tributaria. El diagrama fue aprobado el 17/09/2026. Se implementaron las 15 tablas del MVP; `facturas` y `detalles_factura` permanecen como diseño futuro por decisión del responsable.

## Arquitectura por capas, 17/09/2026

Se adopta el flujo rutas HTTP -> servicios -> repositorios -> SQLAlchemy -> PostgreSQL. Las reglas de negocio y las transacciones pertenecen a servicios; los repositorios reciben una sesión y no realizan commits. Los contratos Pydantic se mantienen separados de las entidades ORM. Los casos de uso se agregarán de forma incremental.

## Configuración y compatibilidad

Se utiliza `DATABASE_URL` mediante pydantic-settings y se incluye `.env.example` sin credenciales reales. Python mínimo: 3.12, por el uso de `asyncio.run(..., loop_factory=...)`. Las migraciones y el comando documentado de Uvicorn usan `SelectorEventLoop`, compatible con psycopg asíncrono en Windows.

Las nuevas dependencias declaran rangos compatibles. No existe todavía un archivo de bloqueo reproducible para todo el backend. Alembic es la única herramienta que modifica el esquema; iniciar la API no crea tablas automáticamente.
