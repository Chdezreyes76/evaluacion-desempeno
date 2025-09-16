# Diseño de Entidades para la Aplicación de Evaluación del Desempeño

Este documento organiza las entidades identificadas en módulos dentro de
una arquitectura hexagonal (domain, application, adapters),
clasificándolas en **Entidades Puras**, **Value Objects** y
**Agregados**.\
Cada elemento incluye una breve explicación de su propósito.

------------------------------------------------------------------------

## Módulo de Organización

### Entidades Puras

-   **Usuario**: Representa a cualquier persona con acceso al sistema
    (empleados internos, clientes externos).\
-   **Rol**: Define los perfiles de acceso (ej. Administrador, RRHH,
    Evaluador, Evaluado).\
-   **Permiso**: Capacidades específicas asociadas a los roles.\
-   **Departamento**: Unidad organizativa de la empresa.\
-   **Puesto**: Posición formal dentro de la estructura organizativa.

### Value Objects

-   **IdentidadUsuario**: Representa la identidad única de un usuario.\
-   **CorreoInstitucional**: Dirección de contacto validada para el
    usuario.

### Agregados

-   **Organigrama**: Agregado que vincula usuarios, departamentos y
    puestos para representar la jerarquía.

------------------------------------------------------------------------

## Módulo de Competencias

### Entidades Puras

-   **MapaDeCompetencias**: Catálogo maestro de competencias de la
    organización.\
-   **Competencia**: Conjunto de habilidades técnicas o blandas a
    evaluar.\
-   **IndicadorConductual**: Descriptores observables que evidencian la
    competencia.\
-   **NivelCompetencia**: Escala que define los grados de dominio.

### Value Objects

-   **EscalaValoración**: Define la forma de medir (1--5, Likert,
    etc.).\
-   **PesoCompetencia**: Ponderación relativa dentro de una evaluación.

### Agregados

-   **PerfilCompetenciasPuesto**: Relaciona un puesto con las
    competencias requeridas y sus niveles esperados.

------------------------------------------------------------------------

## Módulo de Evaluación 360°

### Entidades Puras

-   **CicloEvaluación**: Campaña o ventana temporal de evaluación.\
-   **Configuración360**: Reglas de participación (quién evalúa, pesos,
    anonimato).\
-   **PlantillaCuestionario**: Estructura de preguntas a usar.\
-   **Pregunta**: Ítem evaluable (cerrada, abierta, evidencia).\
-   **OpciónRespuesta**: Alternativas posibles.

### Value Objects

-   **EstadoCiclo**: Define si un ciclo está "Planificado", "Activo",
    "Cerrado". Sirve para controlar en qué fase se encuentra la
    evaluación.\
-   **TokenInvitación**: Código de acceso único y temporal para que un
    evaluador responda.\
-   **EscalaRespuesta**: Define cómo se valoran las respuestas (p. ej.,
    1 = Nunca, 5 = Siempre).

### Agregados

-   **Evaluación**: Agregado raíz que vincula a un evaluado con un
    ciclo, un cuestionario y los evaluadores asignados.\
-   **ParticipaciónEvaluador**: Relación evaluado--evaluador con su rol
    (superior, par, subordinado, cliente).\
-   **Respuesta**: Registro de valoraciones para cada pregunta. Incluye
    comentarios y evidencias.

------------------------------------------------------------------------

## Módulo de Resultados

### Entidades Puras

-   **AgregaciónResultados**: Consolida y calcula promedios y brechas de
    desempeño.\
-   **Informe**: Documento generado con resultados para un evaluado.

### Value Objects

-   **MétricaCompetencia**: Valor calculado de una competencia
    específica.\
-   **BrechaCompetencia**: Diferencia entre nivel esperado y nivel
    observado.

### Agregados

-   **Reporte360**: Agregado que contiene las métricas, comentarios y
    comparaciones por ciclo.

------------------------------------------------------------------------

## Módulo de Desarrollo

### Entidades Puras

-   **PlanDesarrolloIndividual (PDI)**: Plan de acción personalizado
    para un colaborador.\
-   **AcciónDesarrollo**: Actividad concreta (formación, mentoring,
    proyecto).

### Value Objects

-   **EstadoAcción**: Define si una acción está "Pendiente", "En curso",
    "Completada".\
-   **PrioridadAcción**: Nivel de prioridad (alta, media, baja).

### Agregados

-   **SeguimientoPDI**: Agregado que controla el avance del plan, hitos
    y resultados.

------------------------------------------------------------------------

## Módulo de Soporte

### Entidades Puras

-   **Notificación**: Recordatorios y avisos enviados al usuario.\
-   **ClienteExterno**: Persona o entidad externa que participa como
    evaluador.\
-   **Auditoría**: Registro de acciones en el sistema para trazabilidad.

### Value Objects

-   **PreferenciaPrivacidad**: Configura anonimato y consentimiento en
    un ciclo.\
-   **PlantillaNotificación**: Define formato de mensajes enviados.

### Agregados

-   **SistemaMensajería**: Agregado encargado de gestionar las
    notificaciones y su historial.

------------------------------------------------------------------------

## Notas Finales

-   Los **Agregados** agrupan y coordinan cambios en varias entidades
    relacionadas.\
-   Los **Value Objects** no tienen identidad propia, representan
    conceptos medibles, estados o valores inmutables.\
-   Las **Entidades Puras** se identifican de manera única y suelen ser
    persistidas directamente en la base de datos.
