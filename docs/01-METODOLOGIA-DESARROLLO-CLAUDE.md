# 🚀 METODOLOGÍA DE DESARROLLO CON CLAUDE-CODE Y AGENTES

## 📌 01. Introducción

Esta guía establece la metodología estándar para gestionar proyectos usando **Claude Code con Agentes Especializados**, optimizando la calidad del código mediante la división del trabajo entre agentes con contexto específico. Basada en la experiencia de proyectos exitosos y arquitectura hexagonal.

📊 **Ver también**: [04-FLUJO-AGENTES.md](./04-FLUJO-AGENTES.md) para el diagrama detallado del flujo completo con control de calidad automático.

## 🤖 02. Sistema de Agentes Especializados

### Agentes Disponibles

El sistema cuenta con 12 agentes especializados que trabajan de forma **secuencial y coordinada**:

| Agente | Responsabilidad | Temperatura | Archivos Clave |
|--------|----------------|-------------|----------------|
| **PLAN-Agent** | Planificación, documentación, INDEX, WP | 0.1 | `/docs/`, plantillas |
| **DOCUMENT-Agent** | Documentación técnica y actualizaciones | 0.1 | `/docs/projects/****/` |
| **DOMAIN-Agent** | Models, value objects, services, events | 0.1 | `/domain/` |
| **DTOS-Agent** | Definición y desarrollo de DTOs | 0.1 | `/application/****/dtos/` |
| **PORTS-Agent** | Definición y desarrollo de ports | 0.1 | `/application/****/ports/` |
| **USECASES-Agent** | Definición y desarrollo de casos de uso | 0.1 | `/application/****/usecases/` |
| **MAPPERS-Agent** | Definición y desarrollo de mappers y parsers | 0.1 | `/adapter/outbound/excel/` |
| **ALEMBIC-Agent** | Definición y desarrollo de migraciones con Alembic | 0.1 | `/adapter/outbound/database/echeyde/migrations/` |
| **REPOSITORIES-Agent** | Definición y desarrollo de repositorios | 0.1 | `/adapter/outbound/database/****/repositories/` |
| **MODELS-Agent** | Definición y desarrollo de modelos de pydantic y sqlalchemy | 0.1 | `/adapter/outbound/database/****/models/` |
| **ROUTES-Agent** | Definición y desarrollo de endpoints y dependencias | 0.1 | `/adapter/inbound/api/` |
| **TEST-Agent** | Definición y desarrollo de tests unitarios, de integración y end-to-end | 0.1 | `/tests/` |
| **QUALITY-Agent** | Revisión automática de calidad de código | 0.0 | Todos los archivos del proyecto |

## 🎯 03. Principios Fundamentales

1. **Documentación Primero**: PLAN-Agent siempre inicia con su FASE 1 de recopilacion de la solicitud y delega a DOCUMENT-Agent la creación de INDEX y WP.
2. **Flujo Secuencial Obligatorio**: Los agentes trabajan uno después del otro, nunca en paralelo
3. **División por Capas**: Cada agente maneja su capa específica
4. **Secuenciación Estricta**: Orden obligatorio dentro de cada capa basado en dependencias arquitecturales
5. **Contexto Reducido**: Agentes cargan solo archivos relevantes
6. **Reutilización Maximizada**: PLAN-Agent identifica >30% componentes
7. **Calidad Automática**: QUALITY-Agent corrige errores comunes
8. **Testing Integrado**: TEST-Agent valida cada implementación
9. **Exportaciones en __init__.py**: Cada agente actualiza sus exports

## ⏭️ 04. Flujo Secuencial Obligatorio

### 🚫 Sin Paralelismo
**IMPORTANTE**: Los agentes trabajan de forma **estrictamente secuencial**. No hay paralelismo en esta metodología.

#### Razones del Flujo Secuencial:
1. **Dependencias Arquitecturales**: Cada agente necesita el output del anterior
2. **Consistencia de Datos**: Evita conflictos y inconsistencias entre capas
3. **Control de Calidad**: QUALITY-Agent puede validar cada paso antes del siguiente
4. **Simplicidad Operativa**: Flujo predecible y fácil de seguir
5. **Debugging Eficiente**: Problemas se detectan inmediatamente en la capa correcta

#### Flujo General:
```
PLAN → DOMAIN → [DTOS → PORTS → USECASES] → [MODELS → ALEMBIC → MAPPERS → REPOSITORIES → ROUTES] → TEST → CIERRE
```

**Cada flecha (→) representa una dependencia obligatoria que impide el paralelismo.**

## 🔄 05. Secuenciación Obligatoria por Capas

### 📋 Capa de Aplicación - Orden Estricto
**Secuencia:** DTOS → PORTS → USECASES

#### 1. DTOS-Agent (PRIMERO)
- **Propósito**: Definen contratos de entrada y salida del sistema
- **Dependencias**: Ninguna (punto de partida)
- **Razón**: Establecen la estructura de datos que usarán todos los demás componentes
- **Output**: Contratos claros para interfaces y lógica

#### 2. PORTS-Agent (SEGUNDO)
- **Propósito**: Definen interfaces para interactuar con el exterior
- **Dependencias**: Requieren DTOs para definir parámetros y tipos de retorno
- **Razón**: Los Ports necesitan conocer qué DTOs van a manejar en sus métodos
- **Output**: Interfaces que usan los DTOs definidos

#### 3. USECASES-Agent (TERCERO)
- **Propósito**: Implementan la lógica de negocio de la aplicación
- **Dependencias**: Requieren tanto DTOs como Ports
- **Razón**: Los Use Cases orquestan la lógica usando DTOs y dependiendo de Ports
- **Output**: Lógica de negocio completa

```
Flujo de Dependencias Aplicación:
DTOs → Ports → Use Cases
  ↓      ↓        ↓
Contratos → Interfaces → Lógica
```

### 🔧 Capa de Adaptadores - Orden Estricto
**Secuencia:** MODELS → ALEMBIC → MAPPERS → REPOSITORIES → ROUTES

#### 1. MODELS-Agent (PRIMERO)
- **Propósito**: Definen estructura de datos de persistencia (tablas, campos, relaciones)
- **Dependencias**: Ninguna (punto de partida técnico)
- **Razón**: Base fundamental para migraciones, mappers y repositories
- **Output**: Estructura de base de datos definida

#### 2. ALEMBIC-Agent (SEGUNDO)
- **Propósito**: Crean y mantienen el esquema de base de datos
- **Dependencias**: Requieren Models para generar las migraciones
- **Razón**: Las migraciones deben reflejar la estructura definida en Models
- **Output**: Esquema de BD actualizado

#### 3. MAPPERS-Agent (TERCERO)
- **Propósito**: Transforman entre Models (BD) y DTOs (dominio)
- **Dependencias**: Requieren Models para conocer la estructura de datos
- **Razón**: Necesitan saber qué campos mapear entre capas
- **Output**: Transformaciones entre capas

#### 4. REPOSITORIES-Agent (CUARTO)
- **Propósito**: Implementan la lógica de acceso a datos
- **Dependencias**: Requieren Models (para queries) y Mappers (para transformaciones)
- **Razón**: Usan Models para persistir y Mappers para convertir datos
- **Output**: Capa de persistencia completa

#### 5. ROUTES-Agent (QUINTO)
- **Propósito**: Exponen los endpoints HTTP de la API
- **Dependencias**: Requieren Repositories para acceder a datos
- **Razón**: Los endpoints necesitan repositories para procesar requests
- **Output**: API REST completa

```
Flujo de Dependencias Adaptadores:
Models → Alembic → Mappers → Repositories → Routes
  ↓        ↓         ↓           ↓           ↓
Estructura → Schema → Transform → Persist → Expose
```

## 📋 06. Proceso con Agentes

### 🔵 Fase 1: Planificación (PLAN-Agent)

#### Trigger
```
@PLAN-Agent necesito [descripción del proyecto]
```

#### Acciones del PLAN-Agent
1. **Analiza** `/docs/03-PROYECTOS-PREVIOS.md` para componentes reutilizables
2. **Clasifica** proyecto (FEAT/OPTM/REFR/BUGF/INTG/MIGR)
3. **Identifica** agentes necesarios
4. **Genera** código único (4 letras)
5. **Delega** a DOCUMENT-Agent:
   - Crear `INDEX-[CÓDIGO].md` usando plantilla
   - Crear `WP-[CÓDIGO]-001.md` usando plantilla
6. **Crea** `AGENT-CONTEXT-[CÓDIGO].md con:
   - Resumen del proyecto
   - Componentes a reutilizar
   - Instrucciones para siguientes agentes
7. **Valida** con el usuario si hay dudas o necesita clarificación antes de proceder

#### Output Esperado
```
✅ Proyecto [CÓDIGO] planificado
📁 /docs/projects/[CÓDIGO]/
   ├── INDEX-[CÓDIGO].md
   ├── WP-[CÓDIGO]-001.md
   └── AGENT-CONTEXT-[CÓDIGO].md

Siguiente: DOMAIN-Agent para models y value objects
```

### 🟣 Fase 2: Implementación por Capas

#### 2.1 Dominio (DOMAIN-Agent → DOCUMENT-Agent → QUALITY-Agent)
```
@DOMAIN-Agent implementar modelos para [CÓDIGO] según AGENT-CONTEXT
@DOCUMENT-Agent actualizar documentación de dominio para [CÓDIGO]
@QUALITY-Agent revisar código de dominio para [CÓDIGO]
```

**Responsabilidades:**
- **DOMAIN-Agent**: Models y value objects en `/domain/`, Services de dominio, Events de dominio
- **DOCUMENT-Agent**: Actualizar documentación técnica del dominio
- **QUALITY-Agent**: Revisar calidad, estándares y mejores prácticas
- Actualizar `__init__.py` con exports

#### 2.2 Aplicación (DTOS-Agent → PORTS-Agent → USECASES-Agent → DOCUMENT-Agent → QUALITY-Agent)
```
@DTOS-Agent crear DTOs para [CÓDIGO] según AGENT-CONTEXT
@PORTS-Agent definir ports para [CÓDIGO] según AGENT-CONTEXT  
@USECASES-Agent implementar casos de uso para [CÓDIGO] según AGENT-CONTEXT
@DOCUMENT-Agent actualizar documentación de aplicación para [CÓDIGO]
@QUALITY-Agent revisar código de aplicación para [CÓDIGO]
```

**Responsabilidades:**
- **DTOS-Agent**: DTOs en `/application/****/dtos/` (PRIMERO - contratos)
- **PORTS-Agent**: Ports en `/application/****/ports/` (SEGUNDO - interfaces)
- **USECASES-Agent**: Use cases en `/application/****/usecases/` (TERCERO - lógica)
- **DOCUMENT-Agent**: Actualizar documentación técnica de la aplicación
- **QUALITY-Agent**: Revisar calidad, dependencias y arquitectura
- Actualizar `__init__.py` con exports

#### 2.3 Adaptadores (MODELS-Agent → ALEMBIC-Agent → MAPPERS-Agent → REPOSITORIES-Agent → ROUTES-Agent → DOCUMENT-Agent → QUALITY-Agent)
```
@MODELS-Agent crear modelos para [CÓDIGO] según AGENT-CONTEXT
@ALEMBIC-Agent crear migraciones para [CÓDIGO] según AGENT-CONTEXT
@MAPPERS-Agent crear mappers para [CÓDIGO] según AGENT-CONTEXT
@REPOSITORIES-Agent crear repositorios para [CÓDIGO] según AGENT-CONTEXT
@ROUTES-Agent crear endpoints para [CÓDIGO] según AGENT-CONTEXT
@DOCUMENT-Agent actualizar documentación de adaptadores para [CÓDIGO]
@QUALITY-Agent revisar código de adaptadores para [CÓDIGO]
```

**Responsabilidades:**
- **MODELS-Agent**: Models en `/adapter/outbound/database/****/models/` (PRIMERO - estructura BD)
- **ALEMBIC-Agent**: Migraciones en `/adapter/outbound/database/echeyde/migrations/` (SEGUNDO - esquema BD)
- **MAPPERS-Agent**: Mappers en `/adapter/outbound/excel/` (TERCERO - transformaciones)
- **REPOSITORIES-Agent**: Repositories en `/adapter/outbound/database/****/repositories/` (CUARTO - persistencia)
- **ROUTES-Agent**: Endpoints en `/adapter/inbound/api/` (QUINTO - API)
- **DOCUMENT-Agent**: Actualizar documentación técnica de adaptadores
- **QUALITY-Agent**: Revisar calidad, performance y seguridad
- Actualizar `__init__.py` con exports

#### 2.4 Testing y Validación Final (TEST-Agent → DOCUMENT-Agent → QUALITY-Agent)
```
@TEST-Agent testear [CÓDIGO] con >80% cobertura
@DOCUMENT-Agent actualizar documentación de testing para [CÓDIGO]
@QUALITY-Agent validación final de todo el proyecto [CÓDIGO]
```
**Responsabilidades:**

- Tests unitarios en                            `/tests/unit/`

- Tests unitarios de domain en                  `/tests/unit/domain/`
- Tests unitarios domain models en              `/tests/unit/domain/****/models/`
- Tests unitarios domain value objects en       `/tests/unit/domain/****/value_objects/`

- Tests unitarios application en                `/tests/unit/application/`
- Tests unitarios application use cases en      `/tests/unit/application/****/use_cases/`
- Tests unitarios application DTOs en           `/tests/unit/application/****/dtos/`
- Tests unitarios application ports en          `/tests/unit/application/****/ports/`

- Tests unitarios adapter en                    `/tests/unit/adapter/`
- Tests unitarios repositories en               `/tests/unit/adapter/outbound/repositories/****/`
- Tests unitarios Pydantic models en            `/tests/unit/adapter/outbound/models/****/`
- Tests unitarios API Dependencies en           `/tests/unit/adapter/inbound/api/dependencies/****/`
- Tests unitarios API Routes en                 `/tests/unit/adapter/inbound/api/routes/****/`

- Tests integración en                          `/tests/integration/`
- Tests integración repositories en             `/tests/integration/adapter/outbound/repositories/****/`
- Tests integración Pydantic models en          `/tests/integration/adapter/outbound/models/****/`
- Tests integración API dependencies en         `/tests/integration/adapter/inbound/api/dependencies/****/`
- Tests integración API routes en               `/tests/integration/adapter/inbound/api/routes/****/`
- Tests integración DTOs en                     `/tests/integration/application/dtos/****/`
- Tests integración use cases en                `/tests/integration/application/use_cases/****/`
- Tests integración PORTS en                    `/tests/integration/application/ports/****/`
- Tests integración domain models en            `/tests/integration/domain/models/****/`
- Tests integración domain value objects en     `/tests/integration/domain/value_objects/****/`
- Tests integración domain services en          `/tests/integration/domain/services/****/`
- Tests integración domain events en            `/tests/integration/domain/events/****/`

- Tests end-to-end en                           `/tests/e2e/`
- Tests end-to-end API en                       `/tests/e2e/api/`
- Tests end-to-end full flow en                 `/tests/e2e/full_flow/`
- Tests end-to-end edge cases en                `/tests/e2e/edge_cases/`
- Tests end-to-end performance en               `/tests/e2e/performance/`
- Tests end-to-end security en                  `/tests/e2e/security/`
- Tests end-to-end database en                  `/tests/e2e/database/`


### ✅ Fase 5: Cierre (PLAN-Agent)

```
@PLAN-Agent cerrar proyecto [CÓDIGO]
```

**Acciones:**
- Verificar que todos los agentes han completado sus tareas
- Validar que TEST-Agent confirma >80% cobertura y todos los tests pasan
- Asegurar que QUALITY-Agent reporta 0 errores críticos
- Revisar que DOCUMENT-Agent ha actualizado la documentación final en `INDEX-[CÓDIGO].md` y `WP-[CÓDIGO].md`
- Actualizar `/docs/03-PROYECTOS-PREVIOS.md`
- Documentar componentes reutilizables nuevos
- Registrar lecciones aprendidas

## 🤖 07. Prompt Maestro para Proyectos con Agentes

### Plantilla de Solicitud Actualizada:

```markdown
========================================
🚀 SOLICITUD DE NUEVO PROYECTO - SISTEMA DE AGENTES
========================================

@PLAN-Agent iniciar nuevo proyecto

📋 DESCRIPCIÓN BREVE (1-2 líneas):
[Describe qué necesitas hacer]

🎯 PROBLEMA A RESOLVER:
Preguntar al usuario:
- ¿Cuál es el problema actual?
- ¿Qué impacto tiene?

📊 SITUACIÓN ACTUAL:
Preguntar al usuario:
- ¿Cómo se hace actualmente?
- ¿Qué componentes/código existe relacionado?

✅ RESULTADO ESPERADO:
Preguntar al usuario:
- ¿Cómo sabremos que está completo?
- ¿Que aspectos son críticos?

📦 ALCANCE:
INCLUYE:
Proponer y validar con el usuario las funcionalidades.

NO INCLUYE:
Proponer y validar con el usuario qué no se hará.

========================================
```

### Beneficios Clave

1. **Contexto Optimizado**: Cada agente solo carga archivos relevantes
2. **Especialización**: Expertise profundo en cada capa
3. **Secuenciación Controlada**: Orden estricto previene errores de dependencias
4. **Calidad Garantizada**: TEST-Agent valida todo
5. **Reutilización Automática**: PLAN-Agent identifica componentes

## 📁 08. Estructura de Documentación con Agentes

```
/.claude/
└── agents/                            # Configuración de agentes
    ├── PLAN-Agent.md
    ├── DOMAIN-Agent.md
    ├── DTOS-Agent.md
    ├── PORTS-Agent.md
    ├── USECASES-Agent.md
    ├── MAPPERS-Agent.md
    ├── ALEMBIC-Agent.md
    ├── REPOSITORIES-Agent.md
    ├── MODELS-Agent.md
    ├── ROUTES-Agent.md
    ├── TEST-Agent.md
    └── QUALITY-Agent.md

/docs/
├── 01-METODOLOGIA-DESARROLLO-CLAUDE.md  # Este documento
├── 02-SISTEMA-CODIFICACION-DOCS.md      # Sistema de nomenclatura
├── 03-PROYECTOS-PREVIOS.md              # Registro de componentes reutilizables
├── 04-FLUJO-AGENTES.md                  # Flujo detallado con QA automático
├── projects/
│   └── [XXXX]/                       # Ej: TFIN, APRO, IMPX, REMX
│       ├── INDEX-[XXXX].md           # Generado por PLAN-Agent
│       ├── WP-[XXXX]-001.md          # Generado por PLAN-Agent
│       ├── AGENT-CONTEXT-[XXXX].md   # Contexto compartido entre agentes
│       ├── adrs/                      # Architecture Decision Records
│       │   └── ADR-[XXXX]-001.md
│       ├── technical/                 # Especificaciones técnicas
│       │   └── TSD-[XXXX]-001.md
│       ├── tests/                     # Planes de testing
│       │   └── TST-[XXXX]-001.md
│       └── migrations/                # Scripts de migración
│           └── MIG-[XXXX]-001.sql
├── templates/                         # Plantillas obligatorias
│   ├── TEMPLATE-INDEX.md
│   ├── TEMPLATE-WP-FEAT.md
│   ├── TEMPLATE-WP-OPTM.md
│   ├── TEMPLATE-ADR.md
│   ├── TEMPLATE-TSD.md
│   └── TEMPLATE-TST.md
```

## 🚦 09. Quick Start con Agentes

### 1. **Iniciar Proyecto**
```
@PLAN-Agent nuevo proyecto para [descripción]
```

### 2. **Implementar Dominio**
```
@DOMAIN-Agent implementar según AGENT-CONTEXT-[CÓDIGO]
@DOCUMENT-Agent actualizar documentación de dominio para [CÓDIGO]
@QUALITY-Agent revisar código de dominio para [CÓDIGO]
```

### 3. **Crear Aplicación (Secuencia Obligatoria)**
```
# PASO 1: DTOs primero (contratos)
@DTOS-Agent crear DTOs para [CÓDIGO] según AGENT-CONTEXT

# PASO 2: Ports segundo (interfaces)
@PORTS-Agent definir ports para [CÓDIGO] según AGENT-CONTEXT

# PASO 3: Use Cases tercero (lógica)
@USECASES-Agent implementar casos de uso para [CÓDIGO] según AGENT-CONTEXT

# Documentación y calidad
@DOCUMENT-Agent actualizar documentación de aplicación para [CÓDIGO]
@QUALITY-Agent revisar código de aplicación para [CÓDIGO]
```

### 4. **Implementar Adaptadores (Secuencia Obligatoria)**
```
# PASO 1: Models primero (estructura BD)
@MODELS-Agent crear modelos para [CÓDIGO] según AGENT-CONTEXT

# PASO 2: Alembic segundo (esquema BD)
@ALEMBIC-Agent crear migraciones para [CÓDIGO] según AGENT-CONTEXT

# PASO 3: Mappers tercero (transformaciones)
@MAPPERS-Agent crear mappers para [CÓDIGO] según AGENT-CONTEXT

# PASO 4: Repositories cuarto (persistencia)
@REPOSITORIES-Agent crear repositorios para [CÓDIGO] según AGENT-CONTEXT

# PASO 5: Routes quinto (API)
@ROUTES-Agent crear endpoints para [CÓDIGO] según AGENT-CONTEXT

# Documentación y calidad
@DOCUMENT-Agent actualizar documentación de adaptadores para [CÓDIGO]
@QUALITY-Agent revisar código de adaptadores para [CÓDIGO]
```

### 5. **Validar con Tests**
```
@TEST-Agent testear [CÓDIGO] con >80% cobertura
@DOCUMENT-Agent actualizar documentación de testing para [CÓDIGO]
@QUALITY-Agent validación final de todo el proyecto [CÓDIGO]
```

### 6. **Cerrar Proyecto**
```
@PLAN-Agent cerrar [CÓDIGO] y actualizar PROYECTOS-PREVIOS
```

### ⚠️ Recordatorios Críticos:
- **NO alterar el orden** dentro de Aplicación y Adaptadores
- **Esperar aprobación** de QUALITY-Agent antes del siguiente paso
- **Actualizar AGENT-CONTEXT** después de cada agente
- **Verificar exports** en __init__.py de cada capa

## ⚠️ 10. Reglas Críticas del Sistema

### ✅ SIEMPRE
1. Iniciar con PLAN-Agent
2. **Trabajar de forma secuencial**: Un agente a la vez, nunca en paralelo
3. Seguir arquitectura hexagonal estricta
4. **Respetar secuenciación obligatoria**: DTOS→PORTS→USECASES y MODELS→ALEMBIC→MAPPERS→REPOSITORIES→ROUTES
5. Actualizar __init__.py en cada capa
6. Pasar por QUALITY-Agent después de cada fase
7. Validar con TEST-Agent
8. Documentar en PROYECTOS-PREVIOS

### ❌ NUNCA
1. Saltarse la planificación
2. **Trabajar en paralelo**: Los agentes deben ejecutarse secuencialmente
3. **Alterar el orden de secuenciación** dentro de las capas
4. Mezclar responsabilidades entre agentes
5. Implementar sin tests
6. Olvidar exportaciones en __init__.py
7. Ignorar componentes reutilizables
8. Saltar el control de calidad de QUALITY-Agent

## 🔄 11. Flujo Integrado de Calidad y Documentación

### QUALITY-Agent - Control de Calidad Continuo
El **QUALITY-Agent** se ejecuta después de cada fase de implementación:

**Responsabilidades:**
- **Revisión de código**: Estándares, mejores prácticas, arquitectura
- **Validación de dependencias**: Verificar que las capas no se mezclen
- **Control de calidad**: Detectar code smells, duplicación, complejidad
- **Reporte de estado**: Actualizar AGENT-CONTEXT con hallazgos

**Trigger automático después de:**
- DOMAIN-Agent completa implementación
- Cada agente de aplicación (DTOS, PORTS, USECASES) termina
- Cada agente de adaptadores (MODELS, ALEMBIC, MAPPERS, REPOSITORIES, ROUTES) termina
- TEST-Agent completa las pruebas

### DOCUMENT-Agent - Documentación Técnica Continua
El **DOCUMENT-Agent** mantiene la documentación actualizada:

**Responsabilidades:**
- **Documentación técnica**: APIs, interfaces, modelos de datos
- **Actualización de INDEX**: Mantener el índice del proyecto actualizado
- **Documentación de arquitectura**: Decisiones técnicas importantes
- **Reporte de progreso**: Actualizar WP con avances

**Trigger automático después de:**
- Cada fase de implementación (Dominio, Aplicación, Adaptadores)
- Cambios significativos en la arquitectura
- Finalización de testing

## 📝 12. Comunicación Entre Agentes

Los agentes se comunican mediante:

1. **AGENT-CONTEXT-[CÓDIGO].md**: Documento compartido con:

   Este documento debe funcionar como un cuaderno de bitácora que cada agente va actualizando y consultando.

   - Estado actual del proyecto
   - Componentes creados por cada agente
   - Instrucciones específicas
   - Interfaces entre capas

2. **Handoff Messages**: Al terminar, cada agente indica:

   Básicamente, resume lo realizado y los siguientes pasos y quien es el siguiente agente.
   ```
   ✅ DOMAIN-Agent completado
   - Creados: 3 models, 5 value objects
   - Ubicación: /domain/facturacion/
   - Exports actualizados en __init__.py

   Siguiente: APPLICATION-Agent para use cases
   ```
