# Crear README.md
@"
# 🚀 Backend Template - Hexagonal Architecture

Template base para proyectos backend con FastAPI y MySQL siguiendo arquitectura hexagonal.

## 📋 Stack Tecnológico
- Python 3.11+
- FastAPI
- SQLAlchemy 2.0
- MySQL 8.0
- Redis
- Docker & Docker Compose

## 🚀 Quick Start
```bash
# 1. Configurar entorno
cp .env.example .env
# Editar .env con tus valores

# 2. Levantar servicios
docker-compose --profile development up -d

# 3. Verificar
curl http://localhost:8000/