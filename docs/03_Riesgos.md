# Identificación de Riesgos — Sistema de Gestión Hospitalaria

Cada riesgo tiene **Probabilidad** (Alta/Media/Baja), **Impacto** (Alto/Medio/Bajo) y una **estrategia de mitigación concreta** — no genérica ("tener cuidado" no es mitigación real, y un profesor lo nota).

## Matriz de riesgos

| ID | Riesgo | Categoría | Probabilidad | Impacto | Mitigación |
|---|---|---|---|---|---|
| R-01 | Exposición o filtración de datos clínicos de pacientes | Seguridad de datos | Media | Alto | Cifrado en tránsito (HTTPS) y en reposo para campos sensibles; control de acceso por rol; nunca loguear datos clínicos en texto plano |
| R-02 | Doble asignación de la misma cama o del mismo horario médico | Integridad de datos | Media | Alto | Restricciones únicas a nivel de base de datos (constraint), no solo validación en frontend |
| R-03 | Pérdida de datos por falla del servidor sin respaldo | Operativo | Baja | Alto | Respaldos automáticos periódicos de la base de datos y plan de restauración documentado |
| R-04 | Desalineación entre el modelo ER y lo que realmente necesita el negocio hospitalario | Diseño / Alcance | Media | Medio | Validar el modelo con un flujo real de "paciente llega → cita → diagnóstico → receta → factura" antes de programar |
| R-05 | Alcance del proyecto crece durante el desarrollo (agregar módulos no planeados) | Cronograma | Alta | Medio | Congelar el alcance MVP (los requerimientos "Must") antes de programar; todo lo demás queda para una segunda iteración |
| R-06 | Inconsistencia entre backend (Python) y frontend (Angular) por cambios de API no comunicados | Técnico | Media | Medio | Definir contratos de API (esquemas Pydantic / OpenAPI) antes de programar el frontend |
| R-07 | Falta de tiempo para probar todos los módulos antes de la entrega | Cronograma | Alta | Alto | Priorizar pruebas manuales de los flujos "Must" (RF-01, RF-04, RF-08, RF-11, RF-16, RF-18) sobre los "Could" |
| R-08 | Un solo integrante concentra el conocimiento del backend o frontend (bus factor) | Operativo / Equipo | Media | Medio | Documentar decisiones clave en Notion a medida que se avanza, no al final |
| R-09 | Uso de datos reales de pacientes en pruebas (problema ético/legal) | Cumplimiento / Ético | Baja | Alto | Usar exclusivamente datos ficticios/generados para demostraciones |

## Cómo se priorizó

Los riesgos con **Alta probabilidad + Alto impacto** (R-07) y **Alta probabilidad** en general (R-05, R-07) son los que más amenazan una entrega con poco tiempo — por eso el plan de trabajo de este mismo paquete asume el alcance mínimo (Must) primero.
