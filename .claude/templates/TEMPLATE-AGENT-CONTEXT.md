---
codigo: AGENT-CONTEXT-[CODIGO]
tipo: Agent Context
proyecto: [NOMBRE_PROYECTO]
version: 1.0
fecha_inicio: [FECHA_HORA_INICIO]
fecha_actualizacion: [FECHA_HORA_ULTIMA_ACTUALIZACION]
autor: PLAN-Agent
ultimo_agente: [NOMBRE_ULTIMO_AGENTE]
siguiente_agente: [NOMBRE_SIGUIENTE_AGENTE]
estado: [ACTIVO|COMPLETADO|ERROR|PAUSADO]
fase_actual: [PLANIFICACION|DOMINIO|APLICACION|ADAPTADORES|TESTING|FINALIZACION]
---

# 📓 AGENT-CONTEXT - [NOMBRE_PROYECTO] ([CODIGO])

## 🎯 INFORMACIÓN DEL PROYECTO

### Identificación
**Código:** [CODIGO]
**Nombre:** [NOMBRE_PROYECTO]
**Tipo:** [FEAT|OPTM|REFR|BUGF|INTG|MIGR]
**Prioridad:** [ALTA|MEDIA|BAJA]

### Descripción del Objetivo
[DESCRIPCIÓN CLARA DEL OBJETIVO PRINCIPAL DEL PROYECTO EN 3-5 LÍNEAS]

### Alcance
**INCLUYE:**
- [LISTAR QUÉ SÍ SE HARÁ]
- [PUNTO 2]
- [PUNTO 3]

**NO INCLUYE:**
- [LISTAR QUÉ NO SE HARÁ]
- [PUNTO 2]

## ♻️ ANÁLISIS DE REUTILIZACIÓN

### Componentes Identificados para Reutilizar
[ANÁLISIS REALIZADO POR PLAN-Agent]

| Componente | Ubicación | % Reutilización | Adaptaciones Necesarias |
|------------|-----------|-----------------|-------------------------|
| [NOMBRE] | [RUTA] | [PORCENTAJE]% | [DESCRIPCIÓN] |
| [NOMBRE] | [RUTA] | [PORCENTAJE]% | [DESCRIPCIÓN] |

### Decisión de Reutilización
**Total Estimado de Reutilización:** [PORCENTAJE]%
**Estrategia:** [CREAR_NUEVO|REUTILIZAR_ADAPTANDO|HÍBRIDO]

## 🤖 FLUJO DE AGENTES PLANIFICADO

### Secuencia de Ejecución
```
[DIAGRAMA SIMPLE DE FLUJO]
PLAN → DOMAIN → DTOS → PORTS → USECASES → MODELS → ALEMBIC → MAPPERS → REPOSITORIES → ROUTES → TEST → QUALITY
```

### Estado de Ejecución
| Agente | Estado | Inicio | Fin | Observaciones |
|--------|--------|--------|-----|---------------|
| PLAN-Agent | ✅ COMPLETADO | [FECHA_HORA] | [FECHA_HORA] | [NOTAS] |
| DOMAIN-Agent | ⏳ EN PROCESO | [FECHA_HORA] | - | [NOTAS] |
| DTOS-Agent | ⏸️ PENDIENTE | - | - | [NOTAS] |
| [CONTINUAR...] | | | | |

## 📝 BITÁCORA DE EJECUCIÓN

### 🤖 PLAN-Agent
**Timestamp:** [FECHA_HORA]
**Estado:** COMPLETADO ✅

#### Acciones Realizadas
- Generado código único: [CODIGO]
- Clasificado como proyecto tipo: [TIPO]
- Identificados [N] componentes reutilizables
- Creada estructura de documentación
- Delegado INDEX y WP a DOCUMENT-Agent

#### Instrucciones para Siguiente Agente
[INSTRUCCIONES ESPECÍFICAS PARA DOMAIN-Agent]

#### Archivos Creados
- `/docs/projects/[CODIGO]/` - Estructura del proyecto
- `AGENT-CONTEXT-[CODIGO].md` - Este archivo

---

### 🤖 DOMAIN-Agent
**Timestamp:** [FECHA_HORA]
**Estado:** [EN_PROCESO|COMPLETADO|ERROR]

#### Acciones Realizadas
[LISTAR ACCIONES COMPLETADAS]
- [ACCIÓN 1]
- [ACCIÓN 2]

#### Componentes Creados
[LISTAR COMPONENTES DEL DOMINIO]
- Entidad: [NOMBRE] - [DESCRIPCIÓN]
- Value Object: [NOMBRE] - [DESCRIPCIÓN]
- Servicio: [NOMBRE] - [DESCRIPCIÓN]

#### Decisiones Técnicas
[DOCUMENTAR DECISIONES IMPORTANTES]
- [DECISIÓN 1]: [JUSTIFICACIÓN]
- [DECISIÓN 2]: [JUSTIFICACIÓN]

#### Instrucciones para Siguiente Agente
[INSTRUCCIONES ESPECÍFICAS PARA DTOS-Agent]

#### Archivos Creados/Modificados
- `/domain/[ruta]/[archivo]` - [DESCRIPCIÓN]
- `/domain/[ruta]/[archivo]` - [DESCRIPCIÓN]

---

### 🤖 [SIGUIENTE_AGENTE]
**Timestamp:** [FECHA_HORA]
**Estado:** [PENDIENTE|EN_PROCESO|COMPLETADO|ERROR]

#### Acciones Realizadas
[PLANTILLA VACÍA PARA SIGUIENTE AGENTE]

#### Componentes Creados
[PLANTILLA VACÍA]

#### Decisiones Técnicas
[PLANTILLA VACÍA]

#### Instrucciones para Siguiente Agente
[PLANTILLA VACÍA]

#### Archivos Creados/Modificados
[PLANTILLA VACÍA]

---

[CONTINUAR CON PLANTILLAS PARA CADA AGENTE...]

## 🚨 GESTIÓN DE ERRORES Y RECONDUCCIÓN

### Registro de Errores
| Fecha | Agente | Error | Acción Tomada | Resuelto |
|-------|--------|-------|---------------|----------|
| [FECHA] | [AGENTE] | [DESCRIPCIÓN] | [ACCIÓN] | [SI/NO] |

### Reconducciones del Flujo
[DOCUMENTAR SI PLAN-Agent TUVO QUE RECONDUCIR EL FLUJO]

## 📊 MÉTRICAS ACUMULADAS

### Métricas de Desarrollo
- **Archivos Creados:** [NÚMERO]
- **Líneas de Código:** [NÚMERO]
- **Componentes Nuevos:** [NÚMERO]
- **Componentes Reutilizados:** [NÚMERO]

### Métricas de Calidad
- **Cobertura de Tests:** [PORCENTAJE]%
- **Complejidad Ciclomática Promedio:** [NÚMERO]
- **Deuda Técnica:** [BAJA|MEDIA|ALTA]
- **Validaciones QUALITY:** [APROBADAS|CON_OBSERVACIONES]

### Métricas de Tiempo
- **Tiempo Total:** [HORAS/DÍAS]
- **Tiempo por Fase:**
  - Dominio: [TIEMPO]
  - Aplicación: [TIEMPO]
  - Adaptadores: [TIEMPO]
  - Testing: [TIEMPO]

## 🔄 PUNTOS DE SINCRONIZACIÓN

### Validaciones Requeridas
[PUNTOS DONDE SE REQUIERE VALIDACIÓN MANUAL O AUTOMÁTICA]

- [ ] Dominio completo antes de continuar con DTOs
- [ ] DTOs, Ports y UseCases completos antes de Adaptadores
- [ ] Models y Alembic sincronizados antes de Repositories
- [ ] Todo implementado antes de Testing

### Dependencias Críticas
[IDENTIFICAR DEPENDENCIAS ENTRE COMPONENTES]

## 💡 DECISIONES Y APRENDIZAJES

### Decisiones Arquitectónicas
[DECISIONES IMPORTANTES TOMADAS DURANTE EL DESARROLLO]

1. **[TÍTULO DECISIÓN]**
   - Contexto: [CONTEXTO]
   - Decisión: [DECISIÓN]
   - Justificación: [JUSTIFICACIÓN]

### Problemas Encontrados y Soluciones
[DOCUMENTAR PROBLEMAS Y CÓMO SE RESOLVIERON]

### Lecciones Aprendidas
[CONOCIMIENTO ÚTIL PARA FUTUROS PROYECTOS]

## ✅ FINALIZACIÓN DEL PROYECTO

### Checklist de Cierre
- [ ] Todos los agentes completaron su trabajo
- [ ] TEST-Agent confirmó >80% cobertura
- [ ] QUALITY-Agent aprobación final
- [ ] Documentación completa y actualizada
- [ ] Métricas finales registradas

### Resumen de Entregables
[LISTAR TODOS LOS ENTREGABLES FINALES]

### Puntos de Atención para Usuario
[ASPECTOS QUE EL USUARIO DEBE REVISAR O VALIDAR]

1. [PUNTO 1]
2. [PUNTO 2]
3. [PUNTO 3]

### Recomendaciones de Mejora
[SUGERENCIAS PARA OPTIMIZACIONES FUTURAS]

## 📌 NOTAS IMPORTANTES

### Para el Siguiente Agente
[INFORMACIÓN CRÍTICA QUE DEBE CONOCER EL SIGUIENTE AGENTE]

### Restricciones y Limitaciones
[LIMITACIONES TÉCNICAS O DE NEGOCIO IDENTIFICADAS]

### Referencias Útiles
- [DOCUMENTO O RECURSO RELEVANTE]
- [LINK A DOCUMENTACIÓN]
- [REFERENCIA TÉCNICA]

---

**Última Actualización:** [FECHA_HORA]
**Actualizado por:** [NOMBRE_AGENTE]
**Siguiente Acción:** [DESCRIPCIÓN DE LA SIGUIENTE ACCIÓN]

<!-- 
INSTRUCCIONES PARA AGENTES:

1. CADA AGENTE DEBE:
   - Actualizar su sección al iniciar trabajo
   - Documentar decisiones importantes
   - Registrar componentes creados
   - Dejar instrucciones claras para el siguiente
   - Actualizar métricas

2. PLAN-Agent:
   - Crear este archivo al inicio
   - Monitorear progreso
   - Reconducir si hay errores

3. DOCUMENT-Agent:
   - NO modifica este archivo
   - Lee información para actualizar documentación técnica

4. QUALITY-Agent:
   - Valida completitud de cada sección
   - Registra observaciones en su sección

5. TEST-Agent:
   - Actualiza métricas de testing
   - Documenta cobertura final

ESTE ES EL DOCUMENTO MÁS IMPORTANTE DEL PROYECTO
Mantenerlo actualizado es CRÍTICO para el éxito
-->
