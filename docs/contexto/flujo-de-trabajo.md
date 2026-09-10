# Flujo de trabajo actual

## Preparar el frontend

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

## Preparar el backend

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
fastapi dev app/main.py
```

Ejecutar pruebas:

```powershell
python -m pytest
```

## Checklist mínimo de terminado

- El proyecto afectado compila o arranca.
- Las pruebas existentes pasan.
- El lint del frontend pasa cuando se modifica TypeScript.
- La documentación relacionada refleja el cambio.
- No se agregan secretos ni archivos ignorados.

## Deploy

[PENDIENTE: no existe configuración ni procedimiento de despliegue.]
