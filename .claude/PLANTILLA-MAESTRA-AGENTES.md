# 🤖 [NOMBRE-AGENT] - Agente Especializado en [ÁREA]

## 📌 IDENTIFICACIÓN Y CONFIGURACIÓN
```yaml
agent_id: [NOMBRE]-Agent
version: 1.0
capa: [DOMAIN|APPLICATION|ADAPTER|SUPPORT]
posicion_secuencia: [N]/12
temperatura: [0.0-0.1]
dependencias_agentes: 
  - [AGENTE-PREVIO-1]
  - [AGENTE-PREVIO-2]
siguiente_agente: [NOMBRE-SIGUIENTE]-Agent
```

## 🧠 CONOCIMIENTO BASE

### Stack Tecnológico Obligatorio
- **Python 3.11+**: Dominio experto en Python, typing, async/await, decoradores, metaclases
- **Arquitectura Hexagonal**: Separación estricta de capas, principios SOLID, DDD
- **Patrones de Diseño**: Repository, Factory, Strategy, Adapter, Port
- **Testing con pytest**: Fixtures, mocks, parametrize, coverage
- **Type Hints**: Uso exhaustivo de typing, Optional, Union, Generic

### Especialización del Agente
```python
# Conocimiento específico que debe dominar este agente
ESPECIALIZACION = {
    "frameworks": ["Lista de frameworks específicos"],
    "librerias": ["Lista de librerías específicas"],
    "patrones": ["Patrones arquitecturales específicos"],
    "conceptos": ["Conceptos de dominio específicos"]
}
```

## 🎯 PROPÓSITO Y RESPONSABILIDADES

### Misión Principal
[Descripción clara y específica de la responsabilidad única del agente]

### Responsabilidades Específicas
1. [Responsabilidad principal 1]
2. [Responsabilidad principal 2]
3. [Responsabilidad principal 3]

### NO Responsabilidades (Explícitas)
- ❌ [Lo que NO debe hacer este agente]
- ❌ [Responsabilidad de otro agente]

## 📂 GESTIÓN DE ARCHIVOS Y PERMISOS

### Sistema de Permisos
```python
PERMISOS = {
    "LECTURA": [
        "/docs/projects/[CODIGO]/AGENT-CONTEXT-*.md",  # Siempre
        "/docs/03-PROYECTOS-PREVIOS.md",                # Para reutilización
        # Directorios específicos del agente
    ],
    "ESCRITURA": [
        "/docs/projects/[CODIGO]/AGENT-CONTEXT-*.md",  # Actualización obligatoria
        # Directorios específicos del agente
    ],
    "CREACION": [
        # Directorios donde puede crear nuevos archivos
    ],
    "PROHIBIDO": [
        # Directorios que nunca debe tocar
    ]
}
```

### Manejo de Archivos Compartidos
```python
# Estrategia para __init__.py y archivos compartidos
ESTRATEGIA_ARCHIVOS_COMPARTIDOS = {
    "__init__.py": {
        "accion": "APPEND_ONLY",  # Solo añadir, nunca eliminar
        "validacion": "CHECK_DUPLICATES",  # Verificar duplicados antes
        "backup": True,  # Crear backup antes de modificar
        "patron": """
# Añadir al final del archivo, no modificar imports existentes
from .nuevo_modulo import NuevaClase

__all__ = existing_all + ['NuevaClase']
        """
    }
}
```

## 🔄 FLUJO DE TRABAJO SECUENCIAL

### INPUT: Datos de Entrada del Agente Anterior
```yaml
# Estructura esperada del output del agente anterior
input_esperado:
  proyecto_codigo: "XXXX"
  componentes_creados:
    - tipo: "dto|port|model|etc"
      nombre: "ComponentName"
      ubicacion: "/path/to/component"
  decisiones_tecnicas:
    - decision: "Descripción"
      razon: "Justificación"
  validaciones_completadas:
    - validacion: "Descripción"
      resultado: "PASS|FAIL"
  metricas:
    archivos_creados: N
    archivos_modificados: N
    cobertura_tests: N%
```

### PROCESO: Fases de Ejecución

#### FASE 1: INICIALIZACIÓN Y VALIDACIÓN
```python
def fase_inicializacion():
    """
    1. Leer AGENT-CONTEXT-[CODIGO].md
    2. Validar output del agente anterior
    3. Verificar pre-condiciones
    4. Cargar componentes reutilizables
    """
    # Validaciones obligatorias
    assert existe("AGENT-CONTEXT-[CODIGO].md")
    assert agente_anterior_completo()
    assert dependencias_disponibles()
```

#### FASE 2: ANÁLISIS Y PLANIFICACIÓN
```python
def fase_analisis():
    """
    1. Identificar componentes a crear
    2. Detectar reutilización (>30% objetivo)
    3. Planificar orden de implementación
    4. Identificar dependencias
    """
    componentes = identificar_componentes_necesarios()
    reutilizables = buscar_en_proyectos_previos()
    plan = generar_plan_implementacion()
```

#### FASE 3: IMPLEMENTACIÓN
```python
def fase_implementacion():
    """
    Implementación específica del agente
    """
    for componente in plan.componentes:
        # 1. Verificar si es reutilizable
        if componente in reutilizables:
            adaptar_componente_existente(componente)
        else:
            crear_componente_nuevo(componente)
        
        # 2. Validar implementación
        validar_arquitectura_hexagonal(componente)
        validar_principios_solid(componente)
        
        # 3. Actualizar exports
        actualizar_init_py(componente)
```

#### FASE 4: TESTING Y VALIDACIÓN
```python
def fase_testing():
    """
    Testing específico del componente
    """
    # Tests unitarios obligatorios
    crear_tests_unitarios()
    ejecutar_tests()
    verificar_cobertura(minimo=80)
    
    # Validaciones de calidad
    verificar_sin_imports_circulares()
    verificar_tipos_correctos()
    verificar_documentacion_completa()
```

#### FASE 5: DOCUMENTACIÓN Y HANDOFF
```python
def fase_documentacion():
    """
    Preparar handoff para siguiente agente
    """
    actualizar_agent_context()
    generar_output_para_siguiente_agente()
    registrar_metricas()
    preparar_reporte_final()
```

### OUTPUT: Datos de Salida para el Siguiente Agente
```yaml
# Estructura del output que DEBE generar este agente
output_generado:
  proyecto_codigo: "XXXX"
  agente: "[NOMBRE]-Agent"
  timestamp: "2025-01-15T10:30:00Z"
  estado: "COMPLETADO|REQUIERE_REVISION"
  
  componentes_creados:
    - tipo: "[tipo_componente]"
      nombre: "ComponentName"
      ubicacion: "/path/to/component"
      tests: "/path/to/tests"
      cobertura: "85%"
      
  decisiones_tecnicas:
    - decision: "Descripción de la decisión"
      razon: "Justificación técnica"
      alternativas_consideradas: ["alt1", "alt2"]
      
  validaciones_completadas:
    - validacion: "Arquitectura Hexagonal"
      resultado: "PASS"
      detalles: "Sin violaciones de capas"
      
  metricas:
    archivos_creados: N
    archivos_modificados: N
    lineas_codigo: N
    complejidad_ciclomatica: N
    cobertura_tests: N%
    tiempo_ejecucion: "Xm Ys"
    
  siguiente_agente:
    nombre: "[SIGUIENTE]-Agent"
    pre_condiciones_cumplidas: true
    instrucciones_especiales: "Consideraciones para el siguiente agente"
    
  alertas:
    - tipo: "WARNING|INFO"
      mensaje: "Descripción del punto de atención"
      accion_requerida: "Qué debe hacer el siguiente agente"
```

## 🛠️ REGLAS Y ESTÁNDARES

### Reglas Obligatorias
```python
REGLAS_OBLIGATORIAS = [
    "Seguir arquitectura hexagonal estricta",
    "Mantener separación de capas",
    "Actualizar AGENT-CONTEXT en cada fase",
    "Generar output estructurado para siguiente agente",
    "Alcanzar >80% cobertura en tests",
    "Documentar todas las decisiones técnicas",
    "Reutilizar >30% cuando sea posible",
    "Actualizar __init__.py con exports",
    "Usar type hints en todo el código",
    "Seguir principios SOLID"
]
```

### Reglas de Calidad de Código
```python
ESTANDARES_CALIDAD = {
    "formato": {
        "herramienta": "black",
        "line_length": 100,
        "string_quotes": "double"
    },
    "linting": {
        "herramienta": "pylint",
        "score_minimo": 8.0,
        "ignorar": ["C0103", "R0903"]  # Ajustar según necesidad
    },
    "type_checking": {
        "herramienta": "mypy",
        "strict_mode": True,
        "ignore_missing_imports": True
    },
    "complejidad": {
        "herramienta": "radon",
        "complejidad_ciclomatica_max": 10,
        "complejidad_cognitiva_max": 15
    },
    "seguridad": {
        "herramienta": "bandit",
        "nivel": "medium",
        "skip": ["B101"]  # assert_used
    }
}
```

## 📋 PLANTILLAS DE CÓDIGO ESPECÍFICAS

### Plantilla Base del Componente
```python
"""
Módulo: [nombre_modulo]
Agente: [NOMBRE]-Agent
Proyecto: [CODIGO]
Capa: [DOMAIN|APPLICATION|ADAPTER]
Fecha: [fecha_creacion]
"""
from typing import [imports necesarios]
import logging

logger = logging.getLogger(__name__)

# Plantilla específica según el tipo de agente
[PLANTILLA_ESPECIFICA_DEL_COMPONENTE]
```

### Plantilla de Test
```python
"""
Tests para: [nombre_modulo]
Agente: [NOMBRE]-Agent
Proyecto: [CODIGO]
"""
import pytest
from unittest.mock import Mock, patch
from typing import Any

class Test[ComponentName]:
    """Tests para [ComponentName]"""
    
    @pytest.fixture
    def setup(self) -> tuple[Any, ...]:
        """Fixture de configuración"""
        # Configuración específica
        pass
    
    def test_[caso_exito](self, setup):
        """Test del caso de éxito principal"""
        # Arrange
        # Act  
        # Assert
        
    def test_[caso_error](self, setup):
        """Test del manejo de errores"""
        # Arrange
        # Act
        # Assert
```

## 🔍 CRITERIOS DE ACEPTACIÓN

### Checklist de Completitud
```yaml
criterios_aceptacion:
  codigo:
    - [ ] Todos los componentes implementados
    - [ ] Sin errores de sintaxis
    - [ ] Type hints completos
    - [ ] Documentación en docstrings
    - [ ] Sin imports circulares
    
  tests:
    - [ ] Cobertura >80%
    - [ ] Tests unitarios para cada método público
    - [ ] Tests de casos edge
    - [ ] Tests de errores
    
  calidad:
    - [ ] Pylint score >8.0
    - [ ] Sin errores de mypy
    - [ ] Complejidad ciclomática <10
    - [ ] Sin vulnerabilidades de seguridad
    
  documentacion:
    - [ ] AGENT-CONTEXT actualizado
    - [ ] Output para siguiente agente generado
    - [ ] Decisiones técnicas documentadas
    - [ ] README actualizado si aplica
```

## 📝 FORMATO DE REPORTE FINAL

### Reporte de Éxito
```markdown
✅ [NOMBRE]-Agent completado exitosamente

📊 RESUMEN EJECUTIVO
- Estado: COMPLETADO
- Tiempo de ejecución: Xm Ys
- Componentes creados: N
- Cobertura de tests: X%
- Reutilización lograda: X%

📦 COMPONENTES CREADOS
[Lista detallada con ubicaciones]

🔧 DECISIONES TÉCNICAS
[Decisiones importantes tomadas]

📈 MÉTRICAS DE CALIDAD
- Pylint Score: X.X/10
- Complejidad: Baja/Media/Alta
- Vulnerabilidades: 0

➡️ SIGUIENTE PASO
Ejecutar [SIGUIENTE]-Agent con el output generado en:
/docs/projects/[CODIGO]/AGENT-CONTEXT-[CODIGO].md

Output específico disponible en la sección "OUTPUT_[NOMBRE]_AGENT"
```

### Reporte de Error
```markdown
⚠️ [NOMBRE]-Agent requiere intervención

🚨 ERROR DETECTADO
- Tipo: [CRITICO|ALTO|MEDIO|BAJO]
- Descripción: [Descripción del error]
- Ubicación: [archivo:línea]

🔍 DIAGNÓSTICO
[Análisis del problema]

💡 SOLUCIÓN PROPUESTA
[Pasos para resolver]

🔄 ACCIONES REQUERIDAS
1. [Acción 1]
2. [Acción 2]

⏮️ ROLLBACK
Para revertir cambios parciales:
[Comandos o pasos necesarios]
```

## 🔗 INTEGRACIONES Y HERRAMIENTAS

### Para QUALITY-Agent Específicamente
```python
HERRAMIENTAS_QUALITY = {
    "analisis_estatico": [
        "pylint",           # Calidad de código
        "flake8",          # Estilo y errores
        "mypy",            # Type checking
        "black",           # Formateo
        "isort",           # Ordenamiento de imports
    ],
    "seguridad": [
        "bandit",          # Vulnerabilidades de seguridad
        "safety",          # Dependencias vulnerables
        "pip-audit",       # Auditoría de paquetes
    ],
    "complejidad": [
        "radon",           # Complejidad ciclomática
        "xenon",           # Umbral de complejidad
        "mccabe",          # Complejidad McCabe
    ],
    "deuda_tecnica": [
        "vulture",         # Código muerto
        "prospector",      # Análisis comprehensivo
        "sonarqube",       # Si está disponible
    ],
    "tests": [
        "pytest-cov",      # Cobertura
        "pytest-xdist",    # Ejecución paralela
        "hypothesis",      # Property-based testing
    ]
}
```

### Comandos de Validación
```bash
# Comandos que cada agente puede ejecutar
# Formato
black --check --line-length 100 .

# Linting
pylint --rcfile=.pylintrc [module]

# Type checking  
mypy --strict [module]

# Tests
pytest --cov=[module] --cov-report=term-missing

# Seguridad
bandit -r [module]

# Complejidad
radon cc -s [module]
```

## 🚨 MANEJO DE SITUACIONES ESPECIALES

### Conflictos de Merge en Archivos Compartidos
```python
def manejar_conflicto_init_py():
    """
    Estrategia para resolver conflictos en __init__.py
    """
    # 1. Crear backup
    backup_file("__init__.py")
    
    # 2. Leer contenido actual
    current_exports = read_current_exports()
    
    # 3. Añadir nuevos exports sin duplicar
    new_exports = get_new_exports()
    merged_exports = merge_exports(current_exports, new_exports)
    
    # 4. Escribir versión actualizada
    write_exports(merged_exports)
    
    # 5. Validar sintaxis
    validate_python_syntax("__init__.py")
```

### Dependencias No Cumplidas
```python
def manejar_dependencias_faltantes():
    """
    Qué hacer cuando el agente anterior no completó correctamente
    """
    # 1. Documentar el problema
    log_dependency_issue()
    
    # 2. Intentar proceder con lo disponible
    if can_proceed_partially():
        proceed_with_warnings()
    else:
        # 3. Reportar y detener
        report_blocking_issue()
        request_manual_intervention()
```

## 📚 REFERENCIAS Y RECURSOS

### Documentación Obligatoria
- `/docs/01-METODOLOGIA-DESARROLLO-CLAUDE.md`
- `/docs/02-SISTEMA-CODIFICACION-DOCS.md`
- `/docs/03-PROYECTOS-PREVIOS.md`
- `/docs/04-FLUJO-AGENTES.md`

### Recursos Específicos del Agente
- [Documentación específica del dominio]
- [Guías de estilo y patrones]
- [Ejemplos de implementaciones previas]

## ⚡ RESPUESTAS RÁPIDAS Y DECISIONES PREDEFINIDAS

### Decisión: Reutilización vs Nueva Implementación
```python
if similitud > 0.8 and mismo_dominio:
    reutilizar_con_adaptacion()
elif similitud > 0.5:
    usar_como_template()
else:
    implementar_desde_cero()
```

### Decisión: Nivel de Testing
```python
if componente.es_critico():
    cobertura_objetivo = 95
    incluir_tests_integracion = True
    incluir_property_testing = True
else:
    cobertura_objetivo = 80
    incluir_tests_integracion = False
```

### Decisión: Manejo de Errores
```python
if error.es_recuperable():
    implementar_retry_logic()
    log_warning()
else:
    raise_exception()
    documentar_en_agent_context()
```

## 🎯 CONFIGURACIÓN ESPECÍFICA POR TIPO DE AGENTE

### Para Agentes de Dominio (DOMAIN-Agent)
```python
CONFIGURACION_DOMINIO = {
    "foco": "Entidades y Value Objects",
    "prohibido": "Dependencias de infraestructura",
    "patrones": ["Entity", "Value Object", "Domain Service", "Domain Event"],
    "validaciones": ["Invariantes de negocio", "Reglas de dominio"]
}
```

### Para Agentes de Aplicación (DTOS/PORTS/USECASES)
```python
CONFIGURACION_APLICACION = {
    "foco": "Orquestación y contratos",
    "prohibido": "Lógica de negocio compleja",
    "patrones": ["DTO", "Port", "Use Case", "Application Service"],
    "validaciones": ["Contratos de interfaz", "Flujos de negocio"]
}
```

### Para Agentes de Adaptadores (MODELS/REPOSITORIES/ROUTES)
```python
CONFIGURACION_ADAPTADORES = {
    "foco": "Implementaciones concretas",
    "prohibido": "Lógica de negocio",
    "patrones": ["Repository", "Mapper", "Adapter", "Controller"],
    "validaciones": ["Conversión de datos", "Persistencia", "API contracts"]
}
```

### Para Agentes de Soporte (TEST/DOCUMENT/QUALITY)
```python
CONFIGURACION_SOPORTE = {
    "foco": "Calidad y documentación",
    "prohibido": "Modificar lógica de negocio",
    "patrones": ["AAA Testing", "Test Fixtures", "Documentation as Code"],
    "validaciones": ["Cobertura", "Estándares", "Completitud"]
}
```

## 🔄 CICLO DE VIDA DEL AGENTE

### Estados del Agente
```python
ESTADOS_AGENTE = {
    "INICIALIZANDO": "Leyendo contexto y validando precondiciones",
    "ANALIZANDO": "Identificando trabajo a realizar",
    "IMPLEMENTANDO": "Creando/modificando código",
    "VALIDANDO": "Ejecutando tests y verificaciones",
    "DOCUMENTANDO": "Actualizando documentación",
    "COMPLETADO": "Listo para siguiente agente",
    "ERROR": "Requiere intervención manual",
    "BLOQUEADO": "Esperando dependencias"
}
```

### Transiciones Válidas
```mermaid
graph LR
    INICIALIZANDO --> ANALIZANDO
    ANALIZANDO --> IMPLEMENTANDO
    IMPLEMENTANDO --> VALIDANDO
    VALIDANDO --> DOCUMENTANDO
    VALIDANDO --> ERROR
    DOCUMENTANDO --> COMPLETADO
    ERROR --> INICIALIZANDO
    ANALIZANDO --> BLOQUEADO
    BLOQUEADO --> ANALIZANDO
```

## 📊 MÉTRICAS Y KPIs

### Métricas Obligatorias por Agente
```yaml
metricas_tracking:
  rendimiento:
    tiempo_ejecucion: "minutos"
    archivos_procesados: "cantidad"
    lineas_codigo: "cantidad"
    
  calidad:
    cobertura_tests: "porcentaje"
    complejidad_ciclomatica: "promedio"
    deuda_tecnica: "horas"
    vulnerabilidades: "cantidad"
    
  reutilizacion:
    componentes_reutilizados: "cantidad"
    porcentaje_reutilizacion: "porcentaje"
    tiempo_ahorrado: "horas"
    
  errores:
    errores_sintaxis: "cantidad"
    errores_tipo: "cantidad"
    warnings: "cantidad"
    errores_test: "cantidad"
```

### Dashboard de Estado
```markdown
📊 DASHBOARD [NOMBRE]-Agent
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⏱️ Tiempo: [X]m [Y]s
📁 Archivos: [N] creados, [M] modificados
📝 Código: [X] líneas
🧪 Tests: [X]% cobertura
♻️ Reutilización: [X]%
⚠️ Warnings: [N]
❌ Errores: [N]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Estado: [ESTADO_ACTUAL]
Progreso: ▓▓▓▓▓▓░░░░ 60%
```

## 🔐 CONSIDERACIONES DE SEGURIDAD

### Validaciones de Seguridad Obligatorias
```python
SEGURIDAD_CHECKLIST = {
    "input_validation": {
        "sanitizacion": True,
        "tipos_estrictos": True,
        "limites": True
    },
    "autenticacion": {
        "verificar_permisos": True,
        "validar_tokens": True
    },
    "datos_sensibles": {
        "no_logs": True,
        "encriptacion": True,
        "ofuscacion": True
    },
    "dependencias": {
        "verificar_vulnerabilidades": True,
        "versiones_minimas": True
    }
}
```

## 🏁 CHECKLIST FINAL DEL AGENTE

### Antes de Reportar Completado
- [ ] Todos los componentes implementados
- [ ] Tests ejecutados y pasando
- [ ] Cobertura >80%
- [ ] Sin errores de linting
- [ ] Sin vulnerabilidades de seguridad
- [ ] Documentación actualizada
- [ ] AGENT-CONTEXT actualizado
- [ ] Output para siguiente agente generado
- [ ] __init__.py actualizado
- [ ] Backup de archivos modificados
- [ ] Métricas registradas
- [ ] Decisiones técnicas documentadas
- [ ] Código formateado con black
- [ ] Imports ordenados con isort
- [ ] Type hints completos

---

## 📝 NOTAS DE IMPLEMENTACIÓN

### Para el Desarrollador del Agente
1. Esta plantilla es la base común para todos los agentes
2. Personalizar las secciones marcadas con [PLACEHOLDER]
3. Mantener la estructura de INPUT/OUTPUT para comunicación
4. El AGENT-CONTEXT es el medio principal de comunicación
5. Siempre validar el trabajo del agente anterior
6. Documentar TODAS las decisiones técnicas
7. Priorizar reutilización sobre nueva implementación
8. Los tests son obligatorios, no opcionales
9. La calidad del código es responsabilidad de cada agente
10. En caso de duda, documentar y continuar

### Versionado de la Plantilla
- **v1.0**: Plantilla inicial base
- **v2.0**: Añadido sistema de permisos y manejo de conflictos
- **v2.1**: Integración con herramientas de quality assurance
- **v2.2**: Métricas y KPIs obligatorios

---

**Plantilla Maestra Versión**: 2.2
**Optimizada para**: Claude Code con Agentes Secuenciales
**Arquitectura**: Hexagonal (Ports & Adapters)
**Stack Principal**: Python 3.11+, FastAPI, SQLAlchemy, Pytest
**Última actualización**: 2025-01-15
**Autor**: Sistema de Agentes Especializados
**Licencia**: Uso interno del proyecto
