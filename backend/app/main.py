"""
Punto de entrada de la API.
Incluye endpoints CRUD para Paciente, Medico y Cita (los módulos "Must"
del documento de requerimientos). El mismo patrón se repite para agregar
Internamiento, HistorialMedico, Factura, etc.
"""
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import datetime

from . import models, schemas
from .database import engine, get_db

# Crea las tablas en la base de datos si no existen todavía
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API - Sistema de Gestión Hospitalaria")

# Permite que Angular (que corre en otro puerto) llame a esta API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def raiz():
    return {"mensaje": "API del Sistema de Gestión Hospitalaria activa"}


# ---------- PACIENTES ----------
@app.post("/pacientes/", response_model=schemas.Paciente)
def crear_paciente(paciente: schemas.PacienteCreate, db: Session = Depends(get_db)):
    existente = db.query(models.Paciente).filter(
        models.Paciente.documento_identidad == paciente.documento_identidad
    ).first()
    if existente:
        raise HTTPException(status_code=400, detail="Ya existe un paciente con ese documento")

    nuevo = models.Paciente(**paciente.model_dump(), fecha_registro=datetime.utcnow())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@app.get("/pacientes/", response_model=list[schemas.Paciente])
def listar_pacientes(db: Session = Depends(get_db)):
    return db.query(models.Paciente).all()


@app.get("/pacientes/{paciente_id}", response_model=schemas.Paciente)
def obtener_paciente(paciente_id: int, db: Session = Depends(get_db)):
    paciente = db.query(models.Paciente).filter(models.Paciente.id == paciente_id).first()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente


# ---------- MEDICOS ----------
@app.post("/medicos/", response_model=schemas.Medico)
def crear_medico(medico: schemas.MedicoCreate, db: Session = Depends(get_db)):
    nuevo = models.Medico(**medico.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@app.get("/medicos/", response_model=list[schemas.Medico])
def listar_medicos(db: Session = Depends(get_db)):
    return db.query(models.Medico).all()


# ---------- CITAS ----------
@app.post("/citas/", response_model=schemas.Cita)
def crear_cita(cita: schemas.CitaCreate, db: Session = Depends(get_db)):
    # RF-05: evitar doble reserva del mismo médico en el mismo horario
    conflicto = db.query(models.Cita).filter(
        models.Cita.medico_id == cita.medico_id,
        models.Cita.fecha_hora == cita.fecha_hora,
        models.Cita.estado != "cancelada",
    ).first()
    if conflicto:
        raise HTTPException(status_code=400, detail="El médico ya tiene una cita en ese horario")

    nueva = models.Cita(**cita.model_dump())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


@app.get("/citas/", response_model=list[schemas.Cita])
def listar_citas(db: Session = Depends(get_db)):
    return db.query(models.Cita).all()
