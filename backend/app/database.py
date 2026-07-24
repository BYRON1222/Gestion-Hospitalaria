"""
Configuración de la conexión a la base de datos.
Por defecto usa SQLite (archivo local, cero configuración) para que puedas
correr el proyecto de inmediato. Para usar PostgreSQL más adelante, solo
cambia SQLALCHEMY_DATABASE_URL.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# --- SQLite (por defecto, para desarrollo/entrega) ---
SQLALCHEMY_DATABASE_URL = "sqlite:///./hospital.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# --- PostgreSQL (descomenta y ajusta cuando lo necesites) ---
# SQLALCHEMY_DATABASE_URL = "postgresql://usuario:password@localhost:5432/hospital_db"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
