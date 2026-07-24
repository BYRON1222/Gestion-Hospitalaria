# Sistema de Gestión Hospitalaria — Documentación del Proyecto

## 1. Resumen del proyecto

Sistema web para gestionar la operación de un hospital: pacientes, citas, internamientos, historiales clínicos, farmacia y facturación, con control de acceso por rol.

- **Backend:** Python (FastAPI + SQLAlchemy)
- **Frontend:** Angular
- **Base de datos:** PostgreSQL (o SQLite para desarrollo local)

## 2. Objetivos

1. Centralizar la información de pacientes y su historial clínico.
2. Evitar errores operativos comunes (doble reserva de cama/médico).
3. Dar trazabilidad completa: qué médico atendió, qué se recetó, qué se facturó.

## 3. Alcance (MVP vs. futuro)

**Dentro del alcance (MVP — requerimientos "Must"):** registro de pacientes, agenda de citas, internamiento con asignación de cama, historial clínico, facturación básica, autenticación con roles.

**Fuera del alcance de esta entrega:** recordatorios automáticos por correo, alertas de inventario, escalabilidad multi-hospital.

## 4. Diseño ER

Resumen de entidades: Paciente, Médico, Enfermero, Especialidad, Departamento, Habitación, Cama, Cita, Internamiento, Historial Médico, Receta, Medicamento, Factura, Detalle Factura, Seguro, Usuario.

(El diagrama ER completo está en la página "Diseño ER" / bloque Mermaid correspondiente.)


## 5. Requerimientos

*(Ver `02_Requerimientos.md` para la tabla completa clasificada por módulo y prioridad MoSCoW.)*

## 6. Riesgos

*(Ver `03_Riesgos.md` para la matriz completa.)*

## 7. Arquitectura técnica

```
[Angular Frontend] --HTTP/JSON--> [API FastAPI] --SQLAlchemy--> [PostgreSQL]
```

- El frontend consume la API vía servicios HTTP (uno por entidad: PacienteService, CitaService, etc.)
- El backend expone endpoints REST documentados automáticamente en `/docs` (Swagger, incluido gratis con FastAPI)
- Los modelos de SQLAlchemy reflejan 1:1 el diagrama ER

## 8. Estructura de carpetas del repositorio

```
hospital-management-system/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   └── schemas.py
│   └── requirements.txt
├── frontend/
│   └── src/app/
│       ├── models/
│       ├── services/
│       └── components/
└── docs/
    ├── 01_Diseno_ER.md
    ├── 02_Requerimientos.md
    ├── 03_Riesgos.md
    └── 05_Mapa_Miro_Guia.md
```

## 9. Próximos pasos después de la entrega

- Agregar pruebas automatizadas (pytest para backend, Jasmine/Karma para Angular)
- Implementar los requerimientos "Should" y "Could" pendientes
- Migrar de SQLite a PostgreSQL en producción
