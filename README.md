# Sistema de Gestión Hospitalaria — Guía paso a paso (VS Code)

Esta guía asume que no sabes nada de esto. Cada paso dice exactamente qué escribir
y dónde. Todo se hace desde la **terminal integrada de VS Code** (menú superior:
`Terminal` → `New Terminal`, o `Ctrl+ñ` / `` Ctrl+` ``).

## Parte A — Backend (Python)

### A.1 — Abrir la carpeta del backend en VS Code
1. En VS Code: `Archivo` → `Abrir Carpeta` → selecciona la carpeta `backend/` de este paquete.

### A.2 — Crear un entorno virtual (aísla las librerías de este proyecto)
En la terminal, escribe:
```
python -m venv venv
```
Esto crea una carpeta `venv/` — es como una "caja separada" solo para este proyecto,
para que no se mezcle con otros programas de Python que tengas instalados.

### A.3 — Activar el entorno virtual
- **Windows (PowerShell):**
  ```
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```
  source venv/bin/activate
  ```
Si funcionó, verás `(venv)` al inicio de la línea de la terminal.

> Si Windows te da un error de "ejecución de scripts deshabilitada", corre esto una vez:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### A.4 — Instalar las librerías necesarias
```
pip install -r requirements.txt
```
Esto lee el archivo `requirements.txt` e instala FastAPI, SQLAlchemy, etc.
automáticamente. Tarda 1-2 minutos.

### A.5 — Levantar el servidor
```
uvicorn app.main:app --reload
```
Si todo salió bien, verás algo como `Uvicorn running on http://127.0.0.1:8000`.

### A.6 — Probar que funciona
Abre el navegador en: **http://127.0.0.1:8000/docs**

Vas a ver una interfaz automática (Swagger) donde puedes probar cada endpoint
(crear paciente, listar pacientes, crear cita, etc.) sin necesitar el frontend
todavía. Esto es útil para demostrar el backend en la entrega aunque el
frontend no esté 100% terminado.

**Deja esta terminal abierta y corriendo** mientras trabajas en el frontend.

---

## Parte B — Frontend (Angular)

### B.1 — Instalar Node.js (si no lo tienes)
Ve a https://nodejs.org, descarga la versión LTS, instálala (siguiente, siguiente,
finalizar). Verifica en una terminal nueva de VS Code:
```
node -v
npm -v
```
Deberías ver dos números de versión.

### B.2 — Instalar Angular CLI (la herramienta que genera el proyecto)
```
npm install -g @angular/cli
```

### B.3 — Crear el proyecto Angular
Desde la carpeta donde quieras que viva el proyecto (por ejemplo, junto a `backend/`):
```
ng new frontend --routing --style=css --standalone
```
Te va a preguntar un par de cosas — presiona Enter para aceptar las opciones
por defecto. Esto tarda un par de minutos (instala dependencias).

### B.4 — Copiar el código ya preparado
De la carpeta `frontend/src/app/` de este paquete, copia:
- `models/`
- `services/`
- `components/`

...dentro de la carpeta `src/app/` que Angular acaba de generar (reemplazando
si pregunta).

### B.5 — Habilitar HttpClient (para que el frontend pueda hablar con el backend)
Abre `src/app/app.config.ts` (Angular lo genera automáticamente) y agrégale
`provideHttpClient()`:
```ts
import { ApplicationConfig } from '@angular/core';
import { provideHttpClient } from '@angular/common/http';
import { provideRouter } from '@angular/router';
import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routes), provideHttpClient()]
};
```

### B.6 — Usar el componente de pacientes
Abre `src/app/app.component.html` (o el archivo de tu componente principal) y
agrega:
```html
<app-pacientes-lista></app-pacientes-lista>
```
Y en `src/app/app.component.ts`, agrega el import del componente:
```ts
import { PacientesListaComponent } from './components/pacientes/pacientes-lista.component';
// dentro de @Component({ imports: [..., PacientesListaComponent] })
```

### B.7 — Levantar el frontend
```
ng serve
```
Abre el navegador en **http://localhost:4200** — deberías ver la tabla de
pacientes (vacía al inicio, porque la base de datos está limpia).

### B.8 — Crear un paciente de prueba
Ve a **http://127.0.0.1:8000/docs**, busca `POST /pacientes/`, haz clic en
"Try it out", llena los datos de ejemplo y ejecuta. Recarga
`http://localhost:4200` y debería aparecer en la tabla.

---

## Parte C — Qué hacer con el resto del tiempo antes de entregar

Dado que la entrega es hoy/mañana, en este orden de prioridad:

1. **Corre el backend y muestra `/docs` funcionando** — es la prueba más rápida
   de que el diseño ER se tradujo en código real.
2. **Corre el frontend con la lista de pacientes** — demuestra la conexión
   full-stack.
3. **Sube el diagrama Mermaid** (`docs/01_Diseno_ER.md`) a mermaid.live para
   exportarlo como imagen, y pégala en tu documento de Notion.
4. **Arma el tablero de Miro** siguiendo `docs/05_Mapa_Miro_Guia.md` (10-15 min).
5. **Pega `docs/02_Requerimientos.md` y `docs/03_Riesgos.md`** en Notion como
   páginas separadas o secciones.

## Parte D — Si algo falla

- `ModuleNotFoundError` en Python → el entorno virtual no está activado (repite A.3).
- `ng: command not found` → repite B.2, y abre una terminal **nueva** después.
- El frontend carga pero la tabla da error de conexión → confirma que la
  terminal del backend (Parte A) sigue corriendo.
- Puerto ocupado → cierra otras terminales corriendo `uvicorn` o `ng serve` y
  vuelve a intentar.
