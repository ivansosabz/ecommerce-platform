# Convenciones observadas

## Código

- Python usa módulos y funciones en `snake_case`, cuatro espacios y anotaciones de retorno.
- TypeScript usa componentes en `PascalCase`, comillas simples y código sin punto y coma.
- El frontend conserva las reglas generadas por Oxlint.
- Las pruebas Python se ubican en `backend/tests` y usan nombres `test_*.py`.

## Dependencias

- Las dependencias de ejecución del backend están en `requirements.txt`.
- Las dependencias de desarrollo están en `requirements-dev.txt`.
- El frontend usa `package.json` y `package-lock.json`.
- Los secretos y entornos locales se excluyen mediante `.gitignore`.

## Commits

El historial utiliza prefijos `feat`, `docs` y `chore`. Los nuevos cambios siguen Conventional Commits y se agrupan por responsabilidad. El trabajo actual continúa en `codex/refine-database-model`; las ramas nuevas creadas con Codex usan el prefijo `codex/`.

## Patrones prohibidos

[PENDIENTE: no hay patrones prohibidos documentados en el repositorio.]
