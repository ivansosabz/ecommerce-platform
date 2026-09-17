# Errores y consideraciones conocidas

## Estado actual

No se conocen defectos funcionales del dominio porque la aplicación todavía no contiene funcionalidades de comercio electrónico.

## Consideraciones

- El frontend muestra el contenido predeterminado generado por Vite; no representa el diseño del producto.
- Frontend y backend todavía no se comunican.
- Las nuevas dependencias de persistencia declaran rangos, pero todavía no existe un bloqueo completo de las dependencias Python.
- Se requiere Python 3.12 o posterior; se verificó la implementación con 3.14.3.
- La configuración PostgreSQL se proporciona mediante `DATABASE_URL`; `.env.example` contiene valores locales de ejemplo que deben ajustarse.
- En Windows, psycopg asíncrono requiere `SelectorEventLoop`. Usar el comando Uvicorn documentado en README; Alembic ya configura ese bucle.
- Las pruebas PostgreSQL se omiten si no se define `TEST_DATABASE_URL`.
- La migración no carga datos iniciales de roles ni métodos de pago.
- Algunos comandos Git muestran una advertencia de permisos al intentar leer el archivo global `C:\Users\ivans\.config\git\ignore`; la configuración local del proyecto sigue siendo utilizable.

[PENDIENTE: actualizar esta lista cuando aparezcan errores reproducibles o limitaciones confirmadas.]
