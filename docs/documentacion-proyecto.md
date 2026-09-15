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
- **Docentes colaboradores:** [PENDIENTE: registrar docentes colaboradores].

### Integrantes y roles

| Nombre completo | Usuario GitHub | Rol o área principal |
| --- | --- | --- |
| Jesús Iván Sosa Báez | [@ivansosabz](https://github.com/ivansosabz) | Desarrollo full stack |

## 2. Introducción

El proyecto consiste en el desarrollo incremental de una plataforma web de comercio electrónico orientada principalmente a la venta de productos tecnológicos y electrónicos. La aplicación permitirá consultar un catálogo organizado por categorías y marcas, buscar y filtrar productos, registrar usuarios, gestionar favoritos y carrito, realizar un checkout simulado y consultar pedidos. También contará con funciones administrativas para gestionar el catálogo, el stock y los estados de los pedidos. Como extensión posterior se diseñará una factura electrónica paraguaya simulada, sin conexión con la DNIT ni validez tributaria.

El proyecto surge de la necesidad de aplicar de manera integrada los conocimientos adquiridos durante la carrera en un sistema más completo que un CRUD aislado. Su desarrollo permitirá trabajar con frontend, backend, APIs REST, PostgreSQL, autenticación, autorización, testing, Docker y despliegue. Además de cumplir con los objetivos académicos, se busca obtener un producto mantenible y documentado que pueda presentarse posteriormente como proyecto de portfolio.

## 3. Objetivos

### 3.1. Objetivo general

Diseñar e implementar una plataforma web de comercio electrónico para productos tecnológicos, aplicando una arquitectura modular, buenas prácticas de desarrollo, seguridad, persistencia de datos, testing y documentación.

### 3.2. Objetivos específicos

1. Diseñar una API REST versionada para administrar productos, categorías, marcas, usuarios, favoritos, carrito y pedidos.
2. Desarrollar una interfaz web interactiva y responsiva con React, TypeScript y Vite.
3. Modelar una base de datos relacional en PostgreSQL e implementarla con SQLAlchemy y Alembic.
4. Implementar registro y autenticación mediante email y contraseña, además de acceso con Google mediante OAuth 2.0 y OpenID Connect.
5. Aplicar autorización basada en roles para separar las operaciones de usuarios y administradores.
6. Incorporar pruebas automatizadas para los flujos críticos de autenticación, catálogo, carrito, pedidos y permisos.
7. Preparar el proyecto para ejecución y despliegue mediante variables de entorno, Docker e integración continua.
8. Mantener documentación académica y técnica que permita comprender la arquitectura y la evolución del proyecto.

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

La solución seguirá una arquitectura cliente-servidor dentro de un monorepositorio. El frontend React consumirá una API REST construida con FastAPI. El backend concentrará la autenticación, autorización y reglas de negocio, y accederá a PostgreSQL mediante SQLAlchemy. Alembic administrará los cambios del esquema. Los secretos se proporcionarán mediante variables de entorno y no se almacenarán en Git.

```text
Usuario
  -> Frontend React
  -> API REST FastAPI
  -> SQLAlchemy
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
fastapi dev app/main.py
```

Pruebas:

```powershell
python -m pytest
```

### Ramas y commits

- `main` mantiene el estado estable del proyecto.
- Las funcionalidades se desarrollan en ramas breves `feature/<nombre>` cuando sea necesario.
- Se utilizan commits pequeños y descriptivos, preferentemente con Conventional Commits: `feat`, `fix`, `docs`, `test`, `refactor` y `chore`.
- Los archivos relacionados se agrupan en un mismo commit y los cambios independientes se separan.

## 8. Bitácora de Avances por Clase

| Clase o fecha | Actividad realizada | Área | Responsable | Commit o enlace | Estado |
| --- | --- | --- | --- | --- | --- |
| 10/09/2026 | Creación de la estructura inicial del repositorio | Configuración | Jesús Iván Sosa Báez | `751d76d` | Completo |
| 10/09/2026 | Inicialización del frontend con React, TypeScript y Vite | Frontend | Jesús Iván Sosa Báez | `a4e7acc` | Completo |
| 10/09/2026 | Inicialización del backend con FastAPI y endpoint de salud | Backend | Jesús Iván Sosa Báez | `12576c4` | Completo |
| 10/09/2026 | Creación de los documentos de contexto | Documentación | Jesús Iván Sosa Báez | `dbdd949` | Completo |
| 10/09/2026 | Actualización de exclusiones del repositorio | Configuración | Jesús Iván Sosa Báez | `7c46e79` | Completo |
| 15/09/2026 | Conversión de la documentación oficial y diseño inicial de la base de datos | Documentación y datos | Jesús Iván Sosa Báez | [PENDIENTE: completar después del commit] | En curso |

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
