# Requerimientos — Sistema de Gestión Hospitalaria

## 1. Requerimientos Funcionales

### Pacientes
- RF01: El sistema debe permitir registrar un nuevo paciente (datos personales, tipo de sangre, contacto de emergencia).
- RF02: El sistema debe permitir buscar pacientes por nombre, DPI/CUI o número de expediente.
- RF03: El sistema debe permitir editar y dar de baja (lógica) a un paciente.
- RF04: El sistema debe mostrar el historial clínico completo de un paciente.

### Médicos
- RF05: El sistema debe permitir registrar médicos con su especialidad y número de colegiado.
- RF06: El sistema debe permitir asignar horarios/disponibilidad a cada médico.

### Citas
- RF07: El sistema debe permitir agendar una cita seleccionando paciente, médico y horario disponible.
- RF08: El sistema debe validar que no existan cruces de horario para un mismo médico.
- RF09: El sistema debe permitir cancelar o reprogramar citas.
- RF10: El sistema debe notificar (en pantalla o email) el estado de la cita.

### Consultas / Historial Clínico
- RF11: El sistema debe permitir registrar diagnóstico, tratamiento y observaciones asociados a una cita atendida.
- RF12: El sistema debe permitir generar una receta médica ligada a una consulta.

### Internamiento
- RF13: El sistema debe permitir registrar el ingreso de un paciente a una habitación disponible.
- RF14: El sistema debe controlar el estado de las habitaciones (disponible, ocupada, mantenimiento).
- RF15: El sistema debe registrar la fecha de alta y motivo de egreso.

### Medicamentos / Farmacia
- RF16: El sistema debe llevar el inventario de medicamentos (stock, precio).
- RF17: El sistema debe descontar stock automáticamente al despachar una receta.

### Facturación
- RF18: El sistema debe generar una factura por consulta, internamiento o medicamentos.
- RF19: El sistema debe permitir consultar el historial de pagos de un paciente.

### Seguridad / Usuarios
- RF20: El sistema debe autenticar usuarios por rol (Administrador, Médico, Enfermería, Recepción).
- RF21: El sistema debe restringir el acceso a módulos según el rol del usuario.

## 2. Requerimientos No Funcionales

| Código | Requerimiento | Categoría |
|---|---|---|
| RNF01 | El sistema debe responder en menos de 2 segundos ante operaciones CRUD comunes | Rendimiento |
| RNF02 | El sistema debe cifrar contraseñas y proteger datos sensibles del paciente | Seguridad |
| RNF03 | El sistema debe ser responsivo (usable en tablet/escritorio) | Usabilidad |
| RNF04 | El sistema debe validar datos tanto en frontend como backend | Confiabilidad |
| RNF05 | El sistema debe mantener disponibilidad 99% en horario hospitalario | Disponibilidad |
| RNF06 | El código debe seguir arquitectura por capas (separación backend/frontend vía API REST) | Mantenibilidad |
| RNF07 | El sistema debe registrar logs de acciones críticas (auditoría) | Trazabilidad |
| RNF08 | La interfaz debe seguir un solo sistema de diseño consistente (paleta, tipografía) | Usabilidad |
