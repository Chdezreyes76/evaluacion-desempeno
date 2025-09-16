# 📁 ESTRUCTURA DE ARCHIVOS DOCKER EN EL PROYECTO

## 🗂️ Ubicación de cada archivo creado:

```
proyecto-hexagonal/
│
├── 📄 docker-compose.yml                 # ⬅️ Raíz del proyecto
├── 📄 .env.example                       # ⬅️ Raíz del proyecto
├── 📄 .env                               # ⬅️ Crear desde .env.example (ignorar en git)
├── 📄 .gitignore                         # ⬅️ Añadir .env y otros
│
├── 📁 app/
│   ├── 📁 docker/                        # ⬅️ Ya existe con requirements.txt
│   │   ├── 📄 requirements.txt           # ✅ Ya lo tienes aquí
│   │   ├── 📄 Dockerfile.api             # ⬅️ Colocar aquí
│   │   ├── 📄 entrypoint.sh              # ⬅️ Colocar aquí
│   │   │
│   │   ├── 📁 mysql/                     # ⬅️ Crear carpeta
│   │   │   ├── 📁 init/                  # ⬅️ Scripts SQL iniciales
│   │   │   │   └── 📄 01_init.sql       # ⬅️ (Opcional) Datos iniciales
│   │   │   └── 📁 conf.d/                # ⬅️ Configuración MySQL
│   │   │       └── 📄 custom.cnf         # ⬅️ Colocar aquí
│   │   │
│   │   └── 📁 redis/                     # ⬅️ Crear carpeta
│   │       └── 📄 redis.conf             # ⬅️ Colocar aquí
│   │
│   └── 📁 scripts/                       # ⬅️ Scripts útiles
│       ├── 📄 seed_database.py           # ⬅️ (Opcional) Seed data
│       └── 📄 health_check.py            # ⬅️ (Opcional) Health check
│
├── 📁 domain/                            # Tu código de dominio
├── 📁 application/                       # Tu código de aplicación  
├── 📁 adapter/                           # Tu código de adaptadores
├── 📁 tests/                             # Tests
├── 📄 main.py                            # Entry point de FastAPI
├── 📄 alembic.ini                        # Configuración de Alembic
└── 📁 logs/                              # ⬅️ Se creará automáticamente

```

## 📝 INSTRUCCIONES DE CONFIGURACIÓN:

### 1️⃣ **Crear estructura de carpetas:**
```bash
# Desde la raíz del proyecto
mkdir -p app/docker/mysql/init
mkdir -p app/docker/mysql/conf.d
mkdir -p app/docker/redis
mkdir -p app/scripts
mkdir -p logs
```

### 2️⃣ **Copiar archivos a su ubicación:**
```bash
# Mover archivos a sus ubicaciones correctas
mv Dockerfile.api app/docker/
mv entrypoint.sh app/docker/
mv custom.cnf app/docker/mysql/conf.d/
mv redis.conf app/docker/redis/
# docker-compose.yml y .env.example van en la raíz
```

### 3️⃣ **Hacer ejecutable el entrypoint:**
```bash
chmod +x app/docker/entrypoint.sh
```

### 4️⃣ **Crear archivo .env desde ejemplo:**
```bash
cp .env.example .env
# Editar .env con tus valores reales
```

### 5️⃣ **Actualizar .gitignore:**
```bash
echo "
# Environment
.env
.env.local
*.env

# Docker volumes
mysql-data/
redis-data/

# Logs
logs/
*.log

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
" >> .gitignore
```

## 🚀 COMANDOS PARA LEVANTAR EL PROYECTO:

### **Desarrollo (con herramientas de debug):**
```bash
# Construir imágenes
docker-compose --profile development build

# Levantar servicios
docker-compose --profile development up -d

# Ver logs
docker-compose logs -f api

# Acceder a:
# - API: http://localhost:8000
# - Swagger: http://localhost:8000/docs
# - Adminer: http://localhost:8081
# - Redis Commander: http://localhost:8082
```

### **Producción (solo servicios esenciales):**
```bash
# Construir para producción
docker-compose build

# Levantar servicios
docker-compose up -d

# Escalar API si es necesario
docker-compose up -d --scale api=3
```

### **Comandos útiles:**
```bash
# Ejecutar migraciones manualmente
docker-compose exec api alembic upgrade head

# Crear nueva migración
docker-compose exec api alembic revision --autogenerate -m "descripcion"

# Acceder al contenedor de la API
docker-compose exec api bash

# Acceder a MySQL
docker-compose exec mysql mysql -u hexagonal_user -p

# Ver logs de un servicio específico
docker-compose logs -f mysql

# Detener todo
docker-compose down

# Detener y eliminar volúmenes (⚠️ CUIDADO: borra datos)
docker-compose down -v

# Reconstruir sin cache
docker-compose build --no-cache
```

## 🔍 VERIFICACIÓN DE SALUD:

### **Endpoints de health check:**
```python
# main.py - Añadir estos endpoints
from fastapi import FastAPI, status
from sqlalchemy import text

app = FastAPI()

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "healthy"}

@app.get("/ready", status_code=status.HTTP_200_OK)
async def readiness_check(db: Session = Depends(get_db)):
    try:
        # Verificar conexión a BD
        db.execute(text("SELECT 1"))
        return {"status": "ready", "database": "connected"}
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"status": "not ready", "database": "disconnected"}
        )
```

## 📊 MONITOREO:

### **Ver estado de los contenedores:**
```bash
docker-compose ps
```

### **Ver uso de recursos:**
```bash
docker stats
```

### **Ver redes:**
```bash
docker network ls
docker network inspect hexagonal-network
```

### **Ver volúmenes:**
```bash
docker volume ls
docker volume inspect hexagonal-mysql-data
```

## ⚠️ TROUBLESHOOTING:

### **Si MySQL no arranca:**
```bash
# Ver logs específicos
docker-compose logs mysql

# Verificar permisos del volumen
docker-compose down -v  # ⚠️ Elimina datos
docker-compose up -d
```

### **Si la API no conecta a MySQL:**
```bash
# Verificar variables de entorno
docker-compose exec api env | grep DATABASE

# Test manual de conexión
docker-compose exec api python -c "
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://hexagonal_user:hexagonal_pass123!@mysql:3306/hexagonal_db')
conn = engine.connect()
print('✅ Conexión exitosa')
"
```

### **Si hay problemas de permisos:**
```bash
# En Linux/Mac
sudo chown -R $USER:$USER .
chmod +x app/docker/entrypoint.sh
```

## 🎯 SIGUIENTE PASO:

Una vez configurado todo:

1. **Crear main.py** con la aplicación FastAPI básica
2. **Configurar Alembic** para las migraciones
3. **Implementar el dominio** siguiendo la metodología de agentes
4. **Añadir tests** con pytest

¿Necesitas ayuda con alguno de estos pasos?
