# Requerimientos Clasificados — Sistema de Gestión Hospitalaria

Clasificación en dos ejes: **tipo** (Funcional / No Funcional) y **prioridad** (método MoSCoW: Must / Should / Could / Won't). Esto es lo que distingue una entrega de "IA genérica" — la mayoría solo lista requisitos sueltos sin priorizar ni justificar.

## 1. Requerimientos Funcionales (RF)

### Módulo: Gestión de Pacientes
| ID | Requerimiento | Prioridad |
|---|---|---|
| RF-01 | El sistema debe permitir registrar, editar y consultar pacientes (datos personales, tipo de sangre, seguro) | Must |
| RF-02 | El sistema debe permitir buscar pacientes por nombre o documento de identidad | Must |
| RF-03 | El sistema debe validar que el documento de identidad no se repita | Should |

### Módulo: Citas
| ID | Requerimiento | Prioridad |
|---|---|---|
| RF-04 | El sistema debe permitir agendar citas asociando paciente, médico, fecha y motivo | Must |
| RF-05 | El sistema debe evitar doble reserva del mismo médico en el mismo horario | Must |
| RF-06 | El sistema debe permitir cancelar o reprogramar una cita | Should |
| RF-07 | El sistema debe enviar recordatorio de cita (correo o notificación) | Could |

### Módulo: Internamiento
| ID | Requerimiento | Prioridad |
|---|---|---|
| RF-08 | El sistema debe permitir registrar el ingreso de un paciente asignándole cama disponible | Must |
| RF-09 | El sistema debe actualizar el estado de la cama (disponible/ocupada) automáticamente al ingresar o dar de alta | Must |
| RF-10 | El sistema debe permitir registrar el alta médica con diagnóstico final | Should |

### Módulo: Historial Clínico
| ID | Requerimiento | Prioridad |
|---|---|---|
| RF-11 | El sistema debe permitir a un médico registrar diagnóstico, tratamiento y observaciones por paciente | Must |
| RF-12 | El sistema debe mostrar el historial clínico completo y cronológico de un paciente | Must |
| RF-13 | El sistema debe permitir emitir recetas ligadas a un registro del historial | Should |

### Módulo: Farmacia / Inventario
| ID | Requerimiento | Prioridad |
|---|---|---|
| RF-14 | El sistema debe descontar stock de medicamento al emitir una receta | Should |
| RF-15 | El sistema debe alertar cuando el stock de un medicamento esté por debajo de un umbral | Could |

### Módulo: Facturación
| ID | Requerimiento | Prioridad |
|---|---|---|
| RF-16 | El sistema debe generar una factura con el detalle de servicios prestados a un paciente | Must |
| RF-17 | El sistema debe reflejar si la factura está cubierta total o parcialmente por seguro | Should |

### Módulo: Seguridad y Acceso
| ID | Requerimiento | Prioridad |
|---|---|---|
| RF-18 | El sistema debe autenticar usuarios con usuario/contraseña | Must |
| RF-19 | El sistema debe restringir funcionalidades según rol (admin, médico, enfermero, recepción) | Must |

## 2. Requerimientos No Funcionales (RNF)

| ID | Requerimiento | Categoría | Prioridad |
|---|---|---|---|
| RNF-01 | Las contraseñas deben almacenarse con hash (nunca en texto plano) | Seguridad | Must |
| RNF-02 | Los datos clínicos son sensibles: solo roles autorizados pueden verlos (principio de mínimo privilegio) | Seguridad / Cumplimiento | Must |
| RNF-03 | El tiempo de respuesta de consultas comunes (buscar paciente, listar citas) debe ser menor a 2 segundos | Rendimiento | Should |
| RNF-04 | La interfaz debe ser usable por personal no técnico (recepción, enfermería) sin capacitación extensa | Usabilidad | Must |
| RNF-05 | El sistema debe registrar quién y cuándo modificó un historial clínico (auditoría) | Cumplimiento | Should |
| RNF-06 | El backend debe exponer una API documentada (facilita mantenimiento e integración futura) | Mantenibilidad | Should |
| RNF-07 | El sistema debe poder escalar horizontalmente si crece el número de pacientes/hospitales | Escalabilidad | Could |
| RNF-08 | El código debe seguir una arquitectura en capas (separar modelos, lógica de negocio y presentación) | Mantenibilidad | Must |

## 3. Nota metodológica para la entrega

Puedes explicar que se usó **MoSCoW** porque en un sistema hospitalario real no todo tiene el mismo peso: lo que protege datos de pacientes o evita errores médicos (RF-05, RF-09, RNF-01, RNF-02) es innegociable (*Must*), mientras que comodidades como recordatorios por correo (RF-07) son deseables pero no bloquean la operación (*Could*).
