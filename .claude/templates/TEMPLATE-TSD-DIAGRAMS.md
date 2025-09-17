---
codigo: TSD-[CODIGO]-004-diagrams
tipo: Technical Specification Document - Diagrams
proyecto: [NOMBRE_PROYECTO]
version: 1.0
fecha: [FECHA_ACTUAL]
autor: DOCUMENT-Agent
tipo_contenido: DIAGRAMAS
actualizado_por: [ULTIMO_AGENTE]
relacionados: [TSD-CODIGO-003-architecture, TSD-CODIGO-001-domain]
---

# 📘 Diagramas Técnicos - [NOMBRE_PROYECTO]

## 📋 ÍNDICE DE DIAGRAMAS

### Por Categoría
- **Arquitectura**: [N] diagramas
- **Flujos de Proceso**: [N] diagramas
- **Modelo de Datos**: [N] diagramas
- **Secuencias**: [N] diagramas
- **Estados**: [N] diagramas
- **Despliegue**: [N] diagramas
- **Componentes**: [N] diagramas

### Por Nivel de Detalle
- **Nivel Contexto** (L1): Vista general del sistema
- **Nivel Contenedor** (L2): Principales componentes
- **Nivel Componente** (L3): Detalle interno
- **Nivel Código** (L4): Clases y relaciones

## 🏗️ DIAGRAMAS DE ARQUITECTURA

### Diagrama: Contexto del Sistema (C4-L1)
**Tipo:** Contexto
**Herramienta:** Mermaid
**Propósito:** Mostrar el sistema en su entorno con actores externos

```mermaid
graph TB
    subgraph "Contexto del Sistema"
        U[Usuario] -->|Usa| S[Sistema Principal]
        A[Administrador] -->|Configura| S
        S -->|Consulta| E1[Sistema Externo 1]
        S -->|Envía datos| E2[Sistema Externo 2]
        S -->|Notifica| N[Servicio Notificaciones]
    end
```

**Elementos Clave:**
- **Actores**: [DESCRIPCIÓN DE CADA ACTOR]
- **Interacciones**: [TIPO DE COMUNICACIÓN]
- **Límites**: [QUÉ ESTÁ DENTRO Y FUERA]

### Diagrama: Contenedores (C4-L2)
**Tipo:** Contenedores
**Herramienta:** Mermaid
**Propósito:** Mostrar los contenedores principales y sus interacciones

```mermaid
graph TB
    subgraph "Frontend"
        W[Web App<br/>React]
        M[Mobile App<br/>React Native]
    end
    
    subgraph "Backend"
        API[API REST<br/>Node.js]
        BG[Background Jobs<br/>Python]
    end
    
    subgraph "Data"
        DB[(PostgreSQL<br/>Database)]
        C[(Redis<br/>Cache)]
        Q[RabbitMQ<br/>Queue]
    end
    
    W --> API
    M --> API
    API --> DB
    API --> C
    API --> Q
    BG --> Q
    BG --> DB
```

**Tecnologías:**
| Contenedor | Tecnología | Puerto | Protocolo |
|------------|------------|--------|-----------|
| [Web App] | [React] | [3000] | [HTTPS] |
| [API] | [Node.js] | [8080] | [REST] |
| [Database] | [PostgreSQL] | [5432] | [TCP] |

### Diagrama: Componentes (C4-L3)
**Tipo:** Componentes
**Herramienta:** Mermaid
**Propósito:** Detalle interno de un contenedor

```mermaid
graph TD
    subgraph "API Backend Components"
        subgraph "Presentation"
            CTRL[Controllers]
            VAL[Validators]
        end
        
        subgraph "Application"
            UC[Use Cases]
            DTO[DTOs]
            PORTS[Ports]
        end
        
        subgraph "Domain"
            ENT[Entities]
            VO[Value Objects]
            DS[Domain Services]
        end
        
        subgraph "Infrastructure"
            REPO[Repositories]
            EXT[External Services]
        end
        
        CTRL --> UC
        UC --> PORTS
        PORTS --> DS
        DS --> ENT
        REPO -.-> PORTS
        EXT -.-> PORTS
    end
```

## 🔄 DIAGRAMAS DE FLUJO

### Diagrama: Flujo Principal de Negocio
**Tipo:** Flowchart
**Herramienta:** Mermaid
**Propósito:** Proceso principal del sistema

```mermaid
flowchart TD
    Start([Inicio]) --> Input[Recibir Solicitud]
    Input --> Validate{¿Válida?}
    Validate -->|No| Reject[Rechazar]
    Validate -->|Si| Process[Procesar]
    Process --> CheckRules{¿Cumple reglas?}
    CheckRules -->|No| HandleException[Manejar Excepción]
    CheckRules -->|Si| Save[Guardar]
    Save --> Notify[Notificar]
    Notify --> End([Fin])
    Reject --> End
    HandleException --> End
```

**Decisiones Clave:**
| Punto de Decisión | Criterios | Acción SI | Acción NO |
|-------------------|-----------|-----------|-----------|
| [Validación] | [REGLAS] | [CONTINUAR] | [RECHAZAR] |
| [Reglas Negocio] | [CRITERIOS] | [PROCESAR] | [EXCEPCIÓN] |

### Diagrama: Proceso de Autenticación
**Tipo:** Flowchart
**Herramienta:** Mermaid
**Propósito:** Flujo de autenticación y autorización

```mermaid
flowchart LR
    A[Login Request] --> B{Credenciales<br/>Válidas?}
    B -->|Si| C[Generar Token JWT]
    B -->|No| D[Error 401]
    C --> E[Retornar Token]
    E --> F[Cliente guarda Token]
    F --> G[Request con Token]
    G --> H{Token Válido?}
    H -->|Si| I[Procesar Request]
    H -->|No| J[Error 403]
```

## 📊 DIAGRAMAS DE SECUENCIA

### Diagrama: Secuencia de Creación
**Tipo:** Sequence
**Herramienta:** Mermaid
**Propósito:** Interacción temporal entre componentes

```mermaid
sequenceDiagram
    participant U as Usuario
    participant C as Controller
    participant UC as UseCase
    participant R as Repository
    participant DB as Database
    participant E as EventBus
    
    U->>C: POST /resource
    C->>C: Validar entrada
    C->>UC: execute(dto)
    UC->>UC: Validar reglas negocio
    UC->>R: save(entity)
    R->>DB: INSERT
    DB-->>R: ID
    R-->>UC: Entity saved
    UC->>E: publish(CreatedEvent)
    UC-->>C: Result
    C-->>U: 201 Created
```

**Mensajes:**
| De | A | Mensaje | Tipo | Respuesta |
|----|---|---------|------|-----------|
| [Usuario] | [Controller] | [POST /resource] | [Sync] | [201] |
| [UseCase] | [Repository] | [save()] | [Sync] | [Entity] |
| [UseCase] | [EventBus] | [publish()] | [Async] | [None] |

## 🔀 DIAGRAMAS DE ESTADO

### Diagrama: Estados de una Entidad
**Tipo:** State
**Herramienta:** Mermaid
**Propósito:** Ciclo de vida de entidad principal

```mermaid
stateDiagram-v2
    [*] --> Borrador: Crear
    Borrador --> Pendiente: Enviar
    Pendiente --> Aprobado: Aprobar
    Pendiente --> Rechazado: Rechazar
    Aprobado --> EnProceso: Iniciar
    EnProceso --> Completado: Finalizar
    EnProceso --> Cancelado: Cancelar
    Rechazado --> Borrador: Modificar
    Completado --> [*]
    Cancelado --> [*]
    
    note right of Aprobado
        Requiere autorización
        de administrador
    end note
```

**Transiciones:**
| Estado Origen | Estado Destino | Evento | Condiciones | Acciones |
|---------------|----------------|--------|-------------|----------|
| [Borrador] | [Pendiente] | [Enviar] | [Completo] | [Notificar] |
| [Pendiente] | [Aprobado] | [Aprobar] | [Autorizado] | [Log] |

## 💾 DIAGRAMAS DE DATOS

### Diagrama: Modelo Entidad-Relación
**Tipo:** ERD
**Herramienta:** Mermaid
**Propósito:** Estructura de base de datos

```mermaid
erDiagram
    USER ||--o{ ORDER : places
    USER {
        int id PK
        string email UK
        string name
        datetime created_at
    }
    ORDER ||--|{ ORDER_ITEM : contains
    ORDER {
        int id PK
        int user_id FK
        decimal total
        string status
        datetime created_at
    }
    ORDER_ITEM {
        int id PK
        int order_id FK
        int product_id FK
        int quantity
        decimal price
    }
    PRODUCT ||--o{ ORDER_ITEM : "ordered in"
    PRODUCT {
        int id PK
        string name
        decimal price
        int stock
    }
```

**Relaciones:**
| Entidad A | Relación | Cardinalidad | Entidad B | Constraint |
|-----------|----------|--------------|-----------|------------|
| [User] | places | 1:N | [Order] | CASCADE |
| [Order] | contains | 1:N | [OrderItem] | CASCADE |
| [Product] | ordered_in | 1:N | [OrderItem] | RESTRICT |

## 🚀 DIAGRAMAS DE DESPLIEGUE

### Diagrama: Infraestructura de Producción
**Tipo:** Deployment
**Herramienta:** Mermaid
**Propósito:** Arquitectura de despliegue

```mermaid
graph TB
    subgraph "Internet"
        Users[Usuarios]
    end
    
    subgraph "CDN"
        CF[CloudFlare]
    end
    
    subgraph "AWS Cloud"
        subgraph "Public Subnet"
            ALB[Application<br/>Load Balancer]
        end
        
        subgraph "Private Subnet 1"
            EC2A[EC2 Instance A<br/>App Server]
            EC2B[EC2 Instance B<br/>App Server]
        end
        
        subgraph "Private Subnet 2"
            RDS[(RDS PostgreSQL<br/>Primary)]
            RDSR[(RDS PostgreSQL<br/>Read Replica)]
        end
        
        subgraph "ElastiCache"
            REDIS[(Redis Cluster)]
        end
    end
    
    Users --> CF
    CF --> ALB
    ALB --> EC2A
    ALB --> EC2B
    EC2A --> RDS
    EC2B --> RDS
    EC2A --> REDIS
    EC2B --> REDIS
    RDS --> RDSR
```

**Especificaciones:**
| Componente | Tipo | Especificación | Cantidad | Auto-scaling |
|------------|------|----------------|----------|--------------|
| [EC2] | [t3.large] | [2CPU/8GB] | [2-10] | [Si] |
| [RDS] | [db.r5.large] | [2CPU/16GB] | [1+1] | [No] |
| [Redis] | [cache.m5.large] | [2CPU/8GB] | [3] | [No] |

## 🔧 DIAGRAMAS DE CLASES

### Diagrama: Modelo de Dominio
**Tipo:** Class
**Herramienta:** Mermaid
**Propósito:** Estructura de clases del dominio

```mermaid
classDiagram
    class Order {
        -String id
        -Customer customer
        -List~OrderItem~ items
        -OrderStatus status
        -Money total
        +addItem(Product, quantity)
        +removeItem(OrderItem)
        +calculateTotal()
        +approve()
        +cancel()
    }
    
    class OrderItem {
        -String id
        -Product product
        -int quantity
        -Money unitPrice
        +calculateSubtotal()
    }
    
    class Product {
        -String id
        -String name
        -Money price
        -int stock
        +hasStock(quantity)
        +decreaseStock(quantity)
    }
    
    class Customer {
        -String id
        -String name
        -Email email
        +canPlaceOrder()
    }
    
    class Money {
        -BigDecimal amount
        -Currency currency
        +add(Money)
        +multiply(int)
    }
    
    Order "1" --> "*" OrderItem : contains
    OrderItem "*" --> "1" Product : references
    Order "*" --> "1" Customer : belongs to
    Order --> Money : uses
    OrderItem --> Money : uses
    Product --> Money : uses
```

**Patrones Aplicados:**
| Patrón | Clases Involucradas | Propósito |
|--------|-------------------|-----------|
| [Aggregate] | [Order, OrderItem] | [Consistencia] |
| [Value Object] | [Money, Email] | [Inmutabilidad] |
| [Entity] | [Customer, Product] | [Identidad] |

## 📐 DIAGRAMAS DE ACTIVIDADES

### Diagrama: Proceso de Negocio
**Tipo:** Activity
**Herramienta:** Mermaid
**Propósito:** Actividades y decisiones del proceso

```mermaid
graph TD
    Start([Inicio Proceso]) --> A[Actividad 1]
    A --> B{¿Decisión?}
    B -->|Opción 1| C[Actividad 2A]
    B -->|Opción 2| D[Actividad 2B]
    C --> E[Actividad 3]
    D --> E
    E --> F{¿Otra Decisión?}
    F -->|Si| G[Actividad 4]
    F -->|No| End([Fin Proceso])
    G --> End
```

## 🎨 CONVENCIONES DE DIAGRAMAS

### Colores y Estilos
| Elemento | Color | Estilo | Significado |
|----------|-------|--------|-------------|
| Entidad Externa | Gris | Punteado | Fuera del sistema |
| Componente Core | Azul | Sólido | Lógica principal |
| Base de Datos | Verde | Cilindro | Persistencia |
| Servicio Externo | Naranja | Nube | Integración |
| Error/Excepción | Rojo | Doble línea | Flujo de error |

### Nomenclatura
- **Nodos**: PascalCase para clases, camelCase para instancias
- **Relaciones**: Verbos en minúsculas
- **Cardinalidad**: Notación UML (1, *, 0..1, 1..*)
- **Flechas**: → para flujo, -- para asociación, ..> para dependencia

### Niveles de Detalle
| Nivel | Audiencia | Contenido | Herramienta Sugerida |
|-------|-----------|-----------|---------------------|
| L1 | Stakeholders | Contexto general | Draw.io |
| L2 | Arquitectos | Contenedores | Mermaid |
| L3 | Desarrolladores | Componentes | PlantUML |
| L4 | Implementadores | Clases/Código | IDE/Mermaid |

## 🛠️ HERRAMIENTAS Y EXPORTACIÓN

### Herramientas Recomendadas
| Herramienta | Tipo de Diagrama | Formato Exportación | Versionable |
|-------------|------------------|-------------------|-------------|
| Mermaid | Todos | SVG, PNG | Si (texto) |
| PlantUML | UML | SVG, PNG | Si (texto) |
| Draw.io | Complejos | XML, SVG, PNG | Si (XML) |
| Lucidchart | Colaborativos | PDF, PNG | No |
| C4-PlantUML | C4 Model | SVG, PNG | Si (texto) |

### Ubicación de Archivos
```
/docs/projects/[CODIGO]/diagrams/
├── source/           # Archivos fuente (.mmd, .puml, .xml)
├── exported/         # Imágenes exportadas (.svg, .png)
└── README.md        # Índice y descripción de diagramas
```

## 📝 MANTENIMIENTO DE DIAGRAMAS

### Checklist de Actualización
- [ ] Diagrama refleja el estado actual del sistema
- [ ] Versión y fecha actualizadas
- [ ] Exportación en formato versionable
- [ ] Exportación en formato visual
- [ ] Documentación de cambios
- [ ] Enlaces desde documentos relacionados

### Registro de Cambios
| Fecha | Diagrama | Cambio | Responsable | Razón |
|-------|----------|--------|-------------|-------|
| [FECHA] | [NOMBRE] | [DESCRIPCIÓN] | [AGENTE] | [MOTIVO] |

## 🔗 REFERENCIAS

### Documentación Relacionada
- [Architecture Doc](TSD-[CODIGO]-003-architecture.md)
- [Domain Doc](TSD-[CODIGO]-001-domain.md)
- [Database Doc](TSD-[CODIGO]-002-database.md)

### Recursos de Diagramación
- [Mermaid Live Editor](https://mermaid.live)
- [PlantUML Server](http://www.plantuml.com/plantuml)
- [C4 Model](https://c4model.com)
- [UML Guide](https://www.uml.org)

---

**Documento Creado:** [FECHA]
**Autor:** DOCUMENT-Agent
**Última Actualización:** [FECHA]
**Herramienta Principal:** Mermaid

<!-- 
INSTRUCCIONES PARA AGENTES:

1. DOCUMENT-Agent:
   - Crear/actualizar diagramas después de cambios
   - Mantener consistencia con código
   - Exportar en formatos versionables

2. Todos los Agentes:
   - Notificar cambios que afecten diagramas
   - Validar que diagramas reflejan realidad
   - Usar diagramas como referencia

3. QUALITY-Agent:
   - Verificar actualización de diagramas
   - Validar consistencia con implementación
   - Revisar convenciones

Los diagramas son DOCUMENTACIÓN VISUAL
Deben estar SIEMPRE actualizados
Un diagrama vale más que mil palabras
-->
