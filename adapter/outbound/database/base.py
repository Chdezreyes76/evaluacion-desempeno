"""
=====================================================
🗄️ Database Base Configuration
=====================================================
Ubicación: /adapter/outbound/database/base.py
Configuración central de SQLAlchemy para el proyecto
=====================================================
"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# =====================================================
# CONFIGURACIÓN DE BASE DE DATOS
# =====================================================

# Obtener URL de la base de datos desde variables de entorno
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://backend_user:backend123@localhost:3306/backend_db"
)

# Configuración para desarrollo/producción
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
IS_DEVELOPMENT = ENVIRONMENT == "development"

# =====================================================
# ENGINE - Motor de SQLAlchemy
# =====================================================

# Crear el engine con configuración optimizada
engine = create_engine(
    DATABASE_URL,
    # Pool de conexiones
    pool_size=5,                    # Conexiones permanentes en el pool
    max_overflow=10,                # Conexiones adicionales permitidas
    pool_timeout=30,                 # Timeout para obtener conexión del pool
    pool_recycle=3600,              # Reciclar conexiones cada hora
    pool_pre_ping=True,             # Verificar conexiones antes de usarlas
    
    # Configuración adicional
    echo=IS_DEVELOPMENT,            # Mostrar SQL en consola (solo desarrollo)
    echo_pool=False,                # No mostrar debug del pool
    future=True,                    # Usar el nuevo estilo de SQLAlchemy 2.0
    
    # Configuración específica para MySQL
    connect_args={
        "connect_timeout": 10,
        "charset": "utf8mb4"
    } if "mysql" in DATABASE_URL else {}
)

# =====================================================
# SESSION - Fábrica de Sesiones
# =====================================================

# Configurar la fábrica de sesiones
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,      # No hacer commit automático
    autoflush=False,       # No hacer flush automático  
    expire_on_commit=False # Los objetos no expiran después del commit
)

# =====================================================
# BASE - Clase Base para Modelos
# =====================================================

# Convenciones de nombrado para constraints
naming_convention = {
    "ix": "ix_%(column_0_label)s",                    # Índices
    "uq": "uq_%(table_name)s_%(column_0_name)s",     # Unique constraints
    "ck": "ck_%(table_name)s_%(constraint_name)s",   # Check constraints
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s", # Foreign keys
    "pk": "pk_%(table_name)s"                        # Primary keys
}

# Crear metadata con convenciones
metadata = MetaData(naming_convention=naming_convention)

# Clase base para todos los modelos
Base = declarative_base(metadata=metadata)

# Añadir algunos métodos útiles a la clase Base
class BaseModel:
    """Métodos comunes para todos los modelos"""
    
    def to_dict(self):
        """Convertir modelo a diccionario"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    def update_from_dict(self, data: dict):
        """Actualizar modelo desde diccionario"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return self

# Hacer que Base herede los métodos útiles
Base.__class__ = type('Base', (BaseModel, Base.__class__), {})

# =====================================================
# DEPENDENCY INJECTION para FastAPI
# =====================================================

def get_db() -> Generator[Session, None, None]:
    """
    Dependency para inyectar sesión de BD en FastAPI
    
    Uso:
    ```python
    from fastapi import Depends
    from sqlalchemy.orm import Session
    from adapter.outbound.database.base import get_db
    
    @router.get("/users")
    def get_users(db: Session = Depends(get_db)):
        # db está disponible aquí
        return db.query(User).all()
    ```
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =====================================================
# FUNCIONES DE INICIALIZACIÓN
# =====================================================

def init_database():
    """
    Inicializar la base de datos
    Crea todas las tablas si no existen
    """
    try:
        # Importar todos los modelos para que Base los conozca
        # IMPORTANTE: Descomentar cuando tengas modelos creados
        # from adapter.outbound.database.models import user, product, order
        
        # Crear todas las tablas
        Base.metadata.create_all(bind=engine)
        print("✅ Base de datos inicializada correctamente")
        
        # Verificar conexión
        with engine.connect() as conn:
            result = conn.execute("SELECT 1")
            print("✅ Conexión a base de datos verificada")
            
    except Exception as e:
        print(f"❌ Error inicializando base de datos: {e}")
        raise

def drop_all_tables():
    """
    ⚠️ PELIGRO: Elimina TODAS las tablas
    Solo usar en desarrollo/testing
    """
    if not IS_DEVELOPMENT:
        raise Exception("❌ No se pueden eliminar tablas en producción")
    
    Base.metadata.drop_all(bind=engine)
    print("⚠️ Todas las tablas han sido eliminadas")

def check_database_connection():
    """
    Verificar que la conexión a la BD funciona
    """
    try:
        with engine.connect() as conn:
            result = conn.execute("SELECT 1")
            return True
    except Exception as e:
        print(f"❌ Error conectando a la base de datos: {e}")
        return False

def get_tables():
    """
    Obtener lista de tablas en la base de datos
    """
    from sqlalchemy import inspect
    inspector = inspect(engine)
    return inspector.get_table_names()

def create_tables_if_not_exist():
    """
    Crear tablas solo si no existen
    Útil para desarrollo
    """
    # Importar modelos
    # from adapter.outbound.database.models import user, product
    
    # Crear solo las tablas que no existen
    Base.metadata.create_all(bind=engine, checkfirst=True)

# =====================================================
# GESTIÓN DE TRANSACCIONES
# =====================================================

class DatabaseTransaction:
    """
    Context manager para transacciones
    
    Uso:
    ```python
    with DatabaseTransaction() as db:
        user = User(name="John")
        db.add(user)
        # Commit automático si todo va bien
        # Rollback automático si hay excepción
    ```
    """
    def __init__(self):
        self.db = SessionLocal()
    
    def __enter__(self):
        return self.db
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.db.rollback()
        else:
            self.db.commit()
        self.db.close()

# =====================================================
# EXPORTAR TODO LO NECESARIO
# =====================================================

__all__ = [
    "engine",
    "SessionLocal", 
    "Base",
    "get_db",
    "init_database",
    "drop_all_tables",
    "check_database_connection",
    "get_tables",
    "create_tables_if_not_exist",
    "DatabaseTransaction"
]

# =====================================================
# INICIALIZACIÓN AUTOMÁTICA (Opcional)
# =====================================================

# Si estamos en desarrollo, verificar conexión al importar
if IS_DEVELOPMENT:
    if check_database_connection():
        print("✅ Conexión a base de datos establecida")
    else:
        print("⚠️ No se pudo conectar a la base de datos")