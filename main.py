"""
Main Application - FastAPI
"""
import os
from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Load environment
load_dotenv()

# Config
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://backend_user:backend123@mysql:3306/backend_db")

# Create app
app = FastAPI(title="Hexagonal API", version="0.1.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database setup
try:
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)
    SessionLocal = sessionmaker(bind=engine)
except Exception as e:
    print(f"DB Error: {e}")
    engine = None
    SessionLocal = None

# Routes
@app.get("/")
async def root():
    """Welcome endpoint"""
    return {
        "message": "¡Entorno de desarrollo Preparado! 🚀",
        "environment": ENVIRONMENT,
        "status": "READY",
        "version": "0.1.0",
        "docs": "/docs",
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/health")
async def health():
    """Health check"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/ready")
async def ready():
    """Readiness check"""
    db_status = "disconnected"
    
    if SessionLocal:
        try:
            db = SessionLocal()
            db.execute(text("SELECT 1"))
            db.close()
            db_status = "connected"
        except Exception as e:
            db_status = f"error: {str(e)[:50]}"
    
    response = {
        "status": "ready" if db_status == "connected" else "not ready",
        "database": db_status,
        "timestamp": datetime.utcnow().isoformat()
    }
    
    if db_status != "connected":
        return JSONResponse(status_code=503, content=response)
    
    return response

@app.get("/info")
async def info():
    """App info"""
    return {
        "app": "Hexagonal API",
        "version": "0.1.0",
        "environment": ENVIRONMENT,
        "endpoints": ["/", "/health", "/ready", "/info", "/docs"],
        "timestamp": datetime.utcnow().isoformat()
    }

# Startup
@app.on_event("startup")
async def startup():
    print("=" * 50)
    print("🚀 Starting Hexagonal API")
    print(f"📍 Environment: {ENVIRONMENT}")
    print("📚 Docs at: http://localhost:8000/docs")
    
    if SessionLocal:
        try:
            db = SessionLocal()
            db.execute(text("SELECT 1"))
            db.close()
            print("✅ Database connected")
        except Exception as e:
            print(f"❌ Database error: {e}")
    
    print("=" * 50)