# Diseño ER — Sistema de Gestión Hospitalaria

## 1. Entidades

- **Paciente**: id_paciente (PK), nombre, apellido, fecha_nacimiento, genero, dpi, telefono, email, direccion, tipo_sangre, es_menor_edad, id_responsable_legal (FK, nullable), activo, fecha_registro
- **ResponsableLegal**: id_responsable (PK), nombre, apellido, parentesco, dpi, telefono
- **Medico**: id_medico (PK), nombre, apellido, num_colegiado, telefono, email, id_especialidad (FK)
- **Especialidad**: id_especialidad (PK), nombre, descripcion
- **HorarioMedico**: id_horario (PK), id_medico (FK), dia_semana, hora_inicio, hora_fin
- **Usuario**: id_usuario (PK), username, password_hash, rol [admin|medico|enfermeria|recepcion|paciente], mfa_habilitado, fecha_ultimo_cambio_password, activo
- **Cita**: id_cita (PK), id_paciente (FK), id_medico (FK), fecha, hora, canal [web|movil], estado [pendiente|confirmada|cancelada|atendida], motivo
- **Consulta**: id_consulta (PK), id_cita (FK), diagnostico, tratamiento, observaciones, fecha
- **Receta**: id_receta (PK), id_consulta (FK), fecha_emision, firma_electronica
- **Medicamento**: id_medicamento (PK), nombre, descripcion, stock, precio
- **DetalleReceta**: id_detalle (PK), id_receta (FK), id_medicamento (FK), dosis, cantidad
- **OrdenLaboratorio**: id_orden (PK), id_consulta (FK), id_medico_solicita (FK), fecha_solicitud, estado [pendiente|completada]
- **ResultadoLaboratorio**: id_resultado (PK), id_orden (FK), tipo_examen, resultado_texto, archivo_pdf, clasificacion [normal|critico], fecha_resultado
- **ImagenMedica**: id_imagen (PK), id_paciente (FK), id_medico (FK), tipo [radiografia|tomografia|otro], archivo, fecha
- **Factura**: id_factura (PK), id_paciente (FK), monto_total, fecha, estado [pendiente|pagada], concepto
- **Notificacion**: id_notificacion (PK), id_usuario (FK), tipo [email|sms], mensaje, fecha_envio, estado [enviado|pendiente|fallido]
- **Bitacora**: id_bitacora (PK), id_usuario (FK), accion, entidad_afectada, fecha, detalle

## 2. Diagrama ER (Mermaid)

```mermaid
erDiagram
    RESPONSABLE_LEGAL ||--o{ PACIENTE : responde_por
    PACIENTE ||--o{ CITA : agenda
    PACIENTE ||--o{ IMAGEN_MEDICA : posee
    PACIENTE ||--o{ FACTURA : recibe
    MEDICO ||--o{ CITA : atiende
    MEDICO }o--|| ESPECIALIDAD : pertenece
    MEDICO ||--o{ HORARIO_MEDICO : tiene
    MEDICO ||--o{ IMAGEN_MEDICA : registra
    MEDICO ||--o{ ORDEN_LABORATORIO : solicita
    CITA ||--o| CONSULTA : genera
    CONSULTA ||--o{ RECETA : produce
    CONSULTA ||--o{ ORDEN_LABORATORIO : origina
    RECETA ||--o{ DETALLE_RECETA : contiene
    MEDICAMENTO ||--o{ DETALLE_RECETA : incluido_en
    ORDEN_LABORATORIO ||--o{ RESULTADO_LABORATORIO : produce
    USUARIO ||--o{ NOTIFICACION : recibe
    USUARIO ||--o{ BITACORA : genera
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
        boolean es_menor_edad
        int id_responsable_legal FK
        boolean activo
        date fecha_registro
    }
    RESPONSABLE_LEGAL {
        int id_responsable PK
        string nombre
        string apellido
        string parentesco
        string dpi
        string telefono
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
    HORARIO_MEDICO {
        int id_horario PK
        int id_medico FK
        string dia_semana
        time hora_inicio
        time hora_fin
    }
    USUARIO {
        int id_usuario PK
        string username
        string password_hash
        string rol
        boolean mfa_habilitado
        date fecha_ultimo_cambio_password
        boolean activo
    }
    CITA {
        int id_cita PK
        int id_paciente FK
        int id_medico FK
        date fecha
        time hora
        string canal
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
        string firma_electronica
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
    ORDEN_LABORATORIO {
        int id_orden PK
        int id_consulta FK
        int id_medico_solicita FK
        date fecha_solicitud
        string estado
    }
    RESULTADO_LABORATORIO {
        int id_resultado PK
        int id_orden FK
        string tipo_examen
        string resultado_texto
        string archivo_pdf
        string clasificacion
        date fecha_resultado
    }
    IMAGEN_MEDICA {
        int id_imagen PK
        int id_paciente FK
        int id_medico FK
        string tipo
        string archivo
        date fecha
    }
    FACTURA {
        int id_factura PK
        int id_paciente FK
        float monto_total
        date fecha
        string estado
        string concepto
    }
    NOTIFICACION {
        int id_notificacion PK
        int id_usuario FK
        string tipo
        string mensaje
        date fecha_envio
        string estado
    }
    BITACORA {
        int id_bitacora PK
        int id_usuario FK
        string accion
        string entidad_afectada
        date fecha
        string detalle
    }
```

> GitHub renderiza este bloque Mermaid automáticamente en la vista del `.md`. También puede pegarse en [mermaid.live](https://mermaid.live) para exportar como imagen.

## 3. Reglas de negocio reflejadas en el modelo

- RN01 (doble cita): restricción única en `Cita` sobre (id_medico, fecha, hora).
- RN02 (receta vigente): `DetalleReceta` solo puede crearse si la `Receta` asociada está vigente.
- RN03 (no borrado definitivo): `Paciente.activo` y equivalentes en otras entidades clínicas → borrado lógico.
- RN04 (menor de edad): `Paciente.es_menor_edad = true` obliga a `id_responsable_legal` no nulo.
- RN05 (médico ve solo sus pacientes): filtro por `id_medico` reforzado por rol en `Usuario`.
- RN06 (factura con pagos pendientes): validación antes de crear una `Factura` nueva.
- RN07 (factura pagada no modificable): validación de estado antes de actualizar una `Factura`.
