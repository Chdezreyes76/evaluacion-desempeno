---
codigo: WP-[CODIGO]-001
tipo: Work Plan BUGF
proyecto: [NOMBRE_PROYECTO]
version: 1.0
fecha: [FECHA_ACTUAL]
autor: PLAN-Agent
tipo_proyecto: BUGF
prioridad: [CRÍTICA|ALTA|MEDIA|BAJA]
severidad: [BLOQUEANTE|MAYOR|MENOR|COSMÉTICO]
---

# 📋 Plan de Trabajo - Bug Fix

## 🐛 IDENTIFICACIÓN DEL BUG

### Información Básica
**ID del Bug:** [IDENTIFICADOR]
**Reportado por:** [USUARIO/SISTEMA]
**Fecha de Reporte:** [FECHA]
**Severidad:** [BLOQUEANTE|MAYOR|MENOR|COSMÉTICO]
**Prioridad:** [CRÍTICA|ALTA|MEDIA|BAJA]
**Componente Afectado:** [COMPONENTE]
**Frecuencia:** [SIEMPRE|FRECUENTE|OCASIONAL|RARO]

### Descripción del Problema
[DESCRIPCIÓN CLARA Y CONCISA DEL BUG]

### Comportamiento Esperado
[QUÉ DEBERÍA HACER EL SISTEMA]

### Comportamiento Actual
[QUÉ ESTÁ HACIENDO EL SISTEMA INCORRECTAMENTE]

## 🎯 IMPACTO Y URGENCIA

### Usuarios Afectados
- **Número de Usuarios:** [CANTIDAD O PORCENTAJE]
- **Tipo de Usuarios:** [INTERNOS|EXTERNOS|TODOS]
- **Procesos Bloqueados:** [LISTA DE PROCESOS]

### Impacto en el Negocio
| Aspecto | Impacto | Descripción |
|---------|---------|-------------|
| Operación | [ALTO|MEDIO|BAJO] | [CÓMO AFECTA] |
| Datos | [ALTO|MEDIO|BAJO] | [RIESGO DE DATOS] |
| Usuarios | [ALTO|MEDIO|BAJO] | [EXPERIENCIA] |
| Seguridad | [ALTO|MEDIO|BAJO] | [SI APLICA] |

### Workaround Disponible
**¿Existe solución temporal?** [SI|NO]
[DESCRIBIR WORKAROUND SI EXISTE]

## 🔍 ANÁLISIS DE CAUSA RAÍZ

### Pasos para Reproducir
1. [PASO 1]
2. [PASO 2]
3. [PASO 3]
4. [RESULTADO: ERROR OBSERVADO]

### Condiciones de Reproducción
- **Ambiente:** [DESARROLLO|STAGING|PRODUCCIÓN]
- **Datos Específicos:** [DESCRIPCIÓN DE DATOS NECESARIOS]
- **Configuración:** [CONFIGURACIÓN ESPECÍFICA]
- **Frecuencia de Reproducción:** [100%|INTERMITENTE]

### Causa Raíz Identificada
**Componente:** [CLASE/MÉTODO/FUNCIÓN]
**Ubicación:** [RUTA DEL ARCHIVO]
**Tipo de Error:** [LÓGICO|SINTAXIS|CONFIGURACIÓN|DATOS|INTEGRACIÓN]

**Descripción de la Causa:**
[EXPLICACIÓN TÉCNICA DE POR QUÉ OCURRE EL BUG]

### Análisis de Regresión
**¿Es una regresión?** [SI|NO]
**Introducido en:** [VERSIÓN/COMMIT/FECHA]
**Cambio que lo causó:** [DESCRIPCIÓN SI APLICA]

## 🔧 SOLUCIÓN PROPUESTA

### Estrategia de Corrección
[DESCRIPCIÓN DE CÓMO SE VA A CORREGIR EL BUG]

### Componentes a Modificar
| Componente | Archivo | Tipo de Cambio | Agente Responsable |
|------------|---------|----------------|-------------------|
| [NOMBRE] | [RUTA] | [CORRECCIÓN|AJUSTE] | [AGENTE] |
| [NOMBRE] | [RUTA] | [CORRECCIÓN|AJUSTE] | [AGENTE] |

### Cambios Específicos
1. **[CAMBIO 1]**
   - Ubicación: [DÓNDE]
   - Antes: [CÓDIGO/LÓGICA ACTUAL]
   - Después: [CÓDIGO/LÓGICA CORREGIDA]
   - Justificación: [POR QUÉ ESTO CORRIGE EL BUG]

2. **[CAMBIO 2]**
   - Ubicación: [DÓNDE]
   - Antes: [CÓDIGO/LÓGICA ACTUAL]
   - Después: [CÓDIGO/LÓGICA CORREGIDA]
   - Justificación: [POR QUÉ ESTO CORRIGE EL BUG]

## 📋 FASES DE IMPLEMENTACIÓN

### FASE 1: Reproducción y Confirmación
**Responsable:** PLAN-Agent + TEST-Agent

**Actividades:**
- [ ] Reproducir el bug en ambiente controlado
- [ ] Confirmar causa raíz
- [ ] Documentar caso de prueba que falla
- [ ] Validar alcance del problema

**Entregables:**
- Test que reproduce el bug
- Confirmación de causa raíz

### FASE 2: Implementación del Fix
**Responsable:** [AGENTE SEGÚN CAPA AFECTADA]

**Actividades:**
- [ ] Implementar corrección
- [ ] Verificar que el test ahora pasa
- [ ] Asegurar no introducir nuevos problemas
- [ ] Documentar el cambio

**Entregables:**
- Código corregido
- Test pasando

### FASE 3: Testing de Regresión
**Responsable:** TEST-Agent

**Actividades:**
- [ ] Ejecutar suite completa de tests
- [ ] Verificar casos relacionados
- [ ] Probar casos extremos
- [ ] Validar en diferentes escenarios

**Entregables:**
- Confirmación de no regresiones
- Validación del fix

### FASE 4: Validación Final
**Responsable:** QUALITY-Agent

**Actividades:**
- [ ] Revisar calidad del fix
- [ ] Verificar documentación
- [ ] Aprobar para despliegue
- [ ] Actualizar registro de bugs

**Entregables:**
- Aprobación de calidad
- Bug cerrado

## 🧪 PLAN DE TESTING

### Test Específico del Bug
```
Nombre del Test: test_[descripción_del_bug]
Objetivo: Verificar que [comportamiento_esperado]
Entrada: [datos_de_entrada]
Salida Esperada: [resultado_correcto]
```

### Tests de Regresión Relacionados
| Test | Área | Prioridad | Debe Pasar |
|------|------|-----------|------------|
| [NOMBRE TEST] | [ÁREA] | [ALTA|MEDIA] | [ ] |
| [NOMBRE TEST] | [ÁREA] | [ALTA|MEDIA] | [ ] |

### Escenarios de Validación
1. **Caso Original:** [VERIFICAR QUE EL BUG ESTÁ CORREGIDO]
2. **Casos Límite:** [PROBAR VALORES EXTREMOS]
3. **Casos Relacionados:** [FUNCIONALIDAD CERCANA]

## ⚠️ RIESGOS Y CONSIDERACIONES

### Riesgos del Fix
| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| [NUEVA REGRESIÓN] | [ALTA|MEDIA|BAJA] | [ALTO|MEDIO|BAJO] | [ESTRATEGIA] |
| [EFECTO LATERAL] | [ALTA|MEDIA|BAJA] | [ALTO|MEDIO|BAJO] | [ESTRATEGIA] |

### Áreas de Atención Especial
- [COMPONENTE/FUNCIONALIDAD QUE REQUIERE CUIDADO]
- [POSIBLES EFECTOS LATERALES]

## ✅ CRITERIOS DE ACEPTACIÓN

### Criterios de Éxito
- [ ] Bug no reproducible después del fix
- [ ] Test específico del bug pasando
- [ ] Sin regresiones introducidas
- [ ] Todos los tests existentes pasando
- [ ] Documentación actualizada

### Validación en Producción
- [ ] Verificación en ambiente similar a producción
- [ ] Monitoreo post-despliegue planificado
- [ ] Plan de rollback preparado

## 📊 PREVENCIÓN FUTURA

### Lección Aprendida
[QUÉ SE APRENDIÓ DE ESTE BUG]

### Acciones Preventivas
1. [ACCIÓN PARA EVITAR BUGS SIMILARES]
2. [MEJORA EN PROCESO/CÓDIGO]
3. [NUEVA VALIDACIÓN/TEST]

### Mejoras Sugeridas
- [MEJORA EN ARQUITECTURA]
- [MEJORA EN VALIDACIONES]
- [MEJORA EN TESTING]

## 🔄 INFORMACIÓN DE SEGUIMIENTO

### Estado del Bug
- **Estado Actual:** [NUEVO|EN_PROGRESO|RESUELTO|CERRADO]
- **Última Actualización:** [FECHA]
- **Responsable Actual:** [AGENTE]

### Historial de Cambios
| Fecha | Acción | Responsable | Notas |
|-------|--------|-------------|-------|
| [FECHA] | Bug reportado | [QUIEN] | [NOTAS] |
| [FECHA] | Análisis iniciado | PLAN-Agent | [NOTAS] |

## 📝 NOTAS ADICIONALES

### Información Relevante
[CUALQUIER INFORMACIÓN ADICIONAL IMPORTANTE]

### Referencias
- [LINK A ISSUE TRACKER]
- [DOCUMENTACIÓN RELACIONADA]
- [BUGS SIMILARES ANTERIORES]

---

**Documento Creado:** [FECHA]
**Autor:** PLAN-Agent
**Estado:** [ABIERTO|EN_PROGRESO|RESUELTO|CERRADO]

<!-- 
INSTRUCCIONES PARA AGENTES:

1. PLAN-Agent: 
   - Confirmar reproducción del bug
   - Identificar agente responsable según capa
   - Coordinar fix rápido y seguro

2. Agente Implementador:
   - Corregir SOLO el bug reportado
   - No hacer cambios adicionales
   - Mantener cambios mínimos

3. TEST-Agent:
   - Crear test que reproduce el bug
   - Verificar fix corrige el problema
   - Ejecutar regresión completa

4. QUALITY-Agent:
   - Validar que fix es correcto
   - Verificar no hay efectos laterales
   - Aprobar para despliegue

PRINCIPIO: Cambio mínimo que corrige el problema
-->
