# Riesgos Identificados — Sistema de Gestión Hospitalaria

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Entrega no cumplida por tiempo limitado | Alta | Alto | Priorizar MVP: Pacientes, Citas y Consultas primero; dejar Facturación/Internamiento como extra si sobra tiempo |
| Diseño ER incompleto que obligue a refactorizar backend | Media | Alto | Cerrar el ER y validarlo antes de generar el backend |
| Desincronización entre modelos backend y frontend (Angular) | Media | Medio | Definir contratos de API (endpoints y JSON) antes de programar el front |
| Pérdida de datos por falta de backups en desarrollo | Baja | Alto | Usar SQLite/Postgres local con scripts de seed y respaldo |
| Fuga o exposición de datos sensibles de pacientes | Baja | Alto | No usar datos reales de personas, cifrar contraseñas, variables de entorno para credenciales |
| Inconsistencia visual en el frontend | Alta | Medio | Definir guía de estilo específica antes de programar la interfaz |
| Falta de claridad en requerimientos al momento de programar | Media | Medio | Usar el documento de requerimientos como única fuente de verdad |
| Errores de sintaxis / generación incompleta al usar herramientas de IA para generar código | Alta | Media | Probar cada módulo (levantar el servidor) inmediatamente después de generarlo, antes de seguir con el siguiente |
