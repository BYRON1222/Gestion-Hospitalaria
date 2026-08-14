# Guía para el Mapa en Miro — Sistema de Gestión Hospitalaria

Organiza el board en 4 zonas, de izquierda a derecha, para que se lea como una storyline del proyecto:

## Zona 1 — Requerimientos
Post-its agrupados por color, uno por módulo:
- Azul: Requerimientos Funcionales (RF01–RF21)
- Amarillo: Requerimientos No Funcionales (RNF01–RNF08)

## Zona 2 — Riesgos
Matriz probabilidad × impacto (2×2), con cada riesgo del documento `03_Riesgos.md` ubicado como sticky en el cuadrante correspondiente.

## Zona 3 — Diagrama ER
Exporta la imagen del diagrama ER (desde [mermaid.live](https://mermaid.live), pegando el bloque de `01_Diseño_ER.md`) y pégala como imagen central del board, con flechas explicando las relaciones clave (Paciente–Cita, Cita–Consulta, Consulta–Receta).

## Zona 4 — Flujo del sistema
Diagrama de flujo simple mostrando el recorrido de un caso de uso típico:

```
Paciente llega → Cita → Consulta → Receta/Internamiento → Factura
```

## Notas
- Usa un color consistente por tipo de elemento en todo el board (mismo esquema que en Notion).
- Deja espacio en la parte superior para el título del proyecto y los nombres de los integrantes.
