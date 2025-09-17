---
codigo: TSD-[CODIGO]-002-database
tipo: Technical Specification Document - Database
proyecto: [NOMBRE_PROYECTO]
version: 1.0
fecha: [FECHA_ACTUAL]
autor: DOCUMENT-Agent
capa: INFRAESTRUCTURA
actualizado_por: ALEMBIC-Agent
relacionados: [TSD-CODIGO-001-domain, MIG-CODIGO-001]
---

# 📘 Especificación Técnica de Base de Datos - [NOMBRE_PROYECTO]

## 🎯 INFORMACIÓN GENERAL

### Identificación de la Base de Datos
**Nombre BD:** [NOMBRE_DATABASE]
**Motor:** [PostgreSQL|MySQL|MongoDB|Oracle|SQLServer]
**Versión:** [VERSIÓN]
**Ambiente:** [DESARROLLO|STAGING|PRODUCCIÓN]
**Encoding:** [UTF8|LATIN1]
**Collation:** [COLLATION]

### Propósito y Alcance
[DESCRIPCIÓN DEL PROPÓSITO DE ESTA BASE DE DATOS Y QUÉ INFORMACIÓN ALMACENA]

### Conexión y Configuración
| Parámetro | Desarrollo | Staging | Producción |
|-----------|------------|---------|------------|
| Host | [HOST_DEV] | [HOST_STG] | [HOST_PROD] |
| Puerto | [PUERTO] | [PUERTO] | [PUERTO] |
| Database | [DB_NAME] | [DB_NAME] | [DB_NAME] |
| Schema | [SCHEMA] | [SCHEMA] | [SCHEMA] |
| Pool Size | [TAMAÑO] | [TAMAÑO] | [TAMAÑO] |

## 📊 MODELO DE DATOS

### Diagrama Entidad-Relación
```
[DIAGRAMA ERD]

┌─────────────┐        ┌─────────────┐
│   TABLA_A   │1      N│   TABLA_B   │
├─────────────┤────────├─────────────┤
│ id (PK)     │        │ id (PK)     │
│ campo_1     │        │ tabla_a_id  │
│ campo_2     │        │ campo_3     │
└─────────────┘        └─────────────┘
```

### Convenciones de Nomenclatura
| Elemento | Convención | Ejemplo | Justificación |
|----------|------------|---------|---------------|
| Tablas | [snake_case plural] | `users`, `order_items` | [RAZÓN] |
| Columnas | [snake_case] | `created_at`, `user_id` | [RAZÓN] |
| Primary Keys | [id o tabla_id] | `id`, `user_id` | [RAZÓN] |
| Foreign Keys | [tabla_referenciada_id] | `user_id`, `order_id` | [RAZÓN] |
| Índices | [idx_tabla_columnas] | `idx_users_email` | [RAZÓN] |
| Constraints | [tipo_tabla_descripcion] | `uq_users_email` | [RAZÓN] |

## 🗃️ ESQUEMAS

### Esquema: [NOMBRE_SCHEMA]
**Propósito:** [PARA QUÉ SE USA ESTE SCHEMA]
**Owner:** [USUARIO_OWNER]

#### Tablas del Esquema
| Tabla | Propósito | Registros Estimados | Crecimiento |
|-------|-----------|-------------------|-------------|
| [TABLA] | [PARA QUÉ] | [CANTIDAD] | [RATE/MES] |
| [TABLA] | [PARA QUÉ] | [CANTIDAD] | [RATE/MES] |

## 📋 ESPECIFICACIÓN DE TABLAS

### Tabla: [NOMBRE_TABLA_1]
**Schema:** [SCHEMA]
**Descripción:** [QUÉ ALMACENA ESTA TABLA]
**Tipo:** [TRANSACCIONAL|MAESTRO|CONFIGURACIÓN|AUDITORÍA|TEMPORAL]
**Volumen Estimado:** [REGISTROS]
**Crecimiento:** [REGISTROS/PERIODO]

#### Columnas
| Columna | Tipo | Null | Default | Descripción | Constraint |
|---------|------|------|---------|-------------|------------|
| id | SERIAL/BIGINT | NO | - | Identificador único | PRIMARY KEY |
| [columna] | [TIPO] | [SI/NO] | [VALOR] | [DESCRIPCIÓN] | [CONSTRAINT] |
| created_at | TIMESTAMP | NO | NOW() | Fecha creación | - |
| updated_at | TIMESTAMP | NO | NOW() | Última actualización | - |
| deleted_at | TIMESTAMP | SI | NULL | Soft delete | - |

#### Constraints
| Nombre | Tipo | Definición | Descripción |
|--------|------|------------|-------------|
| [pk_tabla] | PRIMARY KEY | (id) | Llave primaria |
| [fk_tabla_ref] | FOREIGN KEY | (columna) REFERENCES tabla(id) | Relación con [tabla] |
| [uq_tabla_campo] | UNIQUE | (campo) | Unicidad de [campo] |
| [ck_tabla_regla] | CHECK | (columna > 0) | Validación de [regla] |

#### Índices
| Nombre | Columnas | Tipo | Propósito | Include |
|--------|----------|------|-----------|---------|
| [idx_tabla_campo] | (campo) | BTREE | Búsquedas por [campo] | - |
| [idx_tabla_campos] | (campo1, campo2) | BTREE | Queries compuestos | (campo3) |
| [idx_tabla_busqueda] | (campo) | GIN/GIST | Búsqueda de texto | - |

#### Triggers
| Nombre | Evento | Timing | Función | Propósito |
|--------|--------|--------|---------|-----------|
| [trg_tabla_evento] | INSERT/UPDATE/DELETE | BEFORE/AFTER | [función()] | [QUÉ HACE] |

#### Particionamiento
**Estrategia:** [RANGE|LIST|HASH|NINGUNO]
**Columna de Partición:** [COLUMNA]
**Detalle:**
```sql
-- Ejemplo de particionamiento si aplica
PARTITION BY RANGE (created_at) (
    PARTITION p2024_01 VALUES LESS THAN ('2024-02-01'),
    PARTITION p2024_02 VALUES LESS THAN ('2024-03-01')
);
```

### Tabla: [NOMBRE_TABLA_2]
[REPETIR ESTRUCTURA PARA CADA TABLA]

## 🔗 RELACIONES

### Relaciones entre Tablas
| Tabla Origen | Tabla Destino | Tipo | Cardinalidad | Constraint | On Delete | On Update |
|--------------|---------------|------|--------------|------------|-----------|-----------|
| [tabla_a] | [tabla_b] | FK | 1:N | [fk_name] | CASCADE | CASCADE |
| [tabla_b] | [tabla_c] | FK | N:1 | [fk_name] | RESTRICT | CASCADE |
| [tabla_d] | [tabla_e] | FK | N:M | Via tabla intermedia | CASCADE | CASCADE |

### Tablas de Relación (N:M)
| Tabla | Relaciona | Columnas | Constraint Único |
|-------|-----------|----------|------------------|
| [tabla_rel] | [tabla_a] ↔ [tabla_b] | tabla_a_id, tabla_b_id | (tabla_a_id, tabla_b_id) |

## 🎯 VISTAS

### Vista: [NOMBRE_VISTA_1]
**Tipo:** [NORMAL|MATERIALIZADA]
**Propósito:** [PARA QUÉ SE USA]
**Actualización:** [SI ES MATERIALIZADA, CUÁNDO SE REFRESCA]

```sql
-- Definición de la vista
CREATE VIEW [nombre_vista] AS
SELECT 
    [columnas]
FROM [tablas]
WHERE [condiciones];
```

#### Columnas de la Vista
| Columna | Tipo | Origen | Descripción |
|---------|------|--------|-------------|
| [columna] | [TIPO] | [tabla.columna] | [DESCRIPCIÓN] |

## 🔧 FUNCIONES Y PROCEDIMIENTOS

### Función: [NOMBRE_FUNCIÓN_1]
**Propósito:** [QUÉ HACE]
**Retorno:** [TIPO DE RETORNO]
**Lenguaje:** [SQL|PLPGSQL|OTRO]

#### Parámetros
| Parámetro | Tipo | Dirección | Descripción | Default |
|-----------|------|-----------|-------------|---------|
| [param1] | [TIPO] | IN/OUT/INOUT | [DESCRIPCIÓN] | [VALOR] |

#### Lógica
```sql
-- Pseudocódigo o descripción de la lógica
1. Validar entrada
2. Procesar datos
3. Retornar resultado
```

### Procedimiento: [NOMBRE_PROCEDIMIENTO_1]
[SIMILAR ESTRUCTURA A FUNCIÓN]

## 🔐 SEGURIDAD

### Usuarios y Roles
| Usuario/Rol | Tipo | Permisos | Propósito |
|-------------|------|----------|-----------|
| [app_user] | Usuario | SELECT, INSERT, UPDATE, DELETE | Aplicación principal |
| [read_only] | Rol | SELECT | Reportes y consultas |
| [admin] | Usuario | ALL | Administración |

### Permisos por Objeto
| Objeto | Tipo | Usuario/Rol | Permisos |
|--------|------|-------------|----------|
| [tabla] | TABLE | [usuario] | SELECT, INSERT, UPDATE |
| [vista] | VIEW | [rol] | SELECT |
| [función] | FUNCTION | [usuario] | EXECUTE |

### Encriptación y Datos Sensibles
| Tabla | Columna | Tipo de Dato | Método de Protección |
|-------|---------|--------------|---------------------|
| [users] | [password] | Contraseña | Hashed con bcrypt |
| [cards] | [number] | Tarjeta | Encriptado AES-256 |

## 📈 OPTIMIZACIÓN Y PERFORMANCE

### Estadísticas de Tablas
| Tabla | Registros | Tamaño | Índices | Tamaño Índices | Bloat |
|-------|-----------|---------|---------|----------------|-------|
| [tabla] | [cantidad] | [MB/GB] | [N] | [MB/GB] | [%] |

### Queries Críticos
| Query ID | Descripción | Frecuencia | Tiempo Objetivo | Optimización |
|----------|-------------|------------|-----------------|--------------|
| [QRY-001] | [QUÉ BUSCA] | [N/seg] | <[ms] | [ÍNDICE/ESTRATEGIA] |

### Índices de Performance
| Índice | Tabla | Hit Rate | Tamaño | Último Uso | Recomendación |
|--------|-------|----------|--------|------------|---------------|
| [índice] | [tabla] | [%] | [MB] | [fecha] | [MANTENER/ELIMINAR] |

### Configuración de Performance
| Parámetro | Valor Dev | Valor Prod | Justificación |
|-----------|-----------|------------|---------------|
| work_mem | [MB] | [MB] | [RAZÓN] |
| shared_buffers | [MB/GB] | [MB/GB] | [RAZÓN] |
| max_connections | [N] | [N] | [RAZÓN] |

## 🔄 MANTENIMIENTO

### Tareas de Mantenimiento
| Tarea | Frecuencia | Horario | Script | Impacto |
|-------|------------|---------|--------|---------|
| VACUUM | Diario | 02:00 | [script] | Bajo |
| ANALYZE | Semanal | Domingo 03:00 | [script] | Bajo |
| REINDEX | Mensual | 1er Domingo | [script] | Medio |
| Backup Full | Diario | 23:00 | [script] | Bajo |
| Backup Incremental | Cada 4h | - | [script] | Mínimo |

### Estrategia de Backup
| Tipo | Frecuencia | Retención | Ubicación | Verificación |
|------|------------|-----------|-----------|--------------|
| Full | Diario | 30 días | [S3/NAS] | Semanal |
| Incremental | 4 horas | 7 días | [S3/NAS] | Diaria |
| WAL/Binlog | Continuo | 7 días | [S3/NAS] | Automática |

### Plan de Recuperación
**RTO (Recovery Time Objective):** [TIEMPO]
**RPO (Recovery Point Objective):** [TIEMPO]

#### Procedimiento de Recuperación
1. [PASO 1 - IDENTIFICAR PUNTO DE RECUPERACIÓN]
2. [PASO 2 - RESTAURAR BACKUP]
3. [PASO 3 - APLICAR WAL/BINLOG]
4. [PASO 4 - VERIFICAR INTEGRIDAD]
5. [PASO 5 - REACTIVAR SERVICIOS]

## 📊 MIGRACIONES

### Historial de Migraciones
| Versión | Fecha | Descripción | Script | Rollback |
|---------|-------|-------------|--------|----------|
| [001] | [FECHA] | Creación inicial | MIG-[CODIGO]-001.sql | N/A |
| [002] | [FECHA] | Agregar tabla X | MIG-[CODIGO]-002.sql | MIG-[CODIGO]-002-rollback.sql |

### Migraciones Pendientes
| Versión | Descripción | Prioridad | Fecha Planificada |
|---------|-------------|-----------|-------------------|
| [003] | [CAMBIO] | [ALTA/MEDIA/BAJA] | [FECHA] |

## 🚨 MONITOREO Y ALERTAS

### Métricas Monitoreadas
| Métrica | Umbral Warning | Umbral Critical | Acción |
|---------|----------------|-----------------|--------|
| Conexiones activas | >80% | >95% | [ESCALAR/ALERTAR] |
| Espacio en disco | >70% | >85% | [LIMPIAR/EXPANDIR] |
| Query time | >500ms | >1000ms | [OPTIMIZAR] |
| Deadlocks | >5/hora | >10/hora | [INVESTIGAR] |

### Health Checks
| Check | Query/Comando | Frecuencia | Timeout |
|-------|---------------|------------|---------|
| Conectividad | SELECT 1 | 30 seg | 5 seg |
| Escritura | INSERT INTO health_check | 1 min | 10 seg |
| Replicación | SHOW SLAVE STATUS | 1 min | 5 seg |

## 📝 CONSIDERACIONES ESPECIALES

### Limitaciones Conocidas
- [LIMITACIÓN 1 - DESCRIPCIÓN]
- [LIMITACIÓN 2 - DESCRIPCIÓN]

### Dependencias Externas
- [SISTEMA/BD EXTERNA Y TIPO DE DEPENDENCIA]

### Requisitos de Compliance
| Requisito | Aplicación | Implementación |
|-----------|------------|----------------|
| GDPR | Datos personales | Soft delete + auditoría |
| PCI-DSS | Datos de tarjetas | Encriptación + logs |

## 🔗 REFERENCIAS

### Documentación Relacionada
- [TSD Domain](TSD-[CODIGO]-001-domain.md)
- [Migrations](migrations/MIG-[CODIGO]-*.sql)
- [API Documentation](API-[CODIGO]-001.md)

### Scripts y Herramientas
- [Ubicación de scripts de mantenimiento]
- [Herramientas de administración]
- [Dashboard de monitoreo]

---

**Documento Creado:** [FECHA]
**Autor:** DOCUMENT-Agent
**Basado en trabajo de:** MODELS-Agent, ALEMBIC-Agent
**Última Actualización:** [FECHA]

<!-- 
INSTRUCCIONES PARA AGENTES:

1. MODELS-Agent:
   - Crear modelos según estas especificaciones
   - Respetar tipos de datos y constraints
   - Mantener nomenclatura consistente

2. ALEMBIC-Agent:
   - Generar migraciones para cada cambio
   - Incluir scripts de rollback
   - Validar integridad referencial

3. REPOSITORIES-Agent:
   - Optimizar queries según índices disponibles
   - Usar vistas cuando sea apropiado
   - Respetar límites de conexiones

4. TEST-Agent:
   - Validar constraints
   - Probar triggers y funciones
   - Verificar performance de queries

5. QUALITY-Agent:
   - Revisar normalización
   - Validar índices necesarios
   - Verificar plan de backup

La base de datos es CRÍTICA para el sistema
Esta documentación debe estar SIEMPRE actualizada
-->
