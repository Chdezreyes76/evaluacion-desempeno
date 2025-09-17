---
codigo: ADR-[CODIGO]-[SEQ]
tipo: Architecture Decision Record
proyecto: [NOMBRE_PROYECTO]
version: 1.0
fecha: [FECHA_ACTUAL]
autor: [AUTOR/EQUIPO]
estado: [PROPUESTO|EN_DISCUSION|ACEPTADO|RECHAZADO|DEPRECADO|REEMPLAZADO]
reemplaza: [ADR-CODIGO-XXX si aplica]
reemplazado_por: [ADR-CODIGO-XXX si aplica]
relacionados: [TSD-CODIGO-003-architecture, WP-CODIGO]
---

# ADR-[SEQ]: [TÍTULO CORTO Y DESCRIPTIVO]

## 📋 METADATOS

**ID:** ADR-[CODIGO]-[SEQ]
**Fecha:** [FECHA_DECISION]
**Estado:** [PROPUESTO|EN_DISCUSION|ACEPTADO|RECHAZADO|DEPRECADO|REEMPLAZADO]
**Decisores:** [PERSONAS/EQUIPOS INVOLUCRADOS]
**Categoría:** [ARQUITECTURA|TECNOLOGIA|PROCESO|SEGURIDAD|DATOS|INTEGRACION]
**Impacto:** [ALTO|MEDIO|BAJO]
**Reversibilidad:** [FACIL|MODERADA|DIFICIL|IRREVERSIBLE]

## 🎯 CONTEXTO Y PROBLEMA

### Contexto
[DESCRIPCIÓN DEL CONTEXTO EN EL QUE SURGE LA NECESIDAD DE TOMAR ESTA DECISIÓN]

### Declaración del Problema
[FORMULACIÓN CLARA Y CONCISA DEL PROBLEMA A RESOLVER]

### Drivers de la Decisión
- **Driver 1:** [REQUISITO O RESTRICCIÓN QUE IMPULSA LA DECISIÓN]
- **Driver 2:** [OTRO FACTOR IMPORTANTE]
- **Driver 3:** [CONSIDERACIÓN ADICIONAL]

### Stakeholders Afectados
| Stakeholder | Rol | Interés Principal | Nivel de Impacto |
|-------------|-----|-------------------|------------------|
| [NOMBRE/GRUPO] | [ROL] | [QUÉ LE IMPORTA] | [ALTO|MEDIO|BAJO] |
| [NOMBRE/GRUPO] | [ROL] | [QUÉ LE IMPORTA] | [ALTO|MEDIO|BAJO] |

## 🤔 OPCIONES CONSIDERADAS

### Opción 1: [NOMBRE DESCRIPTIVO]
**Descripción:** [BREVE DESCRIPCIÓN DE LA OPCIÓN]

**Pros:**
- ✅ [VENTAJA 1]
- ✅ [VENTAJA 2]
- ✅ [VENTAJA 3]

**Contras:**
- ❌ [DESVENTAJA 1]
- ❌ [DESVENTAJA 2]
- ❌ [DESVENTAJA 3]

**Costo Estimado:** [TIEMPO/RECURSOS/DINERO]
**Riesgo:** [ALTO|MEDIO|BAJO]
**Complejidad:** [ALTA|MEDIA|BAJA]

### Opción 2: [NOMBRE DESCRIPTIVO]
**Descripción:** [BREVE DESCRIPCIÓN DE LA OPCIÓN]

**Pros:**
- ✅ [VENTAJA 1]
- ✅ [VENTAJA 2]
- ✅ [VENTAJA 3]

**Contras:**
- ❌ [DESVENTAJA 1]
- ❌ [DESVENTAJA 2]
- ❌ [DESVENTAJA 3]

**Costo Estimado:** [TIEMPO/RECURSOS/DINERO]
**Riesgo:** [ALTO|MEDIO|BAJO]
**Complejidad:** [ALTA|MEDIA|BAJA]

### Opción 3: [NOMBRE DESCRIPTIVO]
[REPETIR ESTRUCTURA PARA CADA OPCIÓN]

### Opción 4: No Hacer Nada (Status Quo)
**Descripción:** Mantener la situación actual sin cambios

**Pros:**
- ✅ Sin costo de implementación
- ✅ Sin riesgo de cambio
- ✅ [OTRA VENTAJA SI APLICA]

**Contras:**
- ❌ [PROBLEMA PERSISTE]
- ❌ [DEUDA TÉCNICA ACUMULA]
- ❌ [OTRA DESVENTAJA]

## 📊 CRITERIOS DE EVALUACIÓN

### Criterios y Pesos
| Criterio | Peso | Descripción |
|----------|------|-------------|
| Performance | [1-5] | [QUÉ SE EVALÚA] |
| Costo | [1-5] | [INICIAL Y OPERATIVO] |
| Complejidad | [1-5] | [TÉCNICA Y OPERATIVA] |
| Mantenibilidad | [1-5] | [FACILIDAD DE MANTENER] |
| Escalabilidad | [1-5] | [CAPACIDAD DE CRECER] |
| Seguridad | [1-5] | [ASPECTOS DE SEGURIDAD] |
| Time to Market | [1-5] | [VELOCIDAD DE IMPLEMENTACIÓN] |

### Matriz de Evaluación
| Opción | Performance | Costo | Complejidad | Mantenibilidad | Escalabilidad | Seguridad | TTM | **Total** |
|--------|------------|-------|-------------|----------------|---------------|-----------|-----|-----------|
| Opción 1 | [1-10] | [1-10] | [1-10] | [1-10] | [1-10] | [1-10] | [1-10] | **[SUMA]** |
| Opción 2 | [1-10] | [1-10] | [1-10] | [1-10] | [1-10] | [1-10] | [1-10] | **[SUMA]** |
| Opción 3 | [1-10] | [1-10] | [1-10] | [1-10] | [1-10] | [1-10] | [1-10] | **[SUMA]** |

*Escala: 1 = Muy Malo, 5 = Neutro, 10 = Excelente*

## ✅ DECISIÓN

### Opción Seleccionada
**Decisión:** Se elige la **Opción [N]: [NOMBRE]**

### Justificación
[EXPLICACIÓN DETALLADA DE POR QUÉ SE ELIGIÓ ESTA OPCIÓN]

### Argumentos Clave
1. **[ARGUMENTO 1]:** [EXPLICACIÓN]
2. **[ARGUMENTO 2]:** [EXPLICACIÓN]
3. **[ARGUMENTO 3]:** [EXPLICACIÓN]

### Trade-offs Aceptados
- **Ganamos:** [QUÉ BENEFICIOS OBTENEMOS]
- **Perdemos:** [QUÉ SACRIFICAMOS]
- **Aceptamos:** [QUÉ COMPROMISOS ASUMIMOS]

## 📈 CONSECUENCIAS

### Consecuencias Positivas
- ✅ **Inmediatas:** [BENEFICIOS A CORTO PLAZO]
- ✅ **A Mediano Plazo:** [BENEFICIOS EN 3-6 MESES]
- ✅ **A Largo Plazo:** [BENEFICIOS ESTRATÉGICOS]

### Consecuencias Negativas
- ⚠️ **Inmediatas:** [IMPACTOS NEGATIVOS INICIALES]
- ⚠️ **A Mediano Plazo:** [POSIBLES PROBLEMAS]
- ⚠️ **A Largo Plazo:** [RIESGOS FUTUROS]

### Consecuencias Neutras
- ℹ️ [CAMBIOS QUE NO SON NI POSITIVOS NI NEGATIVOS]
- ℹ️ [ASPECTOS QUE SIMPLEMENTE CAMBIAN]

## 🎬 PLAN DE IMPLEMENTACIÓN

### Fases de Implementación
| Fase | Descripción | Responsable | Duración Estimada | Dependencias |
|------|-------------|-------------|-------------------|--------------|
| Fase 1 | [QUÉ SE HACE] | [QUIÉN] | [TIEMPO] | [DEPS] |
| Fase 2 | [QUÉ SE HACE] | [QUIÉN] | [TIEMPO] | [DEPS] |
| Fase 3 | [QUÉ SE HACE] | [QUIÉN] | [TIEMPO] | [DEPS] |

### Acciones Inmediatas
- [ ] [ACCIÓN 1 - PRIMERA SEMANA]
- [ ] [ACCIÓN 2 - PRIMERA SEMANA]
- [ ] [ACCIÓN 3 - PRIMER MES]

### Migraciones Necesarias
| Componente | Estado Actual | Estado Objetivo | Estrategia | Rollback |
|------------|---------------|-----------------|------------|----------|
| [COMPONENTE] | [ACTUAL] | [OBJETIVO] | [CÓMO] | [PLAN B] |

## ⚠️ RIESGOS Y MITIGACIONES

### Análisis de Riesgos
| Riesgo | Probabilidad | Impacto | Severidad | Mitigación | Plan de Contingencia |
|--------|--------------|---------|-----------|------------|---------------------|
| [RIESGO 1] | [A/M/B] | [A/M/B] | [A/M/B] | [ESTRATEGIA] | [PLAN B] |
| [RIESGO 2] | [A/M/B] | [A/M/B] | [A/M/B] | [ESTRATEGIA] | [PLAN B] |

### Señales de Alerta Temprana
- 🚨 **Señal 1:** [QUÉ OBSERVAR QUE INDIQUE PROBLEMAS]
- 🚨 **Señal 2:** [OTRO INDICADOR DE PROBLEMAS]
- 🚨 **Señal 3:** [MÉTRICA O EVENTO A MONITOREAR]

### Criterios de Reversión
**La decisión debe revertirse si:**
- [ ] [CONDICIÓN 1 QUE REQUIERE REVERTIR]
- [ ] [CONDICIÓN 2 QUE REQUIERE REVERTIR]
- [ ] [CONDICIÓN 3 QUE REQUIERE REVERTIR]

## 📏 MÉTRICAS DE ÉXITO

### KPIs a Monitorear
| Métrica | Valor Actual | Valor Objetivo | Plazo | Método de Medición |
|---------|--------------|----------------|-------|-------------------|
| [MÉTRICA 1] | [ACTUAL] | [OBJETIVO] | [CUÁNDO] | [CÓMO] |
| [MÉTRICA 2] | [ACTUAL] | [OBJETIVO] | [CUÁNDO] | [CÓMO] |

### Criterios de Éxito
- [ ] [CRITERIO MEDIBLE 1]
- [ ] [CRITERIO MEDIBLE 2]
- [ ] [CRITERIO MEDIBLE 3]

### Periodo de Evaluación
**Revisión en:** [3 MESES | 6 MESES | 1 AÑO]
**Responsable de Evaluación:** [QUIÉN]

## 🔄 ACTUALIZACIONES Y REVISIONES

### Historial de Cambios
| Fecha | Versión | Cambio | Autor | Razón |
|-------|---------|--------|-------|-------|
| [FECHA] | 1.0 | Creación inicial | [AUTOR] | - |
| [FECHA] | 1.1 | [CAMBIO] | [AUTOR] | [RAZÓN] |

### Trigger para Revisión
**Este ADR debe revisarse cuando:**
- [ ] Han pasado [N] meses desde la implementación
- [ ] Cambian los requisitos de [ÁREA]
- [ ] Se detectan problemas de [TIPO]
- [ ] Surge nueva tecnología relevante

### Lecciones Aprendidas
[ESPACIO PARA DOCUMENTAR APRENDIZAJES POST-IMPLEMENTACIÓN]

## 📚 REFERENCIAS

### Documentación Interna
- [Architecture Document](TSD-[CODIGO]-003-architecture.md)
- [Work Plan](WP-[CODIGO]-001.md)
- [Otros ADRs relacionados](ADR-[CODIGO]-XXX.md)

### Referencias Externas
- [Documentación de tecnología]
- [Artículos o papers relevantes]
- [Casos de estudio similares]
- [Best practices de la industria]

### Investigación y POCs
- [Proof of Concept realizado]
- [Benchmarks ejecutados]
- [Análisis comparativo]

## 💡 NOTAS ADICIONALES

### Consideraciones Especiales
[ASPECTOS IMPORTANTES NO CUBIERTOS EN SECCIONES ANTERIORES]

### Supuestos
- [SUPUESTO 1 BAJO EL CUAL SE TOMA LA DECISIÓN]
- [SUPUESTO 2 QUE DEBE CUMPLIRSE]
- [SUPUESTO 3 ASUMIDO]

### Restricciones
- [RESTRICCIÓN 1 QUE LIMITA LAS OPCIONES]
- [RESTRICCIÓN 2 QUE DEBE RESPETARSE]

### Dependencias
- [DEPENDENCIA 1 DE OTROS SISTEMAS/DECISIONES]
- [DEPENDENCIA 2 QUE DEBE ESTAR LISTA]

---

**Estado Actual:** [PROPUESTO|EN_DISCUSION|ACEPTADO|RECHAZADO|DEPRECADO|REEMPLAZADO]
**Fecha de Decisión:** [FECHA]
**Fecha de Implementación:** [FECHA]
**Última Revisión:** [FECHA]

<!-- 
INSTRUCCIONES PARA AGENTES Y EQUIPOS:

1. PLAN-Agent:
   - Identificar necesidad de ADR para decisiones importantes
   - Coordinar discusión y aprobación
   - Asegurar implementación según lo decidido

2. QUALITY-Agent:
   - Validar que implementación sigue el ADR
   - Detectar desviaciones de la decisión
   - Proponer revisión si es necesario

3. Todos los Agentes:
   - Consultar ADRs antes de tomar decisiones relacionadas
   - Seguir las decisiones documentadas
   - Proponer nuevos ADRs cuando sea necesario

4. Proceso de ADR:
   - PROPUESTO: En discusión
   - EN_DISCUSION: Recopilando feedback
   - ACEPTADO: Decisión tomada
   - RECHAZADO: Opción descartada
   - DEPRECADO: Ya no aplica
   - REEMPLAZADO: Sustituido por nuevo ADR

Los ADRs son DECISIONES IMPORTANTES documentadas
Evitan re-discutir las mismas decisiones
Proporcionan contexto histórico valioso
-->
