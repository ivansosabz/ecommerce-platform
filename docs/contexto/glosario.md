# Glosario actual

- **API**: interfaz HTTP proporcionada por FastAPI.
- **ASGI**: interfaz utilizada para ejecutar y probar la aplicación web Python.
- **Backend**: proyecto ubicado en `backend`, responsable actualmente del endpoint de salud.
- **Frontend**: proyecto React ubicado en `frontend`.
- **Health check**: petición `GET /health` que devuelve `{"status": "ok"}`.
- **HMR**: actualización rápida durante el desarrollo proporcionada por Vite.
- **CDC**: código de control de 44 dígitos usado como referencia conceptual para identificar una factura electrónica simulada.
- **Detalle de factura**: copia histórica de un concepto facturado, con cantidad, precio e IVA aplicados.
- **Detalle de pedido**: copia histórica del nombre, precio y cantidad de un producto comprado.
- **Factura**: documento comercial simulado asociado de forma única a un pedido; no tiene validez tributaria.
- **IVA**: impuesto al valor agregado representado por detalle y resumido en la factura simulada.
- **Método de pago**: catálogo de opciones que puede seleccionar un pedido; inicialmente solo se prevé una opción simulada.
- **Pedido**: registro histórico creado durante el proceso de compra, con productos, importes y dirección de entrega.
- **Rol**: categoría de autorización asignada a un usuario; se prevén `usuario` y `administrador`.
- **SIFEN**: Sistema Integrado de Facturación Electrónica Nacional de Paraguay, usado solo como referencia conceptual.
- **Snapshot**: copia inmutable de datos relevantes para preservar el estado histórico de un pedido o factura.
- **SPA**: aplicación web cliente; el frontend generado funciona como una aplicación React de una página.
