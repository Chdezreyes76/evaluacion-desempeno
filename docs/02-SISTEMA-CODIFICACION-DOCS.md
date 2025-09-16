# Sistema de Codificación de Documentación Técnica

## 📋 Objetivo
Establecer un sistema de codificación consistente para relacionar toda la documentación técnica del proyecto, facilitando la trazabilidad y búsqueda de documentos relacionados.

## 🏷️ Formato de Codificación

### Estructura General
```
[TIPO]-[PROYECTO]-[SEQ]-[descripcion].[ext]
```

### Componentes

#### 1. TIPO (Tipo de Documento)
| Código | Tipo | Descripción |
|--------|------|-------------|
| `WP` | Work Plan | Planes de trabajo y roadmaps |
| `INDEX` | Project Index | Índice principal del proyecto |
| `AGENT-CONTEXT` | Agent Context | Cuaderno de bitácora entre agentes |
| `ADR` | Architecture Decision Record | Decisiones arquitectónicas |
| `TSD` | Technical Spec Document | Especificaciones técnicas |
| `DFD` | Data Flow Document | Flujos de datos y procesos |
| `API` | API Documentation | Documentación de endpoints |
| `TST` | Test Plan | Planes y casos de prueba |
| `MIG` | Migration | Scripts y planes de migración |
| `REQ` | Requirements | Requisitos funcionales/no funcionales |
| `DES` | Design Document | Diseños y mockups |
| `AGT` | Agent Documentation | Documentación específica de agentes |

#### 2. PROYECTO (Código de Proyecto/Feature)

##### Códigos de Proyecto Existentes (Ejemplos)
| Código | Proyecto/Feature | Descripción | Estado |
|--------|-----------------|-------------|--------|
| `TFIN` | Totales Financieros | Incorporación de totales en importación | ✅ Completado |
| `APRO` | Actualización Progenitores | Gestión de progenitores en edición de alumnos | ✅ Completado |
| `IMPX` | Importación Excel | Sistema de importación de facturas | 🔄 En desarrollo |
| `PBUG` | Progenitores Bug Fix | Corrección bug persistencia progenitores | ✅ Completado |


##### Tipos de Proyecto (Para WP)
| Tipo | Descripción | Fases Típicas |
|------|-------------|---------------|
| `FEAT` | Nueva Funcionalidad | 7 fases estándar |
| `OPTM` | Optimización/Performance | Incluye benchmarks antes/después |
| `REFR` | Refactoring | Sin cambios funcionales visibles |
| `BUGF` | Bug Fix | Corrección de errores específicos |
| `INTG` | Integración | Con sistemas externos |
| `MIGR` | Migración | De datos o sistemas |

#### 3. SEQ (Secuencial)
- Número de 3 dígitos (001-999)
- Único por combinación TIPO-PROYECTO
- Se incrementa para cada nuevo documento

#### 4. Descripción
- Texto descriptivo en minúsculas
- Palabras separadas por guiones
- Máximo 5-6 palabras clave

## 📁 Estructura de Directorios - Opción B: Híbrida por Proyecto + Tipo

### Estructura Principal (Recomendada)
```
/.claude/
└── agents/                                  # Configuración de agentes
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
├── 📋 01-METODOLOGIA-DESARROLLO-CLAUDE.md  # Documentos globales
├── 📊 02-SISTEMA-CODIFICACION-DOCS.md      # en la raíz
├── 📐 03-PROYECTOS-PREVIOS.md
├── 🔄 04-FLUJO-AGENTES.md
│
├── projects/                                # Carpeta maestra de proyectos
│   ├── TFIN/                               # Un directorio por proyecto
│   │   ├── INDEX-TFIN.md                   # INDEX siempre visible (generado por PLAN-Agent)
│   │   ├── WP-TFIN-001.md                  # WP siempre visible (generado por PLAN-Agent)
│   │   ├── AGENT-CONTEXT-TFIN.md          # Cuaderno de bitácora entre agentes
│   │   ├── adrs/
│   │   │   └── ADR-TFIN-001.md
│   │   ├── api/
│   │   │   └── API-TFIN-001.md
│   │   ├── migrations/
│   │   │   ├── MIG-TFIN-001.sql
│   │   │   ├── MIG-TFIN-002.sql
│   │   │   └── MIG-TFIN-003.md
│   │   ├── technical/
│   │   │   ├── TSD-TFIN-001.md
│   │   │   ├── TSD-TFIN-002.md
│   │   │   └── TSD-TFIN-003.md
│   │   ├── tests/
│   │   │   ├── TST-TFIN-001.md
│   │   │   └── TST-TFIN-002.md
│   │   └── agents/
│   │       ├── AGT-TFIN-001-domain.md      # Documentación específica de agentes
│   │       ├── AGT-TFIN-002-application.md
│   │       └── AGT-TFIN-003-adapters.md
│   │
│   ├── APRO/                               # Proyecto Actualización Progenitores
│   │   ├── INDEX-APRO.md                   # Generado por PLAN-Agent
│   │   ├── WP-APRO-001.md                  # Generado por PLAN-Agent
│   │   ├── AGENT-CONTEXT-APRO.md          # Cuaderno de bitácora
│   │   ├── adrs/
│   │   │   └── ADR-APRO-001.md
│   │   ├── technical/
│   │   │   └── TSD-APRO-001.md
│   │   ├── tests/
│   │   │   └── TST-APRO-001.md
│   │   └── agents/
│   │       └── AGT-APRO-001-summary.md
│   │
│   ├── IMPX/                               # Proyecto Importación Excel
│   │   ├── INDEX-IMPX.md
│   │   ├── WP-IMPX-001.md
│   │   ├── adrs/
│   │   │   └── ADR-IMPX-001.md
│   │   ├── flows/
│   │   │   └── DFD-IMPX-001.md
│   │   ├── technical/
│   │   │   └── TSD-IMPX-001.md
│   │   └── tests/
│   │       └── TST-IMPX-001.md
│   │
│   └── [NUEVO_PROYECTO]/                   # Estructura para nuevos proyectos
│       ├── INDEX-[XXXX].md                 # Generado automáticamente por PLAN-Agent
│       ├── WP-[XXXX]-001.md                # Generado automáticamente por PLAN-Agent
│       ├── AGENT-CONTEXT-[XXXX].md        # Cuaderno de bitácora entre agentes
│       ├── adrs/                           # Subcarpetas por tipo
│       ├── api/
│       ├── migrations/
│       ├── technical/
│       ├── tests/
│       └── agents/                         # Documentación específica de agentes
│
├── templates/                               # 📋 Plantillas reutilizables
│   ├── TEMPLATE-INDEX.md
│   ├── TEMPLATE-WP-FEAT.md
│   ├── TEMPLATE-WP-OPTM.md
│   ├── TEMPLATE-ADR.md
│   ├── TEMPLATE-TSD.md
│   └── TEMPLATE-TST.md
│
├── migrations/                              # 🔄 Migraciones globales
│   └── guias-migracion-generales.md
│
└── api/                                     # 📡 Documentación API general
    └── openapi-specs-generales.yml
```

### Ventajas de la Estructura

1. **Visibilidad inmediata**: INDEX y WP siempre visibles en raíz del proyecto
2. **Organización por tipo**: Subcarpetas mantienen orden cuando hay muchos documentos
3. **Escalabilidad**: Funciona bien con 1 o 100 documentos
4. **Navegación intuitiva**: Fácil encontrar documentos por proyecto y tipo
5. **Flexibilidad**: Subcarpetas solo se crean cuando se necesitan

## 🔗 Documento de Índice por Proyecto

Cada proyecto debe tener un documento índice que liste todos sus documentos relacionados:

### Ejemplo: `projects/TFIN/INDEX-TFIN.md` (Generado por PLAN-Agent)

```yaml
---
codigo: INDEX-TFIN
tipo: Project Index
proyecto: Totales Financieros
version: 1.0
fecha: 2025-08-29
autor: PLAN-Agent
actualizado_por: DOCUMENT-Agent
relacionados: [WP-TFIN-001, AGENT-CONTEXT-TFIN]
estado: COMPLETADO
flujo_agentes: secuencial
---
```

# 📚 Índice de Documentación - Totales Financieros (TFIN)

## 📋 Información del Proyecto
- **Código**: TFIN
- **Estado**: ✅ COMPLETADO
- **Fecha inicio**: 29/08/2024
- **Fecha fin**: 15/10/2024
- **Generado por**: PLAN-Agent
- **Flujo**: Secuencial con 12 agentes especializados

## 🤖 Flujo de Agentes Ejecutado
```
PLAN-Agent → DOMAIN-Agent → DTOS-Agent → PORTS-Agent → USECASES-Agent → 
MODELS-Agent → ALEMBIC-Agent → MAPPERS-Agent → REPOSITORIES-Agent → 
ROUTES-Agent → TEST-Agent → QUALITY-Agent (Final)
```

## 📂 Estructura del Proyecto
```
/docs/projects/TFIN/
├── INDEX-TFIN.md                  # Este documento (PLAN-Agent)
├── WP-TFIN-001.md                  # Plan de trabajo (PLAN-Agent)
├── AGENT-CONTEXT-TFIN.md          # Cuaderno de bitácora (Todos los agentes)
├── adrs/
│   └── ADR-TFIN-001.md            # Decisiones arquitectónicas
├── api/
│   └── API-TFIN-001.md            # Endpoints (ROUTES-Agent)
├── migrations/
│   ├── MIG-TFIN-001.sql           # Migraciones (ALEMBIC-Agent)
│   ├── MIG-TFIN-002.sql
│   └── MIG-TFIN-003.md
├── technical/
│   ├── TSD-TFIN-001.md            # Documentación técnica (DOCUMENT-Agent)
│   ├── TSD-TFIN-002.md
│   └── TSD-TFIN-003.md
├── tests/
│   ├── TST-TFIN-001.md            # Planes de testing (TEST-Agent)
│   └── TST-TFIN-002.md
└── agents/
    ├── AGT-TFIN-001-domain.md     # Documentación específica por agente
    ├── AGT-TFIN-002-application.md
    └── AGT-TFIN-003-adapters.md
```

## 🏷️ Metadatos en Documentos

Cada documento debe incluir un header con metadatos (generado automáticamente por agentes):

```yaml
---
codigo: WP-TFIN-001
tipo: Work Plan
proyecto: Totales Financieros
version: 1.0
fecha: 2025-08-29
autor: PLAN-Agent
generado_por: PLAN-Agent
actualizado_por: DOCUMENT-Agent
relacionados: [ADR-TFIN-001, TSD-TFIN-001, MIG-TFIN-001, AGENT-CONTEXT-TFIN]
estado: EN_DESARROLLO
flujo_agentes: secuencial
siguiente_agente: DOMAIN-Agent
---
```

### Metadatos Específicos para Agentes
```yaml
---
codigo: AGENT-CONTEXT-TFIN
tipo: Agent Context
proyecto: Totales Financieros
version: 1.3
fecha: 2025-08-29
autor: PLAN-Agent
ultimo_agente: USECASES-Agent
siguiente_agente: MODELS-Agent
estado_proyecto: APLICACION_COMPLETADA
fase_actual: ADAPTADORES
progreso: 60%
---
```

## 🔍 Beneficios del Sistema con Agentes

1. **Automatización Completa**: Los agentes gestionan toda la documentación
2. **Trazabilidad Total**: AGENT-CONTEXT registra cada paso del proceso
3. **Consistencia Garantizada**: QUALITY-Agent valida toda la documentación
4. **Búsqueda Optimizada**: Estructura predecible generada automáticamente
5. **Versionado Automático**: DOCUMENT-Agent mantiene versiones actualizadas
6. **Relaciones Automáticas**: Enlaces entre documentos gestionados por agentes
7. **Flujo Secuencial**: Documentación sigue el mismo orden que el desarrollo
8. **Escalabilidad**: Sistema crece automáticamente con cada proyecto
9. **Calidad Continua**: Validación en cada paso del proceso
10. **Comunicación Fluida**: AGENT-CONTEXT facilita handoffs entre agentes

## 📝 Reglas de Uso con Agentes

1. **Inicio automático**: Usar `@PLAN-Agent necesito [descripción]` para nuevos proyectos
2. **Flujo secuencial**: Los agentes trabajan uno después del otro, nunca en paralelo
3. **AGENT-CONTEXT obligatorio**: Cada proyecto debe tener su cuaderno de bitácora
4. **Secuenciales**: Siempre usar siguiente número disponible (gestionado por agentes)
5. **Actualizaciones automáticas**: DOCUMENT-Agent mantiene versiones actualizadas
6. **No intervención manual**: Dejar que los agentes gestionen la documentación
7. **Referencias automáticas**: Los agentes mantienen referencias cruzadas correctas
8. **Validación continua**: QUALITY-Agent verifica consistencia automáticamente

## 🤖 Proceso Automatizado con Agentes

### Flujo Secuencial Obligatorio
El sistema de documentación está completamente integrado con el **flujo secuencial de agentes**:

```
PLAN-Agent → DOMAIN-Agent → [DTOS → PORTS → USECASES] → [MODELS → ALEMBIC → MAPPERS → REPOSITORIES → ROUTES] → TEST-Agent
```

### Paso 1: Iniciación Automática (PLAN-Agent)
```
@PLAN-Agent necesito [descripción del proyecto]
```

**El PLAN-Agent automáticamente:**
1. **Genera código único** de 4 letras para el proyecto
2. **Crea estructura** del proyecto en `/docs/projects/[CODIGO]/`
3. **Delega a DOCUMENT-Agent** la creación de:
   - `INDEX-[CODIGO].md` usando plantilla
   - `WP-[CODIGO]-001.md` usando plantilla
4. **Crea AGENT-CONTEXT-[CODIGO].md** con:
   - Resumen del proyecto
   - Componentes a reutilizar
   - Instrucciones para siguientes agentes

### Paso 2: Documentación Continua (DOCUMENT-Agent)
**El DOCUMENT-Agent se ejecuta automáticamente después de cada fase:**
- **Después de DOMAIN-Agent**: Actualiza documentación técnica del dominio
- **Después de cada agente de aplicación**: Documenta DTOs, Ports, Use Cases
- **Después de cada agente de adaptadores**: Documenta Models, Repositories, Routes
- **Después de TEST-Agent**: Actualiza documentación de testing

### Paso 3: Control de Calidad (QUALITY-Agent)
**El QUALITY-Agent valida automáticamente:**
- Consistencia de la documentación
- Completitud de los metadatos
- Referencias cruzadas correctas
- Actualización del AGENT-CONTEXT

### Paso 4: Comunicación Entre Agentes
**AGENT-CONTEXT-[CODIGO].md funciona como cuaderno de bitácora:**
- Cada agente actualiza su progreso
- Registra componentes creados
- Documenta decisiones técnicas
- Proporciona instrucciones para el siguiente agente

## 🔄 Documentos Obligatorios por Proyecto

### Documentos Automáticos (Generados por Agentes)
| Documento | Generado por | Cuándo | Ubicación |
|-----------|--------------|--------|-----------|
| `INDEX-[CODIGO].md` | PLAN-Agent | Inicio del proyecto | Raíz del proyecto |
| `WP-[CODIGO]-001.md` | PLAN-Agent | Inicio del proyecto | Raíz del proyecto |
| `AGENT-CONTEXT-[CODIGO].md` | PLAN-Agent | Inicio del proyecto | Raíz del proyecto |
| Documentación técnica | DOCUMENT-Agent | Después de cada fase | Subcarpetas por tipo |
| Reportes de calidad | QUALITY-Agent | Después de cada agente | AGENT-CONTEXT |

### Documentos Manuales (Opcionales)
- ADR (Architecture Decision Records)
- TSD (Technical Spec Documents) adicionales
- API Documentation específica
- Migration scripts personalizados

## 📊 Ejemplo de Aplicación con Agentes

### Estructura Completa Generada Automáticamente:
```
/.claude/agents/                     # Configuración de agentes (12 archivos)
/docs/projects/TFIN/
├── INDEX-TFIN.md                    # Generado por PLAN-Agent
├── WP-TFIN-001.md                   # Generado por PLAN-Agent
├── AGENT-CONTEXT-TFIN.md           # Cuaderno de bitácora (todos los agentes)
├── adrs/
│   └── ADR-TFIN-001.md
├── api/
│   └── API-TFIN-001.md              # Generado por ROUTES-Agent
├── migrations/
│   ├── MIG-TFIN-001.sql             # Generado por ALEMBIC-Agent
│   └── MIG-TFIN-002.sql
├── technical/
│   ├── TSD-TFIN-001.md              # Generado por DOCUMENT-Agent
│   └── TSD-TFIN-002.md
├── tests/
│   └── TST-TFIN-001.md              # Generado por TEST-Agent
└── agents/
    ├── AGT-TFIN-001-domain.md       # Documentación por agente
    ├── AGT-TFIN-002-application.md
    └── AGT-TFIN-003-adapters.md
```

### Flujo de Creación Automática:
1. **Usuario**: `@PLAN-Agent necesito sistema de totales financieros`
2. **PLAN-Agent**: Crea estructura, INDEX, WP y AGENT-CONTEXT
3. **Agentes secuenciales**: Cada uno actualiza AGENT-CONTEXT y genera documentación
4. **DOCUMENT-Agent**: Mantiene documentación técnica actualizada
5. **QUALITY-Agent**: Valida consistencia en cada paso

---

**Documento creado**: 29/08/2024
**Versión**: 3.0
**Última actualización**: 15/01/2025
**Cambios v2.0**: Reorganización por proyectos en lugar de tipos de documentos
**Cambios v2.1**: Estructura híbrida (Opción B) - INDEX y WP en raíz, subcarpetas por tipo
**Cambios v3.0**: Integración completa con sistema de agentes secuenciales
- Agregado AGENT-CONTEXT como documento obligatorio
- Proceso automatizado con PLAN-Agent y DOCUMENT-Agent
- Flujo secuencial obligatorio (sin paralelismo)
- Metadatos específicos para agentes
- Documentación automática por cada agente especializado
**Próxima revisión**: Según evolución del sistema de agentes
