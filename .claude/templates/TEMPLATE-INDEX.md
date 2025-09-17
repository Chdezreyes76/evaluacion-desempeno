---
codigo: INDEX-[CODIGO]
tipo: Project Index
proyecto: [NOMBRE_PROYECTO]
version: 1.0
fecha: [FECHA_ACTUAL]
autor: PLAN-Agent
actualizado_por: DOCUMENT-Agent
estado: [EN_DESARROLLO|COMPLETADO|PAUSADO]
---

# 📚 Índice de Documentación - [NOMBRE_PROYECTO] ([CODIGO])

## 📋 Información del Proyecto

**Código del Proyecto:** [CODIGO]
**Nombre:** [NOMBRE_PROYECTO]
**Tipo de Proyecto:** [FEAT|OPTM|REFR|BUGF|INTG|MIGR]
**Estado Actual:** [EN_DESARROLLO|COMPLETADO|PAUSADO]
**Fecha de Inicio:** [FECHA_INICIO]
**Fecha de Finalización:** [FECHA_FIN o "En curso"]

## 🎯 Objetivo Principal

[DESCRIBIR EN 2-3 LÍNEAS EL OBJETIVO PRINCIPAL DEL PROYECTO]

## 🤖 Flujo de Agentes

### Secuencia Planificada
[LISTAR LA SECUENCIA DE AGENTES QUE TRABAJARÁN EN EL PROYECTO]

Ejemplo:
1. PLAN-Agent (Planificación) ✅
2. DOMAIN-Agent (Dominio) ⏳
3. DTOS-Agent (DTOs)
4. PORTS-Agent (Puertos)
5. USECASES-Agent (Casos de Uso)
6. [CONTINUAR SEGÚN PROYECTO...]

### Estado Actual
**Agente Activo:** [NOMBRE_DEL_AGENTE_ACTUAL]
**Fase:** [DOMINIO|APLICACION|ADAPTADORES|TESTING]
**Progreso General:** [PORCENTAJE]%

## 📂 Estructura de Documentación

### Documentos Principales
- [Plan de Trabajo](WP-[CODIGO]-001.md) - Estado: [CREADO|PENDIENTE]
- [Contexto de Agentes](AGENT-CONTEXT-[CODIGO].md) - Estado: [ACTIVO|CERRADO]

### Documentación Técnica
- [Especificación del Dominio](technical/TSD-[CODIGO]-001-domain.md) - [CREADO|PENDIENTE]
- [Arquitectura del Sistema](technical/TSD-[CODIGO]-002-architecture.md) - [CREADO|PENDIENTE]
- [Base de Datos](technical/TSD-[CODIGO]-003-database.md) - [CREADO|PENDIENTE]

### Documentación de API
- [Especificación de Endpoints](api/API-[CODIGO]-001.md) - [CREADO|PENDIENTE]
- [OpenAPI Spec](api/openapi-[CODIGO].yaml) - [CREADO|PENDIENTE]

### Testing
- [Plan de Pruebas](tests/TST-[CODIGO]-001.md) - [CREADO|PENDIENTE]
- [Resultados de Testing](tests/TST-[CODIGO]-002-results.md) - [CREADO|PENDIENTE]

### Decisiones de Arquitectura
- [ADR-001: [TÍTULO]](adrs/ADR-[CODIGO]-001.md) - [CREADO|PENDIENTE]

### Migraciones
- [Plan de Migración](migrations/MIG-[CODIGO]-001.md) - [SI APLICA]

## 📊 Métricas del Proyecto

### Métricas de Desarrollo
- **Componentes Creados:** [NÚMERO]
- **Componentes Reutilizados:** [NÚMERO] ([PORCENTAJE]%)
- **Archivos Generados:** [NÚMERO]
- **Líneas de Documentación:** [NÚMERO]

### Métricas de Calidad
- **Cobertura de Tests:** [PORCENTAJE]%
- **Validaciones QUALITY-Agent:** [APROBADAS|CON_OBSERVACIONES]
- **Documentación Completa:** [SI|NO]

## 🔄 Componentes Reutilizados

[LISTAR COMPONENTES IDENTIFICADOS POR PLAN-Agent PARA REUTILIZACIÓN]

Ejemplo:
- `BaseUseCase` - Reutilizado al 100%
- `ValidationService` - Adaptado con 70% de reutilización
- `ErrorHandler` - Reutilizado al 100%

## ⚠️ Puntos de Atención

[LISTAR ASPECTOS QUE REQUIEREN ATENCIÓN ESPECIAL O DECISIONES PENDIENTES]

## 📝 Notas de Actualización

### Historial de Cambios Importantes
[REGISTRAR CAMBIOS SIGNIFICATIVOS CON FECHA]

Ejemplo:
- **[FECHA]:** Iniciado el proyecto por PLAN-Agent
- **[FECHA]:** Dominio completado por DOMAIN-Agent
- **[FECHA]:** [DESCRIPCIÓN DEL CAMBIO]

## 🔗 Enlaces Rápidos

### Documentación Relacionada
- [Metodología de Desarrollo](/docs/01-METODOLOGIA-DESARROLLO-CLAUDE.md)
- [Sistema de Codificación](/docs/02-SISTEMA-CODIFICACION-DOCS.md)
- [Proyectos Previos](/docs/03-PROYECTOS-PREVIOS.md)

### Repositorio
- [Código del Dominio](/domain/[ruta])
- [Código de Aplicación](/application/[ruta])
- [Código de Adaptadores](/adapter/[ruta])
- [Tests](/tests/[ruta])

## ✅ Checklist de Finalización

### Documentación
- [ ] Todos los documentos técnicos creados
- [ ] AGENT-CONTEXT actualizado y cerrado
- [ ] Métricas finales registradas
- [ ] Lecciones aprendidas documentadas

### Código
- [ ] Dominio implementado
- [ ] Aplicación completa
- [ ] Adaptadores funcionando
- [ ] Tests con >80% cobertura

### Calidad
- [ ] QUALITY-Agent aprobación final
- [ ] TEST-Agent validación completa
- [ ] Sin issues críticos pendientes
- [ ] Documentación revisada

---

**Última Actualización:** [FECHA_Y_HORA]
**Actualizado por:** [NOMBRE_AGENTE]
**Próxima Revisión:** [FECHA_PROGRAMADA]

<!-- 
INSTRUCCIONES PARA AGENTES:
1. PLAN-Agent: Crear este archivo al inicio del proyecto
2. Actualizar estado después de cada fase completada
3. DOCUMENT-Agent: Mantener enlaces actualizados
4. Todos los agentes: Actualizar métricas al finalizar su trabajo
5. No incluir código en este documento, solo referencias
-->
