# Sistema de Gestión Hospitalaria

Sistema web para la administración de un hospital. El **diseño** cubre pacientes (incluyendo menores de edad con responsable legal), médicos y horarios, citas, consultas/diagnósticos, recetas, farmacia, laboratorio clínico, imágenes médicas, notificaciones, facturación, reportes y bitácora de auditoría. El **prototipo funcional** de este entregable implementa el núcleo del sistema (ver sección "Alcance implementado" abajo).

> **Nota de stack:** los Requerimientos No Funcionales originales del cliente indicaban C#/.NET 9, Oracle Database y Windows Server 2025. Por decisión de curso, este proyecto se documenta e implementa en **Python (FastAPI) + Angular + SQLite**.

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

- [Diseño ER](docs/01_Diseño_ER.md) — Modelo de datos completo del sistema (16 entidades) y diagrama Mermaid
- [Requerimientos](docs/02_Requerimientos.md) — Funcionales, No Funcionales, Reglas de Negocio y Restricciones
- [Riesgos](docs/03_Riesgos.md) — Riesgos identificados con probabilidad, impacto y mitigación
- [Guía de documentación en Notion](docs/04_Documentacion_Notion.md)
- [Guía del mapa en Miro](docs/05_Mapa_Miro_Guia.md)

## Alcance implementado en este prototipo

El [Diseño ER](docs/01_Diseño_ER.md) describe el modelo de datos completo pensado para el sistema. Por el tiempo disponible en el curso, el prototipo funcional de este entregable implementa únicamente el núcleo:

**Implementado (backend + frontend funcionando):**
- [x] Pacientes — listar, crear, obtener por ID
- [x] Médicos — listar, crear
- [x] Citas — listar, crear

**Diseñado pero no implementado en este prototipo** (quedan documentados en el ER y los requerimientos para una siguiente iteración):
- [ ] Especialidades y horarios médicos
- [ ] Consultas y recetas
- [ ] Laboratorio (órdenes y resultados)
- [ ] Farmacia (inventario de medicamentos)
- [ ] Facturación
- [ ] Imágenes médicas
- [ ] Notificaciones
- [ ] Bitácora de auditoría
- [ ] Autenticación de usuarios por rol

## Cómo correr el proyecto localmente

> Este proyecto fue desarrollado y probado en **Linux (Fedora)**. A continuación se incluyen los comandos tanto para Linux/macOS como para Windows.

### Backend

**Requisitos:** Python 3.10 o superior.

#### Linux / macOS

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

#### Windows (PowerShell o CMD)

```powershell
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

En ambos casos, el backend queda disponible en `http://localhost:8000`. Documentación interactiva (Swagger) en `http://localhost:8000/docs`.

> **Nota para Windows:** si `python` no es reconocido como comando, verifica que Python esté instalado y agregado al PATH durante la instalación. Si `activate` da error de permisos en PowerShell, ejecuta primero: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`.

### Frontend

**Requisitos:** Node.js 18 o superior (incluye npm).

#### Linux / macOS / Windows (mismo comando en los tres)

```bash
cd frontend
npm install
npm start
```

El frontend queda disponible en `http://localhost:4200`.

> **Nota para Windows:** si no tienes Node.js instalado, descárgalo desde [nodejs.org](https://nodejs.org) (versión LTS) y verifica con `node -v` y `npm -v` en una terminal nueva antes de correr `npm install`.

## Tecnologías

- **Backend:** Python, FastAPI, SQLAlchemy, SQLite
- **Frontend:** Angular (standalone components), Angular Material
- **Documentación de proceso:** ER en Mermaid, requerimientos y riesgos versionados junto al código
