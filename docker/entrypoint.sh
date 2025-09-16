#!/bin/bash
# =====================================================
# 🚀 Entrypoint Script - Python/FastAPI Application
# =====================================================
# Ubicación: /app/docker/entrypoint.sh
# =====================================================

set -e

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting FastAPI Application...${NC}"

# Función para esperar a que MySQL esté listo
wait_for_db() {
    echo -e "${YELLOW}Waiting for MySQL to be ready...${NC}"
    
    # Extraer host y puerto de DATABASE_URL
    if [[ $DATABASE_URL =~ mysql\+pymysql://.*@([^:/]+):?([0-9]+)? ]]; then
        DB_HOST=${BASH_REMATCH[1]}
        DB_PORT=${BASH_REMATCH[2]:-3306}
    else
        DB_HOST=${DB_HOST:-mysql}
        DB_PORT=${DB_PORT:-3306}
    fi
    
    # Intentar conexión hasta 30 veces (30 segundos)
    for i in {1..30}; do
        if nc -z $DB_HOST $DB_PORT 2>/dev/null; then
            echo -e "${GREEN}MySQL is ready!${NC}"
            return 0
        fi
        echo -e "${YELLOW}MySQL is unavailable - sleeping (attempt $i/30)${NC}"
        sleep 1
    done
    
    echo -e "${RED}MySQL is unavailable after 30 attempts - exiting${NC}"
    exit 1
}

# Función para ejecutar migraciones
run_migrations() {
    echo -e "${YELLOW}Running database migrations...${NC}"
    
    # Verificar si Alembic está configurado
    if [ -f "alembic.ini" ]; then
        # Crear las tablas si no existen
        python -c "
from adapter.outbound.database.base import Base, engine
try:
    Base.metadata.create_all(bind=engine)
    print('✅ Database tables created/verified')
except Exception as e:
    print(f'⚠️  Warning creating tables: {e}')
"
        
        # Ejecutar migraciones de Alembic
        alembic upgrade head && echo -e "${GREEN}Migrations completed!${NC}" || {
            echo -e "${YELLOW}No migrations to apply or Alembic not configured${NC}"
        }
    else
        echo -e "${YELLOW}Alembic not configured, skipping migrations${NC}"
    fi
}

# Función para crear datos iniciales
seed_database() {
    if [ "$SEED_DATABASE" = "true" ] || [ "$ENVIRONMENT" = "development" ]; then
        echo -e "${YELLOW}Seeding database with initial data...${NC}"
        
        # Verificar si existe script de seed
        if [ -f "scripts/seed_database.py" ]; then
            python scripts/seed_database.py && echo -e "${GREEN}Database seeded!${NC}"
        else
            echo -e "${YELLOW}No seed script found at scripts/seed_database.py${NC}"
        fi
    fi
}

# Función para verificar la estructura del proyecto
verify_project_structure() {
    echo -e "${YELLOW}Verifying project structure...${NC}"
    
    REQUIRED_DIRS=("domain" "application" "adapter" "tests")
    for dir in "${REQUIRED_DIRS[@]}"; do
        if [ ! -d "$dir" ]; then
            echo -e "${YELLOW}Warning: Directory '$dir' not found${NC}"
        fi
    done
    
    if [ ! -f "main.py" ]; then
        echo -e "${RED}Error: main.py not found!${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}Project structure verified!${NC}"
}

# =====================================================
# MAIN EXECUTION
# =====================================================

# 1. Verificar estructura del proyecto
verify_project_structure

# 2. Esperar a que la base de datos esté lista
if [ "$SKIP_DB_WAIT" != "true" ]; then
    wait_for_db
fi

# 3. Ejecutar migraciones si no estamos en modo "worker"
if [ "$WORKER_MODE" != "true" ]; then
    if [ "$SKIP_MIGRATIONS" != "true" ]; then
        run_migrations
    fi
    
    # 4. Seed de datos si es necesario
    seed_database
fi

# 5. Imprimir información del entorno
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Environment Information:${NC}"
echo -e "${GREEN}========================================${NC}"
echo "ENVIRONMENT: ${ENVIRONMENT:-production}"
echo "HOST: ${HOST:-0.0.0.0}"
echo "PORT: ${PORT:-8000}"
echo "DATABASE_URL: ${DATABASE_URL:0:30}..."  # Solo mostrar inicio por seguridad
echo "WORKER_MODE: ${WORKER_MODE:-false}"
echo -e "${GREEN}========================================${NC}"

# 6. Ejecutar el comando proporcionado o el comando por defecto
if [ $# -eq 0 ]; then
    # Comando por defecto según el entorno
    if [ "$ENVIRONMENT" = "development" ]; then
        echo -e "${GREEN}Starting development server with auto-reload...${NC}"
        exec uvicorn main:app --host ${HOST:-0.0.0.0} --port ${PORT:-8000} --reload
    elif [ "$ENVIRONMENT" = "testing" ]; then
        echo -e "${GREEN}Running tests...${NC}"
        exec pytest
    else
        echo -e "${GREEN}Starting production server...${NC}"
        exec uvicorn main:app --host ${HOST:-0.0.0.0} --port ${PORT:-8000} --workers ${WORKERS:-4}
    fi
else
    # Ejecutar comando personalizado
    echo -e "${GREEN}Executing custom command: $@${NC}"
    exec "$@"
fi
