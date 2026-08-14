# Guía de Documentación en Notion — Sistema de Gestión Hospitalaria

Estructura sugerida de páginas dentro del workspace de Notion del proyecto:

```
📁 Sistema de Gestión Hospitalaria
 ├─ 📄 Resumen del proyecto (alcance, integrantes, fecha de entrega)
 ├─ 📄 Requerimientos Funcionales (tabla, ver docs/02_Requerimientos.md)
 ├─ 📄 Requerimientos No Funcionales (tabla, ver docs/02_Requerimientos.md)
 ├─ 📄 Riesgos (tabla, ver docs/03_Riesgos.md)
 ├─ 📄 Diseño ER (bloque mermaid + diccionario de datos, ver docs/01_Diseño_ER.md)
 └─ 📄 Evidencias / Capturas del sistema funcionando
```

## Cómo pegar el diagrama ER en Notion

1. Copia el bloque de código que empieza con ```` ```mermaid ```` desde `docs/01_Diseño_ER.md`.
2. En Notion, escribe `/code` para insertar un bloque de código.
3. Pega el contenido y selecciona el lenguaje **Mermaid** en el selector del bloque — Notion lo renderiza automáticamente como diagrama.

## Recomendación

Cada página de requerimientos y riesgos puede convertirse directamente en una **tabla nativa de Notion** (Table view), copiando las filas de las tablas en Markdown de `docs/02_Requerimientos.md` y `docs/03_Riesgos.md`.
