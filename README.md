# Sistema de Gestión Hospitalaria

Sistema web para la administración de un hospital: pacientes (incluyendo menores de edad con responsable legal), médicos y horarios, citas (web y móvil), consultas/diagnósticos, recetas con firma electrónica, farmacia/inventario, laboratorio clínico, imágenes médicas, notificaciones automáticas, facturación, reportes y bitácora de auditoría.

> **Nota de stack:** los Requerimientos No Funcionales originales del cliente indicaban C#/.NET 9, Oracle Database y Windows Server 2025. Por decisión de curso, este proyecto se documenta e implementa completamente en **Python (FastAPI) + Angular + SQLite/PostgreSQL**.

## Estructura del repositorio

```
Gestion-Hospitalaria/
├── backend/       ← API REST en FastAPI (Python)
├── frontend/       ← Interfaz en Angular (Angular Material)
├── docs/
│   ├── 01_Diseño_ER.md
│   ├── 02_Requerimientos.md
│   ├── 03_Riesgos.md
│   ├── 04_Documentacion_Notion.md
│   └── 05_Mapa_Miro_Guia.md
└── README.md
```

## Documentación del proyecto

- [Diseño ER](docs/01_Diseño_ER.md) — Entidades, relaciones y diagrama Mermaid
- [Requerimientos](docs/02_Requerimientos.md) — Funcionales, No Funcionales, Reglas de Negocio y Restricciones
- [Riesgos](docs/03_Riesgos.md) — Riesgos identificados con probabilidad, impacto y mitigación
- [Guía de documentación en Notion](docs/04_Documentacion_Notion.md)
- [Guía del mapa en Miro](docs/05_Mapa_Miro_Guia.md)

## Cómo correr el proyecto localmente

### Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

El backend queda disponible en `http://localhost:8000`. Documentación interactiva (Swagger) en `http://localhost:8000/docs`.

### Frontend

```bash
cd frontend
npm install
npm start
```

El frontend queda disponible en `http://localhost:4200`.

## Tecnologías

- **Backend:** Python, FastAPI, SQLAlchemy, SQLite (desarrollo) / PostgreSQL (producción)
- **Frontend:** Angular (standalone components), Angular Material
- **Autenticación:** JWT con verificación MFA simplificada
- **Documentación de proceso:** ER en Mermaid, requerimientos y riesgos versionados junto al código

## Módulos implementados (MVP)

- [x] Usuarios y autenticación por rol
- [x] Pacientes (con responsable legal para menores)
- [x] Médicos, especialidades y horarios
- [x] Citas (con validación de disponibilidad)
- [ ] Consultas y recetas
- [ ] Laboratorio
- [ ] Farmacia
- [ ] Facturación
- [ ] Imágenes médicas
- [ ] Bitácora / auditoría visible en UI
- [ ] Reportes e indicadores
