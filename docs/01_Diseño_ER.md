# Diseño ER — Sistema de Gestión Hospitalaria

## 1. Enfoque de diseño

El dominio se dividió en 6 áreas funcionales para que el modelo sea defendible en una revisión oral (no es solo "Paciente-Médico-Cita" genérico, sino que cubre el ciclo completo: consulta externa, internamiento, historial clínico, farmacia y facturación):

1. **Personal clínico** — Especialidad, Medico, Enfermero, Departamento
2. **Atención ambulatoria** — Cita
3. **Internamiento** — Habitacion, Cama, Internamiento
4. **Historial clínico** — HistorialMedico, Receta, Medicamento
5. **Facturación y seguros** — Factura, DetalleFactura, Seguro
6. **Acceso al sistema** — Usuario (login con roles)

Esta separación es justo lo que un profesor busca al pedir "requerimientos clasificados": que el modelo refleje procesos reales del hospital, no solo tablas sueltas.

## 2. Diagrama Mermaid (ER)

Pega esto tal cual en cualquier visor de Mermaid (mermaid.live, la extensión de VS Code, o directamente en Notion si tu plan lo soporta):

```mermaid
erDiagram
    ESPECIALIDAD ||--o{ MEDICO : agrupa
    DEPARTAMENTO ||--o{ MEDICO : emplea
    DEPARTAMENTO ||--o{ HABITACION : contiene
    HABITACION ||--o{ CAMA : tiene

    PACIENTE ||--o{ CITA : agenda
    MEDICO ||--o{ CITA : atiende

    PACIENTE ||--o{ INTERNAMIENTO : ingresa
    MEDICO ||--o{ INTERNAMIENTO : supervisa
    CAMA ||--o| INTERNAMIENTO : asignada_a

    PACIENTE ||--o{ HISTORIAL_MEDICO : posee
    MEDICO ||--o{ HISTORIAL_MEDICO : registra
    HISTORIAL_MEDICO ||--o{ RECETA : genera
    MEDICAMENTO ||--o{ RECETA : incluida_en

    PACIENTE ||--o{ FACTURA : recibe
    FACTURA ||--o{ DETALLE_FACTURA : compuesta_de
    PACIENTE ||--o| SEGURO : posee

    USUARIO ||--o| MEDICO : es
    USUARIO ||--o| ENFERMERO : es

    PACIENTE {
        int id PK
        string nombre
        string apellido
        date fecha_nacimiento
        string genero
        string documento_identidad
        string telefono
        string email
        string direccion
        string tipo_sangre
        date fecha_registro
    }
    ESPECIALIDAD {
        int id PK
        string nombre
        string descripcion
    }
    DEPARTAMENTO {
        int id PK
        string nombre
        string ubicacion
        int jefe_medico_id FK
    }
    MEDICO {
        int id PK
        string nombre
        string apellido
        int especialidad_id FK
        int departamento_id FK
        string numero_colegiado
        string telefono
        string email
        date fecha_contratacion
    }
    ENFERMERO {
        int id PK
        string nombre
        string apellido
        int departamento_id FK
        string turno
        string telefono
    }
    HABITACION {
        int id PK
        string numero
        int departamento_id FK
        string tipo
    }
    CAMA {
        int id PK
        int habitacion_id FK
        string codigo
        string estado
    }
    CITA {
        int id PK
        int paciente_id FK
        int medico_id FK
        datetime fecha_hora
        string motivo
        string estado
    }
    INTERNAMIENTO {
        int id PK
        int paciente_id FK
        int medico_id FK
        int cama_id FK
        datetime fecha_ingreso
        datetime fecha_alta
        string diagnostico_ingreso
    }
    HISTORIAL_MEDICO {
        int id PK
        int paciente_id FK
        int medico_id FK
        date fecha
        string diagnostico
        string tratamiento
        string observaciones
    }
    MEDICAMENTO {
        int id PK
        string nombre
        string descripcion
        int stock
        decimal precio_unitario
    }
    RECETA {
        int id PK
        int historial_medico_id FK
        int medicamento_id FK
        string dosis
        string frecuencia
        string duracion
    }
    FACTURA {
        int id PK
        int paciente_id FK
        date fecha
        decimal monto_total
        string estado_pago
    }
    DETALLE_FACTURA {
        int id PK
        int factura_id FK
        string concepto
        int cantidad
        decimal precio_unitario
        decimal subtotal
    }
    SEGURO {
        int id PK
        int paciente_id FK
        string aseguradora
        string numero_poliza
        string cobertura
    }
    USUARIO {
        int id PK
        string nombre_usuario
        string password_hash
        string rol
        int medico_id FK
        int enfermero_id FK
    }
```

## 3. Decisiones de modelado que puedes explicar en la entrega

- **Cama vs Habitación**: se separaron porque una habitación puede tener varias camas (realismo hospitalario). El internamiento se asocia a la **cama**, no a la habitación completa.
- **Historial médico independiente de la cita/internamiento**: un registro clínico puede originarse en una consulta ambulatoria o durante un internamiento, así que se modeló como entidad propia en vez de duplicar campos en ambas.
- **Receta ligada al historial, no al paciente directamente**: evita recetas "flotantes" sin respaldo clínico — trazabilidad total (por qué se prescribió ese medicamento).
- **Usuario separado de Médico/Enfermero**: el login es un concepto de sistema, no clínico. Así un mismo empleado puede cambiar de rol sin tocar sus datos clínicos, y permite agregar roles como "Recepcionista" o "Administrador" sin forzar una fila médica falsa.
- **Normalización**: el modelo está en 3FN — no hay atributos derivados almacenados (ej. la edad no se guarda, se calcula desde `fecha_nacimiento`; el `monto_total` de factura podría auditarse contra la suma de `detalle_factura`, pero se mantiene desnormalizado por rendimiento, algo que puedes mencionar como decisión consciente, no error).
