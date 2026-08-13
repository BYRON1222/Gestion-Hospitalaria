# Riesgos Identificados — Sistema de Gestión Hospitalaria

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Entrega no cumplida por tiempo limitado del curso | Alta | Alto | Priorizar MVP (Usuarios, Pacientes, Médicos, Citas, Consultas) antes de módulos secundarios |
| Cambiar el ER después de generar el backend con IA | Media | Alto | Cerrar el diseño ER antes de generar código |
| Integración con laboratorio clínico externo no disponible en entorno académico | Alta | Media | Simular la integración con un endpoint interno en vez de un servicio externo real |
| MFA y firma electrónica añaden complejidad no esencial para la demo | Media | Media | Implementar versión simplificada (código de prueba, hash/token en vez de certificado real) |
| Confusión entre stack pedido por el cliente (C#/Oracle) y el implementado (Python/Angular) | Media | Media | Documentar explícitamente la adaptación de stack en toda la documentación |
| Exposición de datos sensibles de pacientes | Baja | Alto | No usar datos reales, cifrar contraseñas y campos sensibles, usar variables de entorno |
| Reglas de negocio no validadas en backend (solo en frontend) | Media | Alto | Validar cada regla de negocio explícitamente en los servicios del backend |
| Desincronización entre modelos backend y frontend Angular | Media | Media | Definir contratos de API antes de programar el frontend |
| Errores de sintaxis / generación incompleta al usar herramientas de IA para generar código | Alta | Media | Probar cada módulo (levantar el servidor) inmediatamente después de generarlo, antes de seguir con el siguiente |
| Límite de uso de herramientas de IA (Cursor) interrumpe el flujo de trabajo | Media | Media | Hacer commits frecuentes para no perder avance; tener plan B de corrección manual |
