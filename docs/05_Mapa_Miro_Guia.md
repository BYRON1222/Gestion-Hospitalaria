# Guía para el Mapa en Miro

No puedo crear el tablero de Miro directamente (no tengo acceso a tu cuenta), pero aquí está todo el contenido ya organizado por secciones — solo copias cada bloque en un "frame" (marco) de Miro. Con esto un tablero completo te toma 10-15 minutos en vez de partir de una hoja en blanco.

## Frame 1 — Mapa de módulos del sistema

Crea 6 notas adhesivas (sticky notes), una por módulo, conectadas al centro con un nodo "Sistema de Gestión Hospitalaria":

1. Gestión de Pacientes
2. Citas
3. Internamiento
4. Historial Clínico
5. Farmacia
6. Facturación y Seguros

## Frame 2 — Flujo de usuario: paciente ambulatorio

Secuencia de tarjetas conectadas con flechas (izquierda a derecha):

`Paciente llega` → `Recepción busca/registra paciente` → `Se agenda cita con médico` → `Médico atiende y registra historial` → `Médico emite receta (si aplica)` → `Facturación genera cobro` → `Paciente se retira`

## Frame 3 — Flujo de usuario: paciente internado

`Paciente llega` → `Se evalúa y decide internamiento` → `Se asigna cama disponible` → `Seguimiento diario (historial clínico)` → `Médico da de alta` → `Cama se libera` → `Facturación genera cobro final`

## Frame 4 — Arquitectura técnica (diagrama de cajas)

Tres cajas conectadas con flechas:

`Angular (Frontend)` → `FastAPI (Backend / API REST)` → `PostgreSQL (Base de datos)`

Debajo de cada caja, una nota pequeña:
- Angular: "Componentes por módulo, consume la API vía servicios HTTP"
- FastAPI: "Valida datos con Pydantic, expone /docs automático"
- PostgreSQL: "Refleja el diagrama ER, con llaves foráneas para integridad"

## Frame 5 — Matriz de riesgos (visual)

Cuadrícula 3x3 (Probabilidad Baja/Media/Alta como filas, Impacto Bajo/Medio/Alto como columnas). Coloca cada riesgo (R-01 a R-09 del documento de riesgos) como una nota en la celda que le corresponde. Colorea rojo la esquina Alta probabilidad / Alto impacto — visualmente muestra dónde está el mayor peligro del proyecto (en este caso, R-07: falta de tiempo para pruebas).

## Tip para la presentación

Si tu profesor pide "mapa Miro" para ver que pensaron el sistema como equipo (no solo como diagrama técnico), los Frames 2 y 3 (flujos de usuario) son los que más impresionan, porque muestran que entendieron el *proceso hospitalario real*, no solo las tablas de la base de datos.
