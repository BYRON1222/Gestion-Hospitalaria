"""
Modelos SQLAlchemy — cada clase es una tabla, reflejan exactamente
el diagrama ER en docs/01_Diseno_ER.md
"""
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from .database import Base


class Especialidad(Base):
    __tablename__ = "especialidades"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String)


class Departamento(Base):
    __tablename__ = "departamentos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    ubicacion = Column(String)


class Medico(Base):
    __tablename__ = "medicos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    especialidad_id = Column(Integer, ForeignKey("especialidades.id"))
    departamento_id = Column(Integer, ForeignKey("departamentos.id"))
    numero_colegiado = Column(String, unique=True)
    telefono = Column(String)
    email = Column(String)
    fecha_contratacion = Column(Date)

    especialidad = relationship("Especialidad")
    departamento = relationship("Departamento")


class Paciente(Base):
    __tablename__ = "pacientes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    fecha_nacimiento = Column(Date)
    genero = Column(String)
    documento_identidad = Column(String, unique=True, index=True)
    telefono = Column(String)
    email = Column(String)
    direccion = Column(String)
    tipo_sangre = Column(String)
    fecha_registro = Column(DateTime)


class Habitacion(Base):
    __tablename__ = "habitaciones"
    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String, nullable=False)
    departamento_id = Column(Integer, ForeignKey("departamentos.id"))
    tipo = Column(String)


class Cama(Base):
    __tablename__ = "camas"
    id = Column(Integer, primary_key=True, index=True)
    habitacion_id = Column(Integer, ForeignKey("habitaciones.id"))
    codigo = Column(String, unique=True)
    estado = Column(String, default="disponible")  # disponible | ocupada | mantenimiento


class Cita(Base):
    __tablename__ = "citas"
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    medico_id = Column(Integer, ForeignKey("medicos.id"), nullable=False)
    fecha_hora = Column(DateTime, nullable=False)
    motivo = Column(String)
    estado = Column(String, default="programada")  # programada | completada | cancelada

    paciente = relationship("Paciente")
    medico = relationship("Medico")


class Internamiento(Base):
    __tablename__ = "internamientos"
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    medico_id = Column(Integer, ForeignKey("medicos.id"), nullable=False)
    cama_id = Column(Integer, ForeignKey("camas.id"), nullable=False)
    fecha_ingreso = Column(DateTime, nullable=False)
    fecha_alta = Column(DateTime, nullable=True)
    diagnostico_ingreso = Column(String)


class HistorialMedico(Base):
    __tablename__ = "historiales_medicos"
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    medico_id = Column(Integer, ForeignKey("medicos.id"), nullable=False)
    fecha = Column(Date, nullable=False)
    diagnostico = Column(String)
    tratamiento = Column(String)
    observaciones = Column(String)


class Medicamento(Base):
    __tablename__ = "medicamentos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String)
    stock = Column(Integer, default=0)
    precio_unitario = Column(Numeric(10, 2))


class Receta(Base):
    __tablename__ = "recetas"
    id = Column(Integer, primary_key=True, index=True)
    historial_medico_id = Column(Integer, ForeignKey("historiales_medicos.id"), nullable=False)
    medicamento_id = Column(Integer, ForeignKey("medicamentos.id"), nullable=False)
    dosis = Column(String)
    frecuencia = Column(String)
    duracion = Column(String)


class Factura(Base):
    __tablename__ = "facturas"
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    fecha = Column(Date, nullable=False)
    monto_total = Column(Numeric(10, 2))
    estado_pago = Column(String, default="pendiente")


class DetalleFactura(Base):
    __tablename__ = "detalle_facturas"
    id = Column(Integer, primary_key=True, index=True)
    factura_id = Column(Integer, ForeignKey("facturas.id"), nullable=False)
    concepto = Column(String)
    cantidad = Column(Integer, default=1)
    precio_unitario = Column(Numeric(10, 2))
    subtotal = Column(Numeric(10, 2))


class Seguro(Base):
    __tablename__ = "seguros"
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), unique=True)
    aseguradora = Column(String)
    numero_poliza = Column(String)
    cobertura = Column(String)


class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre_usuario = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    rol = Column(String, nullable=False)  # admin | medico | enfermero | recepcionista
