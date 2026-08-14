# Diseño ER — Sistema de Gestión Hospitalaria

## 1. Entidades

- **Paciente**: id_paciente (PK), nombre, apellido, fecha_nacimiento, genero, dpi, telefono, email, direccion, tipo_sangre, contacto_emergencia, fecha_registro
- **Medico**: id_medico (PK), nombre, apellido, num_colegiado, telefono, email, id_especialidad (FK)
- **Especialidad**: id_especialidad (PK), nombre, descripcion
- **Usuario**: id_usuario (PK), username, password_hash, rol, id_referencia, activo
- **Cita**: id_cita (PK), id_paciente (FK), id_medico (FK), fecha, hora, estado, motivo
- **Consulta**: id_consulta (PK), id_cita (FK), diagnostico, tratamiento, observaciones, fecha
- **Receta**: id_receta (PK), id_consulta (FK), fecha_emision
- **Medicamento**: id_medicamento (PK), nombre, descripcion, stock, precio
- **DetalleReceta**: id_detalle (PK), id_receta (FK), id_medicamento (FK), dosis, cantidad
- **Habitacion**: id_habitacion (PK), numero, tipo, piso, estado
- **Internamiento**: id_internamiento (PK), id_paciente (FK), id_habitacion (FK), fecha_ingreso, fecha_alta, motivo
- **Factura**: id_factura (PK), id_paciente (FK), monto_total, fecha, estado, concepto

## 2. Diagrama ER (Mermaid)

```mermaid
erDiagram
    PACIENTE ||--o{ CITA : agenda
    MEDICO ||--o{ CITA : atiende
    MEDICO }o--|| ESPECIALIDAD : pertenece
    CITA ||--o| CONSULTA : genera
    CONSULTA ||--o{ RECETA : produce
    RECETA ||--o{ DETALLE_RECETA : contiene
    MEDICAMENTO ||--o{ DETALLE_RECETA : incluido_en
    PACIENTE ||--o{ INTERNAMIENTO : registra
    HABITACION ||--o{ INTERNAMIENTO : asignada_a
    PACIENTE ||--o{ FACTURA : recibe
    USUARIO ||--o| MEDICO : es
    USUARIO ||--o| PACIENTE : accede_como

    PACIENTE {
        int id_paciente PK
        string nombre
        string apellido
        date fecha_nacimiento
        string genero
        string dpi
        string telefono
        string email
        string tipo_sangre
        date fecha_registro
    }
    MEDICO {
        int id_medico PK
        string nombre
        string apellido
        string num_colegiado
        string telefono
        int id_especialidad FK
    }
    ESPECIALIDAD {
        int id_especialidad PK
        string nombre
        string descripcion
    }
    CITA {
        int id_cita PK
        int id_paciente FK
        int id_medico FK
        date fecha
        time hora
        string estado
        string motivo
    }
    CONSULTA {
        int id_consulta PK
        int id_cita FK
        string diagnostico
        string tratamiento
        string observaciones
        date fecha
    }
    RECETA {
        int id_receta PK
        int id_consulta FK
        date fecha_emision
    }
    MEDICAMENTO {
        int id_medicamento PK
        string nombre
        string descripcion
        int stock
        float precio
    }
    DETALLE_RECETA {
        int id_detalle PK
        int id_receta FK
        int id_medicamento FK
        string dosis
        int cantidad
    }
    HABITACION {
        int id_habitacion PK
        string numero
        string tipo
        int piso
        string estado
    }
    INTERNAMIENTO {
        int id_internamiento PK
        int id_paciente FK
        int id_habitacion FK
        date fecha_ingreso
        date fecha_alta
        string motivo
    }
    FACTURA {
        int id_factura PK
        int id_paciente FK
        float monto_total
        date fecha
        string estado
    }
    USUARIO {
        int id_usuario PK
        string username
        string password_hash
        string rol
        boolean activo
    }
```

> GitHub renderiza este bloque Mermaid automáticamente en la vista del `.md`. También puede pegarse en [mermaid.live](https://mermaid.live) para exportar como imagen.
