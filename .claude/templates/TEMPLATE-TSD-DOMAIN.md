---
codigo: TSD-[CODIGO]-001-domain
tipo: Technical Specification Document - Domain
proyecto: [NOMBRE_PROYECTO]
version: 1.0
fecha: [FECHA_ACTUAL]
autor: DOCUMENT-Agent
capa: DOMINIO
actualizado_por: DOMAIN-Agent
relacionados: [WP-CODIGO, AGENT-CONTEXT-CODIGO]
---

# 📘 Especificación Técnica del Dominio - [NOMBRE_PROYECTO]

## 🎯 VISIÓN GENERAL DEL DOMINIO

### Contexto de Negocio
[DESCRIPCIÓN DEL CONTEXTO DE NEGOCIO QUE MODELA ESTE DOMINIO]

### Bounded Context
**Nombre:** [NOMBRE_DEL_CONTEXTO_DELIMITADO]
**Descripción:** [QUÉ INCLUYE Y QUÉ NO INCLUYE ESTE CONTEXTO]
**Fronteras:** [LÍMITES CLAROS CON OTROS CONTEXTOS]

### Lenguaje Ubicuo
| Término de Negocio | Definición | Sinónimos a Evitar | Representación en Código |
|--------------------|------------|-------------------|--------------------------|
| [TÉRMINO] | [DEFINICIÓN CLARA] | [TÉRMINOS CONFUSOS] | [CLASE/CONCEPTO] |
| [TÉRMINO] | [DEFINICIÓN CLARA] | [TÉRMINOS CONFUSOS] | [CLASE/CONCEPTO] |
| [TÉRMINO] | [DEFINICIÓN CLARA] | [TÉRMINOS CONFUSOS] | [CLASE/CONCEPTO] |

## 🏗️ ARQUITECTURA DEL DOMINIO

### Modelo de Capas
```
[DIAGRAMA DE CAPAS DEL DOMINIO]

├── Entidades
│   └── Reglas de negocio fundamentales
├── Value Objects
│   └── Conceptos inmutables del dominio
├── Agregados
│   └── Límites de consistencia
├── Servicios de Dominio
│   └── Lógica que no pertenece a entidades
└── Eventos de Dominio
    └── Hechos del negocio
```

### Principios DDD Aplicados
| Principio | Implementación | Beneficio |
|-----------|----------------|-----------|
| Aggregates | [CÓMO SE DEFINEN] | [CONSISTENCIA] |
| Value Objects | [CUÁLES Y POR QUÉ] | [INMUTABILIDAD] |
| Domain Events | [EVENTOS IDENTIFICADOS] | [DESACOPLAMIENTO] |
| Repositories | [ABSTRACCIÓN DE PERSISTENCIA] | [INDEPENDENCIA] |

## 📦 AGREGADOS

### Agregado: [NOMBRE_AGREGADO_1]
**Raíz del Agregado:** [ENTIDAD_RAÍZ]
**Propósito:** [QUÉ GESTIONA ESTE AGREGADO]

#### Componentes del Agregado
| Componente | Tipo | Responsabilidad | Invariantes |
|------------|------|-----------------|-------------|
| [NOMBRE] | Entidad Raíz | [RESPONSABILIDAD] | [REGLAS] |
| [NOMBRE] | Entidad | [RESPONSABILIDAD] | [REGLAS] |
| [NOMBRE] | Value Object | [RESPONSABILIDAD] | [REGLAS] |

#### Reglas de Consistencia
1. [REGLA 1 - QUE SIEMPRE DEBE CUMPLIRSE]
2. [REGLA 2 - QUE SIEMPRE DEBE CUMPLIRSE]
3. [REGLA 3 - QUE SIEMPRE DEBE CUMPLIRSE]

#### Límites Transaccionales
- **Qué se modifica junto:** [ELEMENTOS]
- **Qué requiere consistencia eventual:** [ELEMENTOS]
- **Operaciones atómicas:** [LISTADO]

### Agregado: [NOMBRE_AGREGADO_2]
[REPETIR ESTRUCTURA PARA CADA AGREGADO]

## 🔷 ENTIDADES

### Entidad: [NOMBRE_ENTIDAD_1]
**Identidad:** [CÓMO SE IDENTIFICA ÚNICAMENTE]
**Ciclo de Vida:** [ESTADOS Y TRANSICIONES]

#### Atributos
| Atributo | Tipo | Obligatorio | Reglas de Validación | Mutabilidad |
|----------|------|-------------|---------------------|-------------|
| [NOMBRE] | [TIPO] | [SI/NO] | [REGLAS] | [INMUTABLE/MUTABLE] |
| [NOMBRE] | [TIPO] | [SI/NO] | [REGLAS] | [INMUTABLE/MUTABLE] |

#### Comportamientos
| Método | Propósito | Pre-condiciones | Post-condiciones | Eventos Emitidos |
|--------|-----------|-----------------|------------------|------------------|
| [NOMBRE] | [QUÉ HACE] | [ESTADO REQUERIDO] | [ESTADO RESULTANTE] | [EVENTOS] |
| [NOMBRE] | [QUÉ HACE] | [ESTADO REQUERIDO] | [ESTADO RESULTANTE] | [EVENTOS] |

#### Estados y Transiciones
```
[DIAGRAMA DE ESTADOS]

INICIAL → ACTIVO → PROCESADO → FINALIZADO
         ↓      ↗
      SUSPENDIDO
```

#### Invariantes
- [INVARIANTE 1 - REGLA QUE SIEMPRE SE CUMPLE]
- [INVARIANTE 2 - REGLA QUE SIEMPRE SE CUMPLE]

### Entidad: [NOMBRE_ENTIDAD_2]
[REPETIR ESTRUCTURA PARA CADA ENTIDAD]

## 💎 VALUE OBJECTS

### Value Object: [NOMBRE_VO_1]
**Inmutabilidad:** Garantizada
**Igualdad:** Por valor, no por referencia

#### Propiedades
| Propiedad | Tipo | Validación | Ejemplo |
|-----------|------|------------|---------|
| [NOMBRE] | [TIPO] | [REGLA] | [VALOR] |
| [NOMBRE] | [TIPO] | [REGLA] | [VALOR] |

#### Métodos de Creación
| Factory Method | Validaciones | Retorno |
|----------------|--------------|---------|
| [CREAR_DESDE_X] | [QUÉ VALIDA] | [VO o ERROR] |
| [CREAR_VALIDO] | [QUÉ VALIDA] | [VO o ERROR] |

#### Operaciones
| Operación | Descripción | Retorna Nuevo VO |
|-----------|-------------|------------------|
| [NOMBRE] | [QUÉ HACE] | [SI/NO] |

### Value Object: [NOMBRE_VO_2]
[REPETIR ESTRUCTURA PARA CADA VALUE OBJECT]

## ⚡ EVENTOS DE DOMINIO

### Evento: [NOMBRE_EVENTO_1]
**Trigger:** [QUÉ LO DISPARA]
**Significado de Negocio:** [QUÉ REPRESENTA]

#### Payload del Evento
| Campo | Tipo | Descripción | Obligatorio |
|-------|------|-------------|-------------|
| [CAMPO] | [TIPO] | [DESCRIPCIÓN] | [SI/NO] |
| [CAMPO] | [TIPO] | [DESCRIPCIÓN] | [SI/NO] |

#### Handlers/Suscriptores
| Handler | Acción | Sincronía |
|---------|--------|-----------|
| [SERVICIO] | [QUÉ HACE] | [SYNC/ASYNC] |
| [SERVICIO] | [QUÉ HACE] | [SYNC/ASYNC] |

### Evento: [NOMBRE_EVENTO_2]
[REPETIR ESTRUCTURA PARA CADA EVENTO]

## 🔧 SERVICIOS DE DOMINIO

### Servicio: [NOMBRE_SERVICIO_1]
**Propósito:** [QUÉ LÓGICA ENCAPSULA]
**Justificación:** [POR QUÉ NO ESTÁ EN UNA ENTIDAD]

#### Operaciones
| Operación | Entrada | Salida | Lógica de Negocio |
|-----------|---------|--------|-------------------|
| [MÉTODO] | [PARAMS] | [RETURN] | [DESCRIPCIÓN] |
| [MÉTODO] | [PARAMS] | [RETURN] | [DESCRIPCIÓN] |

#### Dependencias
- [REPOSITORIO O SERVICIO QUE NECESITA]
- [OTRO SERVICIO DE DOMINIO]

### Servicio: [NOMBRE_SERVICIO_2]
[REPETIR ESTRUCTURA PARA CADA SERVICIO]

## 📐 REGLAS DE NEGOCIO

### Reglas Fundamentales
| ID | Regla | Aplicación | Consecuencia de Violación |
|----|-------|------------|---------------------------|
| RN-01 | [REGLA INVIOLABLE] | [DÓNDE SE APLICA] | [QUÉ PASA SI SE VIOLA] |
| RN-02 | [REGLA INVIOLABLE] | [DÓNDE SE APLICA] | [QUÉ PASA SI SE VIOLA] |

### Validaciones de Dominio
| Validación | Contexto | Implementación | Mensaje de Error |
|------------|----------|----------------|------------------|
| [NOMBRE] | [CUÁNDO APLICA] | [DÓNDE ESTÁ] | [MENSAJE USER-FRIENDLY] |
| [NOMBRE] | [CUÁNDO APLICA] | [DÓNDE ESTÁ] | [MENSAJE USER-FRIENDLY] |

### Cálculos de Negocio
| Cálculo | Fórmula | Variables | Ubicación |
|---------|---------|-----------|-----------|
| [NOMBRE] | [FÓRMULA] | [INPUTS] | [ENTIDAD/SERVICIO] |

## 🔄 FLUJOS DE NEGOCIO

### Flujo: [NOMBRE_PROCESO_1]
```
[DIAGRAMA DEL FLUJO]

Inicio → Validación → Proceso → Evento → Fin
           ↓
        Rechazo
```

#### Pasos del Flujo
| Paso | Acción | Responsable | Validaciones | Resultado |
|------|--------|-------------|--------------|-----------|
| 1 | [ACCIÓN] | [ENTIDAD/SERVICIO] | [VALIDACIONES] | [OUTPUT] |
| 2 | [ACCIÓN] | [ENTIDAD/SERVICIO] | [VALIDACIONES] | [OUTPUT] |

### Flujo: [NOMBRE_PROCESO_2]
[REPETIR ESTRUCTURA PARA CADA FLUJO]

## 🗄️ REPOSITORIOS (Interfaces)

### Repositorio: [NOMBRE_REPOSITORIO_1]
**Agregado:** [AGREGADO QUE PERSISTE]
**Tipo:** [COMMAND|QUERY|AMBOS]

#### Operaciones Definidas
| Operación | Propósito | Parámetros | Retorno |
|-----------|-----------|------------|---------|
| [GUARDAR] | [PERSISTIR AGREGADO] | [AGREGADO] | [VOID/ID] |
| [OBTENER_POR_ID] | [RECUPERAR] | [ID] | [AGREGADO/NULL] |
| [BUSCAR] | [QUERY] | [CRITERIOS] | [LISTA] |

### Repositorio: [NOMBRE_REPOSITORIO_2]
[REPETIR ESTRUCTURA PARA CADA REPOSITORIO]

## 🏭 FACTORIES

### Factory: [NOMBRE_FACTORY_1]
**Crea:** [QUÉ TIPO DE OBJETO]
**Complejidad:** [POR QUÉ NECESITA FACTORY]

#### Métodos de Creación
| Método | Entrada | Validaciones | Salida |
|--------|---------|--------------|--------|
| [CREAR_DESDE_DTO] | [DTO] | [VALIDACIONES] | [ENTIDAD] |
| [CREAR_DEFAULT] | [PARAMS] | [VALIDACIONES] | [ENTIDAD] |

## 🎭 POLÍTICAS DE DOMINIO

### Política: [NOMBRE_POLÍTICA_1]
**Aplica a:** [CONTEXTO]
**Tipo:** [SINCRÓNICA|ASINCRÓNICA]

#### Reglas de la Política
1. [REGLA 1]
2. [REGLA 2]
3. [REGLA 3]

#### Implementación
- **Ubicación:** [DÓNDE ESTÁ IMPLEMENTADA]
- **Trigger:** [QUÉ LA ACTIVA]
- **Resultado:** [QUÉ PRODUCE]

## 🔐 ASPECTOS DE SEGURIDAD DEL DOMINIO

### Control de Acceso
| Recurso | Operación | Regla de Autorización |
|---------|-----------|----------------------|
| [ENTIDAD] | [CREAR] | [QUIÉN PUEDE] |
| [ENTIDAD] | [MODIFICAR] | [QUIÉN PUEDE] |
| [ENTIDAD] | [ELIMINAR] | [QUIÉN PUEDE] |

### Auditoría del Dominio
| Evento | Qué se Audita | Información Registrada |
|--------|---------------|------------------------|
| [CREAR_X] | [CREACIÓN] | [USUARIO, FECHA, DATOS] |
| [MODIFICAR_X] | [CAMBIOS] | [USUARIO, FECHA, ANTES/DESPUÉS] |

## 📊 MÉTRICAS DEL DOMINIO

### Complejidad
| Agregado | Entidades | Value Objects | Servicios | Complejidad Total |
|----------|-----------|---------------|-----------|-------------------|
| [NOMBRE] | [N] | [N] | [N] | [BAJA/MEDIA/ALTA] |

### Cobertura de Reglas de Negocio
| Categoría | Total Reglas | Implementadas | Testeadas | Coverage |
|-----------|--------------|---------------|-----------|----------|
| Validaciones | [N] | [N] | [N] | [%] |
| Cálculos | [N] | [N] | [N] | [%] |
| Políticas | [N] | [N] | [N] | [%] |

## 🧪 CONSIDERACIONES DE TESTING

### Tests del Dominio
| Tipo | Qué Testear | Prioridad | Herramientas |
|------|-------------|-----------|--------------|
| Unitarios | Entidades y VOs | ALTA | [FRAMEWORK] |
| Integración | Agregados completos | ALTA | [FRAMEWORK] |
| Reglas de Negocio | Todas las validaciones | CRÍTICA | [FRAMEWORK] |

### Casos de Test Críticos
- [CASO 1 - INVARIANTE PRINCIPAL]
- [CASO 2 - FLUJO HAPPY PATH]
- [CASO 3 - VALIDACIONES LÍMITE]

## 📝 DECISIONES DE DISEÑO

### Decisiones Arquitectónicas
| Decisión | Alternativas | Justificación | Trade-offs |
|----------|--------------|---------------|------------|
| [DECISIÓN] | [OPCIONES] | [POR QUÉ] | [PROS/CONTRAS] |

### Patrones Aplicados
| Patrón | Dónde | Por qué | Beneficio |
|--------|-------|---------|-----------|
| [AGGREGATE] | [UBICACIÓN] | [JUSTIFICACIÓN] | [VENTAJA] |
| [SPECIFICATION] | [UBICACIÓN] | [JUSTIFICACIÓN] | [VENTAJA] |

## 🔗 REFERENCIAS

### Documentación Relacionada
- [Work Plan](WP-[CODIGO]-001.md)
- [Agent Context](AGENT-CONTEXT-[CODIGO].md)
- [API Documentation](API-[CODIGO]-001.md)

### Referencias de Dominio
- [DOCUMENTACIÓN DE NEGOCIO]
- [GLOSARIO DE TÉRMINOS]
- [REGLAS DE NEGOCIO OFICIALES]

---

**Documento Creado:** [FECHA]
**Autor:** DOCUMENT-Agent
**Basado en trabajo de:** DOMAIN-Agent
**Última Actualización:** [FECHA]

<!-- 
INSTRUCCIONES PARA AGENTES:

1. DOMAIN-Agent:
   - Implementar según esta especificación
   - Mantener lenguaje ubicuo consistente
   - Respetar límites de agregados

2. DOCUMENT-Agent:
   - Actualizar después de cada cambio en dominio
   - Sincronizar con código implementado
   - Validar que refleja realidad

3. TEST-Agent:
   - Testear TODAS las invariantes
   - Validar TODAS las reglas de negocio
   - Cubrir todos los flujos documentados

4. QUALITY-Agent:
   - Verificar que dominio es puro (sin dependencias)
   - Validar que reglas están encapsuladas
   - Confirmar lenguaje ubicuo consistente

El dominio es el CORAZÓN del sistema
Esta documentación es su ESPECIFICACIÓN COMPLETA
-->
