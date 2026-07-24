"""
Esquemas Pydantic: definen la "forma" de los datos que entran y salen
de la API (validación automática + documentación en /docs).
"""
from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel


class PacienteBase(BaseModel):
    nombre: str
    apellido: str
    fecha_nacimiento: Optional[date] = None
    genero: Optional[str] = None
    documento_identidad: str
    telefono: Optional[str] = None
    email: Optional[str] = None
    direccion: Optional[str] = None
    tipo_sangre: Optional[str] = None


class PacienteCreate(PacienteBase):
    pass


class Paciente(PacienteBase):
    id: int
    fecha_registro: Optional[datetime] = None

    class Config:
        from_attributes = True


class MedicoBase(BaseModel):
    nombre: str
    apellido: str
    especialidad_id: Optional[int] = None
    departamento_id: Optional[int] = None
    numero_colegiado: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None


class MedicoCreate(MedicoBase):
    pass


class Medico(MedicoBase):
    id: int

    class Config:
        from_attributes = True


class CitaBase(BaseModel):
    paciente_id: int
    medico_id: int
    fecha_hora: datetime
    motivo: Optional[str] = None
    estado: Optional[str] = "programada"


class CitaCreate(CitaBase):
    pass


class Cita(CitaBase):
    id: int

    class Config:
        from_attributes = True
