# 🔄 Flujo Completo de Agentes con QUALITY-Agent

## Flujo General de Control

```mermaid
graph LR
    Start([Nueva Solicitud]) --> PLAN1[PLAN-Agent<br/>Planifica y Asigna]
    PLAN1 --> CHOICE{Asigna Capa}
    
    CHOICE -->|Capa Dominio| DOMAIN_LAYER[Capa de Dominio]
    CHOICE -->|Capa Aplicación| APP_LAYER[Capa de Aplicación]
    CHOICE -->|Capa Adaptadores| ADAPTER_LAYER[Capa de Adaptadores]
    
    DOMAIN_LAYER --> VALIDATE{QUALITY-Agent<br/>Validación Final}
    APP_LAYER --> VALIDATE
    ADAPTER_LAYER --> VALIDATE
    
    VALIDATE -->|Aprobado| COMPLETE([Tarea Completada])
    VALIDATE -->|Requiere Ajustes| RETRY{¿Requiere<br/>Corrección?}
    RETRY -->|Sí| PLAN1
    RETRY -->|No| COMPLETE
```

## Flujo estandar para cada agente

```mermaid
graph LR
    A[Agente X] -->|Ejecuta tarea| B[Genera código]
    B -->|Actualiza| C[AGENT-CONTEXT]
    C -->|Instruye| D[DOCUMENT-Agent]
    D -->|Crea/Actualiza| E[Documentación]
    E -->|Reporta| F[AGENT-CONTEXT]
```

## 1. Capa de Dominio

```mermaid
graph TB
    PLAN_IN[PLAN-Agent<br/>Asigna Tarea] --> DOMAIN_CHOICE{Tipo de Tarea<br/>Dominio}
    
    DOMAIN_CHOICE -->|Implementar Entidad| DOMAIN[DOMAIN-Agent<br/>Implementa Entidad]
    DOMAIN_CHOICE -->|Documentar| DOCS1[DOCUMENT-Agent<br/>Actualiza Docs]
    DOMAIN_CHOICE -->|Testing| TEST1[TEST-Agent<br/>Tests Unitarios]
    DOMAIN_CHOICE -->|Revisar Calidad| QA1[QUALITY-Agent<br/>Revisa Código]
    
    %% Flujo de trabajo
    DOMAIN --> DOCS1
    DOMAIN --> TEST1
    DOMAIN --> QA1
    
    %% Reportes de retorno
    DOCS1 -.->|Reporte| PLAN_OUT[Reporte a PLAN-Agent]
    TEST1 -.->|Resultados| PLAN_OUT
    QA1 --> PLAN_OUT
    
    %% Estilos
    classDef domainAgent fill:#e1f5fe
    classDef supportAgent fill:#f3e5f5
    classDef qualityAgent fill:#e8f5e8
    
    class DOMAIN domainAgent
    class DOCS1,TEST1 supportAgent
    class QA1 qualityAgent
```

## 2. Capa de Aplicación (Secuencia Ordenada)

```mermaid
graph TB
    PLAN_IN[PLAN-Agent<br/>Asigna Tarea] --> STEP1{PASO 1<br/>DTOs Primero}
    
    %% PASO 1: DTOs
    STEP1 --> DTOS[DTOS-Agent<br/>Implementa DTOs]
    DTOS --> DOCS2[DOCUMENT-Agent<br/>Docs DTOs]
    DTOS --> TEST2[TEST-Agent<br/>Tests DTOs]
    DTOS --> QA2[QUALITY-Agent<br/>Revisión DTOs]
    
    %% PASO 2: Ports (dependen de DTOs)
    QA2 -->|DTOs Aprobados| STEP2{PASO 2<br/>Ports Segundo}
    STEP2 --> PORTS[PORTS-Agent<br/>Implementa Ports]
    PORTS --> DOCS3[DOCUMENT-Agent<br/>Docs Ports]
    PORTS --> TEST3[TEST-Agent<br/>Tests Ports]
    PORTS --> QA3[QUALITY-Agent<br/>Revisión Ports]
    
    %% PASO 3: Use Cases (dependen de DTOs y Ports)
    QA3 -->|Ports Aprobados| STEP3{PASO 3<br/>Use Cases Final}
    STEP3 --> USECASES[USECASES-Agent<br/>Implementa Use Cases]
    USECASES --> DOCS4[DOCUMENT-Agent<br/>Docs Use Cases]
    USECASES --> TEST4[TEST-Agent<br/>Tests Use Cases]
    USECASES --> QA4[QUALITY-Agent<br/>Revisión Use Cases]
    
    %% Reportes de retorno
    DOCS2 -.->|Reporte| PLAN_OUT[Reporte a PLAN-Agent]
    DOCS3 -.->|Reporte| PLAN_OUT
    DOCS4 -.->|Reporte| PLAN_OUT
    TEST2 -.->|Resultados| PLAN_OUT
    TEST3 -.->|Resultados| PLAN_OUT
    TEST4 -.->|Resultados| PLAN_OUT
    QA2 -.->|Estado| PLAN_OUT
    QA3 -.->|Estado| PLAN_OUT
    QA4 --> PLAN_OUT
    
    %% Dependencias visuales
    DTOS -.->|Contratos| PORTS
    DTOS -.->|Contratos| USECASES
    PORTS -.->|Interfaces| USECASES
    
    %% Estilos
    classDef appAgent fill:#fff3e0
    classDef supportAgent fill:#f3e5f5
    classDef qualityAgent fill:#e8f5e8
    classDef sequenceNode fill:#ffecb3
    
    class DTOS,PORTS,USECASES appAgent
    class DOCS2,DOCS3,DOCS4,TEST2,TEST3,TEST4 supportAgent
    class QA2,QA3,QA4 qualityAgent
    class STEP1,STEP2,STEP3 sequenceNode
```

## 3. Capa de Adaptadores (Secuencia Ordenada)

```mermaid
graph TB
    PLAN_IN[PLAN-Agent<br/>Asigna Tarea] --> STEP1{PASO 1<br/>Models Base}
    
    %% PASO 1: Models (base de datos)
    STEP1 --> MODELS[MODELS-Agent<br/>Implementa Models]
    MODELS --> DOCS6[DOCUMENT-Agent<br/>Docs Models]
    MODELS --> TEST6[TEST-Agent<br/>Tests Models]
    MODELS --> QA6[QUALITY-Agent<br/>Revisión Models]
    
    %% PASO 2: Alembic (depende de Models)
    QA6 -->|Models Aprobados| STEP2{PASO 2<br/>Migraciones}
    STEP2 --> ALEMBIC[ALEMBIC-Agent<br/>Implementa Migraciones]
    ALEMBIC --> DOCS7[DOCUMENT-Agent<br/>Docs Migraciones]
    ALEMBIC --> TEST7[TEST-Agent<br/>Tests Migraciones]
    ALEMBIC --> QA7[QUALITY-Agent<br/>Revisión Migraciones]
    
    %% PASO 3: Mappers (depende de Models)
    QA7 -->|Migraciones Aprobadas| STEP3{PASO 3<br/>Mappers}
    STEP3 --> MAPPERS[MAPPERS-Agent<br/>Implementa Mappers]
    MAPPERS --> DOCS5[DOCUMENT-Agent<br/>Docs Mappers]
    MAPPERS --> TEST5[TEST-Agent<br/>Tests Mappers]
    MAPPERS --> QA5[QUALITY-Agent<br/>Revisión Mappers]
    
    %% PASO 4: Repositories (depende de Models y Mappers)
    QA5 -->|Mappers Aprobados| STEP4{PASO 4<br/>Repositories}
    STEP4 --> REPOS[REPOSITORIES-Agent<br/>Implementa Repositories]
    REPOS --> DOCS8[DOCUMENT-Agent<br/>Docs Repositories]
    REPOS --> TEST8[TEST-Agent<br/>Tests Repositories]
    REPOS --> QA8[QUALITY-Agent<br/>Revisión Repositories]
    
    %% PASO 5: Routes (depende de Repositories)
    QA8 -->|Repositories Aprobados| STEP5{PASO 5<br/>Routes Final}
    STEP5 --> ROUTES[ROUTES-Agent<br/>Implementa Routes]
    ROUTES --> DOCS9[DOCUMENT-Agent<br/>Docs Routes]
    ROUTES --> TEST9[TEST-Agent<br/>Tests Routes]
    ROUTES --> QA9[QUALITY-Agent<br/>Revisión Routes]
    
    %% Reportes de retorno
    DOCS5 -.->|Reporte| PLAN_OUT[Reporte a PLAN-Agent]
    DOCS6 -.->|Reporte| PLAN_OUT
    DOCS7 -.->|Reporte| PLAN_OUT
    DOCS8 -.->|Reporte| PLAN_OUT
    DOCS9 -.->|Reporte| PLAN_OUT
    TEST5 -.->|Resultados| PLAN_OUT
    TEST6 -.->|Resultados| PLAN_OUT
    TEST7 -.->|Resultados| PLAN_OUT
    TEST8 -.->|Resultados| PLAN_OUT
    TEST9 -.->|Resultados| PLAN_OUT
    QA5 -.->|Estado| PLAN_OUT
    QA6 -.->|Estado| PLAN_OUT
    QA7 -.->|Estado| PLAN_OUT
    QA8 -.->|Estado| PLAN_OUT
    QA9 --> PLAN_OUT
    
    %% Dependencias visuales
    MODELS -.->|Estructura| ALEMBIC
    MODELS -.->|Esquema| MAPPERS
    MODELS -.->|Entidades| REPOS
    MAPPERS -.->|Transformaciones| REPOS
    REPOS -.->|Persistencia| ROUTES
    
    %% Estilos
    classDef adapterAgent fill:#e8eaf6
    classDef supportAgent fill:#f3e5f5
    classDef qualityAgent fill:#e8f5e8
    classDef sequenceNode fill:#ffecb3
    
    class MAPPERS,MODELS,ALEMBIC,REPOS,ROUTES adapterAgent
    class DOCS5,DOCS6,DOCS7,DOCS8,DOCS9,TEST5,TEST6,TEST7,TEST8,TEST9 supportAgent
    class QA5,QA6,QA7,QA8,QA9 qualityAgent
    class STEP1,STEP2,STEP3,STEP4,STEP5 sequenceNode
```

## Características del Flujo

### Flujo de Retorno y Control de Calidad

1. **Validación Centralizada**: Todos los agentes QUALITY reportan a una validación final
2. **Control de Iteraciones**: Si se detectan problemas, el flujo regresa al PLAN-Agent
3. **Reportes Informativos**: Los agentes DOCUMENT y TEST envían reportes continuos (líneas punteadas)
4. **Finalización Controlada**: Solo se completa la tarea cuando pasa la validación final

### Secuenciación en Capa de Aplicación

La capa de aplicación sigue un **orden estricto de desarrollo** basado en dependencias arquitecturales:

#### 1. DTOs (Data Transfer Objects) - PRIMERO
- **Propósito**: Definen los contratos de entrada y salida del sistema
- **Dependencias**: Ninguna (punto de partida)
- **Razón**: Establecen la estructura de datos que usarán todos los demás componentes

#### 2. Ports (Interfaces) - SEGUNDO  
- **Propósito**: Definen las interfaces para interactuar con el exterior
- **Dependencias**: Requieren DTOs para definir parámetros y tipos de retorno
- **Razón**: Los Ports necesitan conocer qué DTOs van a manejar en sus métodos

#### 3. Use Cases (Casos de Uso) - TERCERO
- **Propósito**: Implementan la lógica de negocio de la aplicación
- **Dependencias**: Requieren tanto DTOs como Ports
- **Razón**: Los Use Cases orquestan la lógica usando DTOs y dependiendo de Ports

#### Flujo de Dependencias
```
DTOs → Ports → Use Cases
  ↓      ↓        ↓
Contratos → Interfaces → Lógica
```

### Secuenciación en Capa de Adaptadores

La capa de adaptadores sigue un **orden estricto de desarrollo** basado en dependencias técnicas:

#### 1. Models (Modelos de Base de Datos) - PRIMERO
- **Propósito**: Definen la estructura de datos de persistencia (tablas, campos, relaciones)
- **Dependencias**: Ninguna (punto de partida técnico)
- **Razón**: Base fundamental para migraciones, mappers y repositories

#### 2. Alembic (Migraciones) - SEGUNDO
- **Propósito**: Crean y mantienen el esquema de base de datos
- **Dependencias**: Requieren Models para generar las migraciones
- **Razón**: Las migraciones deben reflejar la estructura definida en Models

#### 3. Mappers (Transformadores) - TERCERO
- **Propósito**: Transforman entre Models (BD) y DTOs (dominio)
- **Dependencias**: Requieren Models para conocer la estructura de datos
- **Razón**: Necesitan saber qué campos mapear entre capas

#### 4. Repositories (Persistencia) - CUARTO
- **Propósito**: Implementan la lógica de acceso a datos
- **Dependencias**: Requieren Models (para queries) y Mappers (para transformaciones)
- **Razón**: Usan Models para persistir y Mappers para convertir datos

#### 5. Routes (Endpoints) - QUINTO
- **Propósito**: Exponen los endpoints HTTP de la API
- **Dependencias**: Requieren Repositories para acceder a datos
- **Razón**: Los endpoints necesitan repositories para procesar requests

#### Flujo de Dependencias Técnicas
```
Models → Alembic (migraciones)
Models → Mappers (transformaciones)
Models + Mappers → Repositories (persistencia)
Repositories → Routes (endpoints)
```

### Código de Colores

- **Azul claro**: Agentes de Dominio
- **Naranja claro**: Agentes de Aplicación  
- **Púrpura claro**: Agentes de Adaptadores
- **Rosa claro**: Agentes de Soporte (DOCUMENT, TEST)
- **Verde claro**: Agentes de Calidad (QUALITY)
- **Amarillo claro**: Nodos de Secuencia (orden de desarrollo)

