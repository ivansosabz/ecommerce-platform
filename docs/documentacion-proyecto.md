# Documentación de Proyecto Tecnológico

**Universidad Nacional de Caaguazú**  
Facultad de Ciencias y Tecnologías - Sede Coronel Oviedo  
Diseño de Compiladores (KTII080) - Carrera de Ingeniería en Informática  
Trabajo Práctico Integrador

Este documento reúne la documentación viva del proyecto. Se actualizará de forma incremental durante el semestre para registrar decisiones, avances, entregas y referencias.

## 1. Ficha del Proyecto

- **Título:** Plataforma de comercio electrónico para productos tecnológicos.
- **Repositorio:** `ecommerce-platform`.
- **URL:** <https://github.com/ivansosabz/ecommerce-platform>.
- **Áreas involucradas:** desarrollo web frontend y backend, diseño de APIs REST, modelado de bases de datos, autenticación, autorización, infraestructura, testing, control de versiones y documentación técnica.
- **Docentes colaboradores:**

### Integrantes y roles

| Nombre completo | Usuario GitHub | Rol o área principal |
| --- | --- | --- |
| Jesús Iván Sosa Báez | [@ivansosabz](https://github.com/ivansosabz) | Desarrollo full stack |

## 2. Introducción

El proyecto consiste en el desarrollo incremental de una plataforma web de comercio electrónico orientada principalmente a la venta de productos tecnológicos y electrónicos. La aplicación permitirá consultar un catálogo organizado por categorías y marcas, buscar y filtrar productos, registrar usuarios, gestionar favoritos y carrito, realizar un checkout simulado y consultar pedidos. También contará con funciones administrativas para gestionar el catálogo, el stock y los estados de los pedidos. Como extensión posterior se diseñará una factura electrónica paraguaya simulada, sin conexión con la DNIT ni validez tributaria.

El proyecto surge de la necesidad de aplicar de manera integrada los conocimientos adquiridos durante la carrera en un sistema más completo que un CRUD aislado. Su desarrollo permitirá trabajar con frontend, backend, APIs REST, PostgreSQL, autenticación, autorización, testing, Docker y despliegue. Además de cumplir con los objetivos académicos, se busca obtener un producto mantenible y documentado que pueda presentarse posteriormente como proyecto de portfolio.

## 3. Objetivos

### 3.1. Objetivo general

Desarrollar, durante el curso, una plataforma web de comercio electrónico para productos tecnológicos que permita consultar productos, gestionar usuarios y realizar compras simuladas, aplicando una arquitectura por capas, persistencia relacional, pruebas automatizadas y documentación verificable.

### 3.2. Objetivos específicos

1. **OE1. Implementar** una API REST versionada para catálogo, usuarios, favoritos, carrito y pedidos, organizada en rutas, servicios y repositorios, y verificar al menos una operación principal de cada módulo antes del cierre del curso.
2. **OE2. Desarrollar** una interfaz responsiva con vistas de catálogo, autenticación, carrito, checkout y pedidos, y verificar el flujo de compra simulado en tamaños móvil y escritorio antes de la demostración final.
3. **OE3. Implementar** las 15 tablas del MVP aprobado en PostgreSQL con SQLAlchemy y Alembic, conservando sus restricciones y relaciones, y verificar la creación y reversión de la migración inicial durante la etapa de datos.
4. **OE4. Implementar** registro y acceso con email y contraseña, así como acceso con Google mediante OAuth 2.0 y OpenID Connect, y verificar los escenarios de acceso exitoso y rechazo de credenciales inválidas durante la etapa de autenticación.
5. **OE5. Aplicar** los roles usuario y administrador, y verificar que un usuario común no pueda ejecutar las operaciones administrativas del catálogo y los pedidos antes de finalizar el MVP.
6. **OE6. Incorporar** pruebas automatizadas de integridad de datos, autenticación, catálogo, carrito, pedidos y permisos, incluyendo al menos un escenario exitoso y uno de error por flujo crítico implementado, y ejecutarlas antes de publicar los cambios correspondientes.
7. **OE7. Preparar** la configuración por entorno, la ejecución mediante Docker, una comprobación automatizada en CI y un despliegue demostrable del MVP antes de la entrega final.
8. **OE8. Mantener** la documentación académica y técnica actualizada semanalmente, registrando cada actividad relevante con responsable, área, estado y enlace al commit disponible, y relacionar los ocho objetivos específicos con actividades de la bitácora.

Los plazos se relacionan con las etapas del cronograma tentativo de 16 semanas; las fechas oficiales se ajustarán al calendario del curso cuando esté disponible. Los objetivos describen entregables previstos y no implican que las funcionalidades estén terminadas.

## 4. Justificación y Análisis de Viabilidad

### 4.1. Justificación

El proyecto permite integrar conocimientos de desarrollo frontend y backend, diseño de APIs, bases de datos relacionales, seguridad, testing, infraestructura y Git. Un comercio electrónico presenta problemas relevantes como el manejo de identidades, permisos, stock, búsqueda, persistencia del carrito y conservación histórica de pedidos. Esto lo convierte en un trabajo apropiado para la materia y en una base sólida para un proyecto de portfolio.

### 4.2. Viabilidad técnica

La solución se desarrollará como una aplicación web dentro de un monorepositorio. El frontend utiliza React, TypeScript y Vite. El backend utiliza Python y FastAPI. La persistencia prevista utiliza PostgreSQL, SQLAlchemy en modo asíncrono, psycopg 3 y Alembic. Las herramientas seleccionadas son de código abierto y cuentan con documentación oficial disponible.

### 4.3. Viabilidad de tiempo y recursos

El proyecto es viable dentro del semestre si se mantiene el alcance del MVP y se implementa por etapas. Se utilizarán herramientas gratuitas y servicios gratuitos o de bajo costo cuando sea posible. Las funcionalidades con mayor costo operativo o complejidad se registran como posibles extensiones y no condicionan la finalización académica.

### 4.4. Riesgos identificados

| Riesgo | Impacto | Mitigación propuesta |
| --- | --- | --- |
| Alcance excesivo para el semestre | Alto | Priorizar el MVP y mantener las extensiones fuera de los criterios de finalización. |
| Modelo de datos incorrecto o prematuro | Alto | Validar primero el diagrama en dbdiagram.io y crear la ORM después de su aprobación. |
| Confundir la factura simulada con un comprobante fiscal válido | Alto | Identificarla explícitamente como simulación y excluir integración, firma y validación ante SIFEN. |
| Complejidad de OAuth y vinculación de cuentas | Alto | Diseñar el flujo antes de implementarlo y cubrir los casos críticos con pruebas. |
| Inconsistencias de stock durante el checkout | Alto | Validar y actualizar el stock dentro de una transacción al crear el pedido. |
| Falta de tiempo para pruebas y documentación | Medio | Incluir pruebas y documentación dentro de cada fase. |
| Problemas de configuración o despliegue | Medio | Usar variables de entorno, `.env.example`, Docker y CI de forma progresiva. |

## 5. Alcance y Limitaciones

### Incluido en el MVP

- Catálogo público con productos, imágenes, marcas, categorías y subcategorías.
- Búsqueda tradicional, filtros, ordenamiento y paginación.
- Registro y login con email y contraseña.
- Login con Google mediante OAuth 2.0 y OpenID Connect.
- Roles `usuario` y `administrador`, almacenados en una entidad independiente.
- Perfil básico, favoritos y carrito persistente para usuarios autenticados.
- Checkout con método de pago simulado.
- Pedidos con datos históricos de los productos y la dirección de entrega.
- Administración básica del catálogo, stock, pedidos y usuarios.
- Pruebas sobre las funcionalidades críticas.
- Documentación, Docker, CI y despliegue demostrable.

### Fuera del alcance del MVP

- Pagos reales.
- Carrito anónimo o sincronización híbrida.
- Cupones, reseñas y recomendaciones.
- Reservas temporales de inventario.
- Múltiples vendedores.
- Devoluciones y reembolsos.
- Paneles analíticos avanzados.
- Gestión compleja de envíos.
- Recomendaciones, búsqueda semántica o asistentes basados en IA.
- Emisión fiscal real, integración con SIFEN, firma digital y comprobantes válidos ante la DNIT.

Estas funciones podrán evaluarse como extensiones posteriores, pero no forman parte de los criterios de finalización del MVP académico.

### Extensión posterior planificada

El modelo conceptual incluye una factura electrónica paraguaya simulada con cabecera, detalles, IVA y un CDC ficticio de 44 dígitos. Esta función se implementará después del MVP y no representa una pasarela de pago ni un sistema de facturación homologado.

## 6. Áreas de Trabajo y Arquitectura General

La solución sigue una arquitectura cliente-servidor dentro de un monorepositorio. El frontend React consumirá una API REST construida con FastAPI. El backend se organiza en capas de rutas HTTP, servicios de negocio y repositorios de datos. Los servicios definirán reglas y transacciones; los repositorios ejecutarán consultas mediante SQLAlchemy sin confirmar transacciones. Los contratos Pydantic estarán separados de los modelos ORM. Alembic administra los cambios del esquema. Los secretos se proporcionan mediante variables de entorno y no se almacenan en Git.

```text
Usuario
  -> Frontend React
  -> Rutas HTTP FastAPI
  -> Servicios de negocio
  -> Repositorios y modelos SQLAlchemy
  -> PostgreSQL
```

| Área | Qué abarca en este proyecto | Responsable |
| --- | --- | --- |
| Frontend | Interfaz, navegación, catálogo, autenticación, carrito y administración | Jesús Iván Sosa Báez |
| Backend | API REST, reglas de negocio, autenticación y autorización | Jesús Iván Sosa Báez |
| Datos | Modelo relacional, integridad, consultas y migraciones | Jesús Iván Sosa Báez |
| Calidad e infraestructura | Testing, Docker, CI y despliegue | Jesús Iván Sosa Báez |
| Documentación | README, documentación académica, bitácora y decisiones | Jesús Iván Sosa Báez |

## 7. Guía del Repositorio

### Estructura actual

```text
ecommerce-platform/
├── backend/
│   ├── app/
│   └── tests/
├── frontend/
│   ├── public/
│   └── src/
├── docs/
│   ├── contexto/
│   ├── database/
│   └── documentacion-proyecto.md
├── .gitignore
└── README.md
```

### Clonado

```powershell
git clone https://github.com/ivansosabz/ecommerce-platform.git
cd ecommerce-platform
```

### Frontend

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

### Backend

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
Copy-Item .env.example .env
# Ajustar DATABASE_URL y crear previamente una base PostgreSQL.
python -m alembic upgrade head
python -m uvicorn app.main:app --loop app.core.event_loop:create_event_loop --reload
```

Pruebas:

```powershell
python -m pytest
python -m ruff check app tests migrations
python -m ruff format --check app tests migrations
```

Se requiere Python 3.12 o posterior. Las pruebas de integración se habilitan con `TEST_DATABASE_URL`, apuntando a una base exclusiva de pruebas previamente migrada. Sin esa variable se omiten; las pruebas de salud y del contrato ORM no requieren una conexión.

### Ramas y commits

- `main` mantiene el estado estable del proyecto.
- Las funcionalidades se desarrollan en ramas breves `feature/<nombre>` cuando sea necesario.
- Se utilizan commits pequeños y descriptivos, preferentemente con Conventional Commits: `feat`, `fix`, `docs`, `test`, `refactor` y `chore`.
- Los archivos relacionados se agrupan en un mismo commit y los cambios independientes se separan.

## 8. Bitácora de Avances por Clase

| Clase o fecha | Actividad realizada | Área | Responsable | Commit o enlace | Estado | Objetivo relacionado |
| --- | --- | --- | --- | --- | --- | --- |
| 10/09/2026 | Creación de la estructura inicial del repositorio | Configuración | Jesús Iván Sosa Báez | [751d76d](https://github.com/ivansosabz/ecommerce-platform/commit/751d76dab5d52c6cc4a7b78a35136fecf761c573) | Completo | OE7, OE8 |
| 10/09/2026 | Inicialización del frontend con React, TypeScript y Vite | Frontend | Jesús Iván Sosa Báez | [a4e7acc](https://github.com/ivansosabz/ecommerce-platform/commit/a4e7acc32468118bdacb27280b71a962da3c51ce) | Completo | OE2 |
| 10/09/2026 | Inicialización del backend con FastAPI y endpoint de salud | Backend | Jesús Iván Sosa Báez | [12576c4](https://github.com/ivansosabz/ecommerce-platform/commit/12576c4e5441a356c9eac9ce25b6137c207fd8e2) | Completo | OE1 |
| 10/09/2026 | Creación de los documentos de contexto | Documentación | Jesús Iván Sosa Báez | [dbdd949](https://github.com/ivansosabz/ecommerce-platform/commit/dbdd949fe2fdd8481b5676a66c007bc9e26b8be8) | Completo | OE8 |
| 10/09/2026 | Actualización de exclusiones del repositorio | Configuración | Jesús Iván Sosa Báez | [7c46e79](https://github.com/ivansosabz/ecommerce-platform/commit/7c46e793a9b8a6cca5a3e601eb895d38ba675d6b) | Completo | OE7 |
| 15/09/2026 | Refinamiento del modelo relacional de 17 tablas con restricciones, relaciones y copias históricas | Datos | Jesús Iván Sosa Báez | [81cbd30](https://github.com/ivansosabz/ecommerce-platform/commit/81cbd30fef41e8af7bbe67cbdd28981a657512dd) | Completo | OE3 |
| 15/09/2026 | Revisión del alcance del MVP y actualización de la documentación académica | Documentación | Jesús Iván Sosa Báez | [448a705](https://github.com/ivansosabz/ecommerce-platform/commit/448a705018dc51c1155dc4e7c107bdfe330e0c92) | Completo | OE8 |
| 15/09/2026 | Actualización del README y exclusión de fuentes locales de documentación | Configuración y documentación | Jesús Iván Sosa Báez | [2984f5e](https://github.com/ivansosabz/ecommerce-platform/commit/2984f5e66c5f50aa6362e7cccf072d4cc28d2f33) | Completo | OE7, OE8 |
| 17/09/2026 | Implementación de los modelos SQLAlchemy correspondientes a las 15 tablas aprobadas del MVP | Datos y backend | Jesús Iván Sosa Báez | [3be5f78](https://github.com/ivansosabz/ecommerce-platform/commit/3be5f78f81d461031f398e2ff7b0d10f70887e9a) | Completo | OE3 |
| 17/09/2026 | Creación de la migración inicial Alembic y verificación de su creación, reversión y recreación en PostgreSQL 17 temporal | Datos y calidad | Jesús Iván Sosa Báez | [3be5f78](https://github.com/ivansosabz/ecommerce-platform/commit/3be5f78f81d461031f398e2ff7b0d10f70887e9a) | Completo | OE3, OE6 |
| 17/09/2026 | Organización del backend por capas, extracción del router de salud y preparación de paquetes de servicios, repositorios y contratos | Backend | Jesús Iván Sosa Báez | [3be5f78](https://github.com/ivansosabz/ecommerce-platform/commit/3be5f78f81d461031f398e2ff7b0d10f70887e9a) | Completo | OE1 |
| 17/09/2026 | Configuración del motor y sesiones asíncronas, DATABASE_URL y compatibilidad de psycopg con Windows | Backend e infraestructura | Jesús Iván Sosa Báez | [3be5f78](https://github.com/ivansosabz/ecommerce-platform/commit/3be5f78f81d461031f398e2ff7b0d10f70887e9a) | Completo | OE7 |
| 17/09/2026 | Incorporación y ejecución de 12 pruebas de salud, correspondencia con el DBML e integridad PostgreSQL; revisión de código con Ruff | Calidad | Jesús Iván Sosa Báez | [3be5f78](https://github.com/ivansosabz/ecommerce-platform/commit/3be5f78f81d461031f398e2ff7b0d10f70887e9a) | Completo | OE6 |
| 17/09/2026 | Revisión del objetivo general y los ocho objetivos específicos en infinitivo, con criterios verificables y actividades asociadas | Documentación académica | Jesús Iván Sosa Báez | [bb918b5](https://github.com/ivansosabz/ecommerce-platform/commit/bb918b55e04438854593e8be0c6141f1b730dd9d) | Completo | OE8 |
| 17/09/2026 | Actualización de la bitácora semanal, arquitectura por capas, decisiones técnicas y guía de ejecución y pruebas | Documentación técnica | Jesús Iván Sosa Báez | [bb918b5](https://github.com/ivansosabz/ecommerce-platform/commit/bb918b55e04438854593e8be0c6141f1b730dd9d) | Completo | OE7, OE8 |
| Planificada: catálogo y búsqueda | Implementar endpoints versionados y consultas para categorías, marcas, productos, filtros y paginación | Backend | Jesús Iván Sosa Báez | Sin commit: actividad pendiente | Pendiente | OE1 |
| Planificada: interfaz | Desarrollar y verificar vistas de catálogo, autenticación, carrito, checkout y pedidos en móvil y escritorio | Frontend | Jesús Iván Sosa Báez | Sin commit: actividad pendiente | Pendiente | OE2 |
| Planificada: autenticación | Implementar y probar registro, acceso con contraseña y acceso con Google OIDC | Backend y seguridad | Jesús Iván Sosa Báez | Sin commit: actividad pendiente | Pendiente | OE4, OE6 |
| Planificada: autorización | Implementar y probar permisos de usuario y administrador para catálogo y pedidos | Backend y seguridad | Jesús Iván Sosa Báez | Sin commit: actividad pendiente | Pendiente | OE5, OE6 |
| Planificada: funciones de usuario y ventas | Implementar favoritos, carrito persistente, checkout simulado y pedidos, con pruebas de éxito y error | Backend y calidad | Jesús Iván Sosa Báez | Sin commit: actividad pendiente | Pendiente | OE1, OE6 |
| Planificada: despliegue | Preparar Docker, CI y un despliegue demostrable del MVP | Infraestructura | Jesús Iván Sosa Báez | Sin commit: actividad pendiente | Pendiente | OE7 |
| Pendiente de enlaces | Actualizar el documento oficial en Google Drive y comentar en la entrega de Classroom después de verificar la actualización | Documentación y entrega académica | Jesús Iván Sosa Báez | Sin commit: actividad pendiente | Pendiente | OE8 |

Las actividades futuras son compromisos planificados; no se presentan como avances realizados. Los trabajos de la semana del 14 al 20 de septiembre corresponden a las filas del 15 y 17/09/2026. Las filas del 10/09 se conservan como historial.

Estados permitidos: Pendiente, En curso, Completo y Bloqueado.

## 9. Cronograma Tentativo

| Etapa | Semana o clase estimada | Entregable asociado |
| --- | --- | --- |
| Planificación y configuración | Semanas 1 y 2 | Alcance, repositorio, frontend, backend y documentación inicial |
| Diseño de datos | Semanas 2 y 3 | Diagrama aprobado, modelos SQLAlchemy y migración inicial |
| Catálogo | Semanas 4 y 5 | Categorías, marcas, productos, imágenes y catálogo público |
| Búsqueda | Semana 6 | Filtros, búsqueda, ordenamiento y paginación |
| Autenticación | Semanas 7 y 8 | Registro, login, JWT, roles y Google OIDC |
| Funciones de usuario | Semanas 9 y 10 | Perfil, favoritos y carrito persistente |
| Pedidos | Semanas 11 y 12 | Checkout simulado, pedidos y estados |
| Administración | Semana 13 | Gestión de catálogo, stock, pedidos y usuarios |
| Calidad y seguridad | Semanas 14 y 15 | Pruebas, validaciones, errores, logging y refactoring |
| Despliegue y portfolio | Semana 16 | Docker, CI, despliegue, capturas y documentación final |
| Facturación simulada | Posterior al MVP | Factura electrónica ficticia asociada a pedidos, sin integración fiscal |

[PENDIENTE: ajustar las semanas al calendario oficial de clases y entregas].

## 10. Referencias

- DBML. (s. f.). *DBML syntax*. <https://dbml.dbdiagram.io/docs/>
- Dirección Nacional de Ingresos Tributarios. (s. f.). *Guía paso a paso: emisión de documentos tributarios a través del sistema Ekuatia'i*. <https://ekuatia.set.gov.py/documents/20123/884739/Guia%2BPaso%2Ba%2BPaso%2B-%2BEmisi%C3%B3n%2Bdel%2BDocumentos%2BTributarios%2Ba%2Btrav%C3%A9s%2Bdel%2BSistema%2BEkuatia%C2%B4i.pdf/7aef7ee8-28bd-a63b-73ef-5fa92181eee5?t=1714139786444.pdf>
- FastAPI. (s. f.). *Tutorial - User guide*. <https://fastapi.tiangolo.com/tutorial/>
- OpenID Foundation. (2023). *OpenID Connect Core 1.0 incorporating errata set 2*. <https://openid.net/specs/openid-connect-core-1_0.html>
- PostgreSQL Global Development Group. (s. f.). *PostgreSQL documentation*. <https://www.postgresql.org/docs/>
- React Team. (s. f.). *React documentation*. <https://react.dev/>
- SQLAlchemy. (s. f.). *SQLAlchemy 2.0 asyncio documentation*. <https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html>
- Vite. (s. f.). *Getting started*. <https://vite.dev/guide/>

Este documento se actualiza en cada clase de trabajo y forma parte de la entrega final integradora de la materia.
