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
- Futura implementación con SQLAlchemy asíncrono, psycopg 3 y Alembic.

La simulación no se conecta con SIFEN, no firma documentos y no produce comprobantes con validez tributaria. La ORM y las migraciones permanecen pendientes hasta que el diagrama sea aprobado en dbdiagram.io.
