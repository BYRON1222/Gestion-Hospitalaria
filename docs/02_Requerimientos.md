# Requerimientos — Sistema de Gestión Hospitalaria

> Nota de stack: los Requerimientos No Funcionales entregados originalmente por el cliente indicaban C#/.NET 9, Oracle Database y Windows Server 2025. Por decisión de curso, este proyecto se documenta e implementa completamente en **Python (FastAPI) y Angular**, con **PostgreSQL/SQLite** como base de datos.

## 1. Requerimientos Funcionales

### Pacientes
- RF01: Los recepcionistas deben poder registrar nuevos pacientes.
- RF02: Los pacientes menores de edad deben quedar asociados a un responsable legal.
- RF03: El personal médico debe poder consultar el historial clínico completo de un paciente.

### Médicos y horarios
- RF04: Los administradores podrán configurar los horarios de atención de cada especialista.

### Citas
- RF05: El sistema permitirá programar citas médicas desde dispositivos móviles.
- RF06: Los pacientes podrán solicitar citas mediante una aplicación móvil.
- RF07: Los pacientes podrán visualizar el estado de sus citas.
- RF08: El sistema deberá enviar recordatorios automáticos por correo electrónico y SMS.

### Consultas y recetas
- RF09: Los médicos podrán registrar diagnósticos y tratamientos.
- RF10: Los médicos deberán firmar electrónicamente las recetas emitidas.

### Laboratorio
- RF11: El laboratorio deberá registrar automáticamente los resultados de los exámenes realizados.
- RF12: El sistema deberá integrarse con el laboratorio clínico externo.
- RF13: Los pacientes podrán descargar sus resultados de laboratorio en formato PDF.
- RF14: El sistema deberá enviar una notificación automática al médico cuando un resultado de laboratorio sea clasificado como crítico.

### Imágenes médicas
- RF15: El sistema permitirá registrar imágenes médicas como radiografías y tomografías.

### Farmacia
- RF16: El módulo de farmacia deberá controlar automáticamente el inventario de medicamentos.

### Administración / Reportes / Auditoría
- RF17: Los administradores deberán generar reportes mensuales de ingresos.
- RF18: El sistema deberá generar indicadores estadísticos para la dirección del hospital.
- RF19: El sistema deberá registrar una bitácora de todas las acciones realizadas por los usuarios.

## 2. Requerimientos No Funcionales

| Código | Requerimiento del cliente (original) | Adaptación para este proyecto |
|---|---|---|
| RNF01 | Responder cualquier consulta en menos de 3 segundos | Se mantiene igual |
| RNF02 | Funcionar en Chrome, Edge y Firefox | Se mantiene igual |
| RNF03 | Almacenar información médica en Oracle Database | Adaptado: PostgreSQL (SQLite en desarrollo) |
| RNF04 | Infraestructura en Windows Server 2025 | Adaptado: entorno Linux/contenedores para el prototipo académico |
| RNF05 | Disponibilidad 24/7 todo el año | Se documenta como meta de diseño |
| RNF06 | Registrar una consulta en máximo 5 minutos | Se mantiene igual, validado en el flujo de UI |
| RNF07 | Autenticación multifactor (MFA) | Se mantiene igual: MFA simplificado en backend |
| RNF08 | Lenguaje C# sobre .NET 9 | Reemplazado: Python (FastAPI) |
| RNF09 | Cambio de contraseña cada 90 días | Se mantiene igual |
| RNF10 | Soportar 800 usuarios concurrentes | Meta de diseño, no probado con carga real |
| RNF11 | Backups automáticos cada noche | Se mantiene igual |
| RNF12 | Cumplir legislación de protección de datos personales | Se mantiene igual |
| RNF13 | Cifrado AES-256 para datos sensibles | Se mantiene igual |

## 3. Reglas de Negocio

- RN01: Ningún paciente podrá tener dos citas médicas a la misma hora con el mismo especialista.
- RN02: Los medicamentos únicamente podrán ser despachados cuando exista una receta médica vigente.
- RN03: Ningún usuario podrá eliminar expedientes médicos definitivamente (borrado lógico obligatorio).
- RN04: Los pacientes menores de edad deberán estar asociados a un responsable legal.
- RN05: Los médicos únicamente podrán visualizar la información de los pacientes asignados a ellos.
- RN06: Ninguna factura podrá emitirse si el paciente posee pagos pendientes de consultas anteriores.
- RN07: Ningún empleado podrá modificar una factura que ya haya sido pagada.

## 4. Restricciones de Proyecto

- Presupuesto máximo referencial del cliente: Q850,000.
- Plazo máximo deseado por el cliente: 6 meses (ajustado al plazo de entrega del curso para el ejercicio académico).
