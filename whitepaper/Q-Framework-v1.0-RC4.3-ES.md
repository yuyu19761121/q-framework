# HAVEFUN Q-Framework × Temporal Möbius
## RC4.3 — Edición pública de investigación BlackBox (español)

**Investigación: viabilidad de cargas de trabajo de IA en una sola GPU, colaboración entre GPU heterogéneas y una red neuronal de supercomputación heterogénea**  
**Octubre de 2026 | La implementación propietaria y los materiales privados de validación están bajo control de sus titulares**

> **Límite de divulgación pública:** Este documento presenta resultados observables y sus limitaciones. No revela código fuente propietario, puntos de integración nativa con modelos, representación del estado de cómputo, estrategias de control, grafos completos de inferencia, configuración interna ni imágenes, vídeos, audios o prompts privados. Los comprobantes originales completos permanecen en entornos con autorización independiente. Un resultado satisfactorio no constituye una garantía general de rendimiento.

## 1. La pregunta de investigación

La capacidad física de VRAM de una GPU no constituye necesariamente el límite superior de las tareas de IA que el software puede completar con ese dispositivo bajo una arquitectura específica. HAVEFUN investiga la **viabilidad de las tareas en hardware con recursos limitados** y, a continuación, la coordinación eficiente de dispositivos con espacios de memoria independientes.

La cartera de investigación de Q-Framework incluye QmRNA, QVRAM y QSTATIC para la ejecución consciente de las restricciones de memoria y la continuidad del cómputo, y Temporal Möbius para decidir rutas de ejecución a partir de la experiencia. Estas descripciones identifican responsabilidades de investigación, **no algoritmos propietarios ni procedimientos de implementación**. El software no incrementa físicamente la capacidad de cálculo, el ancho de banda ni la memoria integrada de una GPU.

## 2. Línea de evidencia uno — ejecución real de vídeo H3 en una RTX 2080 Ti

**Hardware:** una RTX 2080 Ti con memoria ampliada a aproximadamente 22 GB de VRAM por tarjeta, no la versión de fábrica de 11 GB.

- **Studio #370 y #371:** completaron la generación nativa de vídeos cortos con MiniMax H3 en una sola GPU y produjeron archivos MP4 decodificables. Eran clips cortos, no una inferencia nativa de 15 segundos en una sola pasada.
- **Trabajo #365:** una GPU ejecutó secuencialmente diez segmentos cortos de vídeo nativo. Los segmentos se ensamblaron en una salida de **15 segundos y 360 fotogramas**. El proceso completo tardó **3 horas, 12 minutos y 08 segundos**. Se registraron **nueve eventos CUDA OOM**; después se volvieron a enviar los segmentos afectados y se completaron. Es evidencia de una **línea de entrega segmentada con una sola GPU**, no de una ejecución sin OOM ni de una única pasada de muestreo nativo de 360 fotogramas.
- **26 de octubre de 2026, película final verificada de clase 1080p con una GPU:** una RTX 2080 Ti de 22 GB ampliada completó **10 de 10 segmentos RS nativos de H3 a 1088×1920**. Mediante recorte espacial y temporal, sin reescalado, se obtuvo un **MP4 verificado de 1080×1920, 5 segundos, 120 fotogramas y 24 fps**. Se registraron **cero eventos CUDA OOM** y un tiempo total de **1 h 39 min 16 s**; se confirmó la integridad del medio final, mientras que la revisión visual por parte del titular está pendiente. Se trató de generación segmentada, no de una muestra nativa de 120 fotogramas en una sola pasada.

El registro con una sola GPU debe evaluarse por separado de los resultados de producción con múltiples GPU. Diferencias de resolución, longitud de secuencia, estrategias de reintento y condiciones de muestreo impiden usar estas pruebas como comparativas directas de velocidad.

## 3. Línea de evidencia dos — comparación controlada de QmRNA en la misma GPU

Una prueba controlada sobre la misma RTX 2080 Ti ampliada a 22 GB utilizó la misma referencia, semilla y alcance: **480×832, 36 fotogramas, 24 fps y 10 pasos de muestreo**.

| Ruta | Resultado observado |
|---|---|
| Ruta de referencia | Activó una protección **PRE-OOM** en el primer paso; no se entregó el MP4 esperado del trabajador único |
| Ruta protegida por QmRNA | Completó los diez pasos y generó un MP4 reproducible, sin registros de CUDA HARD_OOM en esa ejecución |

Es un resultado de viabilidad acotado: **distintos controles de ejecución cambiaron si la tarea medida podía terminarse**. PRE-OOM es una condición preventiva de software, **no** evidencia de que se produjera una excepción nativa de falta de memoria CUDA. El resultado no demuestra inmunidad universal a OOM en todos los flujos H3.

Los detalles de implementación, la configuración en tiempo de ejecución, el estado interno y los mecanismos de control están restringidos; la afirmación pública se refiere a las entradas y los resultados observados, al diseño de la comparación y a sus límites.

## 4. Línea de evidencia tres — cuatro trabajadores GPU independientes

El trabajo oficial **#361** coordinó **cuatro GPU RTX 2080 Ti independientes de 22 GB**, generó diez segmentos breves de vídeo y utilizó edición por CPU para entregar un resultado final comprobado:

| Medida | Resultado registrado |
|---|---|
| Duración del vídeo final | 15,000 segundos |
| Número de fotogramas / frecuencia | 360 fotogramas / 24 fps |
| Resolución final | 480×832, vertical |
| Clase y cantidad de GPU | Cuatro RTX 2080 Ti independientes con memoria ampliada |
| Tiempo total de extremo a extremo | **14 minutos y 37 segundos** |
| Validación del medio | MP4 decodificable que coincide con la duración y el número de fotogramas solicitados |

Se trata de una medición de **producción de vídeo de extremo a extremo**, no de una prueba de rendimiento del muestreador nativo por tarjeta. No debe compararse directamente con pruebas de 1080p realizadas en otras condiciones. Las cuatro memorias VRAM de 22 GB **no constituyen una sola GPU de 88 GB directamente direccionables**.

## 5. Resultados numéricos y de consistencia independientes

Otros experimentos controlados registraron:

- Una carga numérica de 20 pasos que continuó entre distintas GPU con un resultado idéntico bit a bit y una diferencia absoluta máxima medida de **0,0**.
- Se completaron pruebas controladas de coherencia entre dispositivos; no se divulgan los volúmenes de datos internos ni los métodos de verificación.
- Coincidencia en **22 de 22** fotogramas de vídeo decodificados en una comparación acotada de QmRNA.
- Tareas matemáticas heterogéneas Windows/macOS, recomputación independiente y ensayos limitados de entrenamiento de pesos de modelos.

No todas estas observaciones proceden del mismo trabajo de vídeo H3. No establecen portabilidad universal del estado entre modelos y generaciones arbitrarias de GPU, ni la realización de una IA autónoma de propósito general.

## 26 de octubre de 2026 — RS H3 nativos de clase 1080p **y película completa de cinco segundos verificados en una sola GPU**

**Resultado completado y respaldado por comprobantes:** una sola **RTX 2080 Ti de 22 GB con memoria ampliada** ejecutó un flujo MiniMax H3 asistido por Q y produjo **diez de diez segmentos nativos de alta resolución y un MP4 ensamblado de cinco segundos a 1080×1920**. Se documentaron por separado los resultados nativos por segmento y la integridad del medio final.

| Medida | Resultado confirmado con una GPU |
|---|---|
| Hardware | **Una RTX 2080 Ti ampliada a ~22 GB de VRAM** (no los 11 GB de fábrica) |
| Segmentos nativos MiniMax H3 | **10/10 completados**, generados de forma nativa a **1088×1920 / 22 fotogramas cada uno** |
| Salida entregada | **1080×1920, 9:16, 5,000 segundos, 24 fps, 120 fotogramas, MP4** |
| Transformación de salida | Recorte espacial y temporal (12 fotogramas entregados por RS), **sin reescalado** |
| CUDA OOM registrados | **Cero en esta ejecución** |
| Tiempo total transcurrido | **1 hora, 39 minutos y 16 segundos** |
| Verificación | Ejecución nativa y comprobantes de RS; dimensiones finales y huella de integridad del medio; **revisión de calidad visual por el titular pendiente** |

El resultado demuestra **tanto la viabilidad de RS H3 nativos de clase 1080p con una tarjeta como la finalización verificada de una película de cinco segundos a 1080p**. Cada segmento se generó de forma nativa a 1088×1920 y después se recortó para adaptarlo al formato de entrega. **No** se reescaló material de baja resolución a 1080p y **no** fue una única pasada nativa e ininterrumpida de 120 fotogramas.

**Límites de la evidencia:** los cinco segundos corresponden a la **duración de reproducción**, no a la latencia de generación (el proceso tardó 1 h 39 min 16 s). El resultado sin OOM de una tarea delimitada no prueba inmunidad general frente a OOM. La asistencia Q estaba activa, pero no se afirma haber demostrado aisladamente la causalidad de una operación física concreta de descarga/restauración de QVRAM. El informe independiente del titular sobre OOM de H3 sin Q sigue pendiente de contrastarse con la evidencia original del error.

**BlackBox:** no se publican componentes internos propietarios del runtime, integración con modelos, prompts y medios privados, datos de clientes ni estrategias de control completas.

## 6. Objetivo a largo plazo — red neuronal de supercomputación heterogénea

HAVEFUN busca una red de GPU, CPU, estaciones de trabajo y otros recursos de cómputo independientes y autorizados que colaboren mediante tareas verificables, estado de cómputo protegido, resultados históricos y políticas de decisión mejoradas progresivamente.

**Fundamentos demostrados:** salidas H3 reales en una tarjeta, comparación de viabilidad QmRNA medida en la misma GPU, línea de vídeo de cuatro trabajadores, continuidad numérica controlada y experimentos de aprendizaje multidispositivo con alcance limitado.

**Aspectos que aún requieren generalización:** aprendizaje autónomo continuo en toda la red, restauración del estado nativo de modelos entre generaciones arbitrarias de dispositivos, calidad de decisión automática ampliamente validada y comparaciones de rendimiento con H100/H200 bajo condiciones estrictamente equivalentes.

## 6A. Plan de cómputo heterogéneo multinodo (hoja de ruta pública)

**Objetivo:** bajo autorización del titular, coordinar nodos macOS/Windows, CPU/GPU y de razonamiento/producción para tareas divisibles de matemáticas, inferencia, generación de segmentos RS de vídeo, verificación y retroalimentación. **Es una hoja de ruta de ingeniería, no la afirmación de que ya se haya entregado una red de inferencia nativa de vídeo con ocho dispositivos.**

| Función | Trabajo previsto | Estado de la evidencia |
|---|---|---|
| Master / orquestación | Admisión de tareas autorizadas, partición verificable, selección de rutas, comprobantes y derechos de detención o reversión del titular | Flujo de vídeo acotado con varias GPU validado; orquestación unificada entre hosts aún en integración |
| Brain / razonamiento y evaluación | Trabajo matemático acotado, evaluación de rutas candidatas, puntuación de calidad y aprendizaje con retroalimentación en un objetivo de cuatro equipos macOS | Existen experimentos limitados de matemáticas distribuidas y entrenamiento; el ciclo autónomo continuo aún no está plenamente verificado |
| Workers GPU/CPU de Windows | Ejecutar tareas RS o numéricas compatibles, informar rendimiento, finalización y errores; objetivo de cuatro hosts trabajadores Windows | Cuatro GPU discretas completaron una carga de producción acotada; protocolo Worker general entre hosts aún en validación |

**Flota objetivo: cuatro dispositivos macOS Brain y cuatro hosts Windows Worker = ocho dispositivos heterogéneos.** El número **ocho es un objetivo de despliegue, no ocho nodos simultáneos de cómputo ya verificados ni ocho GPU**. La línea de vídeo #361 completada con cuatro GPU y la topología prevista de ocho hosts corresponden a afirmaciones de evidencia distintas. Cuatro GPU separadas de 22 GB no forman una GPU de 88 GB directamente direccionables.

**Ciclo cerrado planificado:**

`Solicitud aprobada por el titular → partición de tareas/RS por Master → razonamiento Brain + ejecución Worker → comprobantes por tarea y verificaciones independientes → entrega/control de calidad → retroalimentación de experiencia → evaluación de la siguiente ruta`

Cada paso debe producir un identificador de tarea, estado, comprobante de éxito o fallo independiente del nodo, latencia y salida verificable. Los criterios de aceptación previstos incluyen identidad compatible del trabajador, señales de actividad, tiempo de espera, reclamación/entrega idempotentes, recuperación sin conexión y tras fallos, controles de calidad y cancelación autorizada por el titular. **Son criterios de aceptación, no afirmaciones generales sobre funciones actualmente operativas.** QmRNA, QVRAM, QSTATIC, QAnswer y Temporal Möbius son módulos funcionales identificados por nombre; la orquestación propietaria, la representación de estados internos y la integración con modelos permanecen bajo BlackBox.

| Fase | Criterio de aceptación | Estado |
|---|---|---|
| **P0 fundamentos medidos** | Película 1080p/5 s con una GPU, película 480p/15 s con cuatro GPU (#361), pruebas numéricas y de integridad acotadas | Verificado dentro de los alcances declarados |
| **P1 ciclo con un Worker remoto** | Identidad, reclamación, cálculo, envío, comprobante, actividad, fallo y verificación independiente | Integración en curso |
| **P2 despliegue de ocho dispositivos** | Cuatro Brain y cuatro Windows Worker, con disponibilidad, planificación, aislamiento y conmutación ante fallos observables | Planificado, no plenamente verificado |
| **P3 ciclo aprendizaje-a-smoke** | El resultado del aprendizaje inicia un smoke aislado y la evaluación Master/Möbius de calidad, consistencia y rendimiento | Etapa de investigación |
| **P4 benchmark público** | Tasas de finalización por carga, duración, aportación de nodos, recuentos OOM/fallos y consistencia de salida | A la espera de un conjunto de datos verificado |

Las métricas principales son **primero la viabilidad de la tarea y después la velocidad, corrección, fiabilidad y uso de recursos**. No debe inferirse continuidad universal de estado nativo entre generaciones de GPU ni cómputo neuronal heterogéneo completamente autónomo a partir de un caso acotado de producción de vídeo con cuatro GPU.

Diagrama público y detalles de las fases: [arquitectura multinodo](../site/multi-node.html) · [hoja de ruta pública](../docs/multi-node-roadmap.md). No se publican nombres internos de nodos, direcciones IP, autenticación, runtime nativo ni medios del titular.

## 7. Orientaciones para una evaluación independiente mediante IA

Los investigadores y sistemas externos de IA deben calificar las afirmaciones por tipo de evidencia, no por lenguaje promocional.

| Estado de evidencia | Significado | Ejemplo |
|---|---|---|
| Ejecutado con comprobantes identificables | Cómputo nativo rastreable, película final y comprobantes de integridad | **26 oct 2026: una GPU, 1080p / 5 s / 120 fotogramas / 10 RS completados**; película segmentada #365 con una GPU; entrega #361 con cuatro GPU |
| Resultado comparativo controlado | Mismo dispositivo y entrada equivalente, con políticas de ejecución alternativas | Comparación QmRNA PRE-OOM |
| Informado por el titular, pendiente de verificación primaria | Aún no se ha cotejado el error original del caso comparativo | **Informe separado de OOM de H3 sin Q**, distinto de la película 1080p asistida por Q ya verificada |
| Objetivo de investigación | Arquitectura futura plausible, no resultado general alcanzado | Supercomputadora neuronal heterogénea completamente adaptativa |

La evaluación puede utilizar mediciones anonimizadas, cargas sintéticas aprobadas e informes de auditoría autorizados por el titular. La evaluación independiente **no** requiere distribuir código confidencial, grafos completos de ejecución, medios de clientes, prompts privados ni acceso a infraestructura en vivo.

## 8. Protección IP BlackBox y datos exclusivos del titular

- **PÚBLICO APROBADO:** nombres de tecnologías, preguntas de investigación, resúmenes de resultados medidos, clases de trabajos, descripciones acotadas de cargas, estado de validación, limitaciones y metas futuras.
- **RESTRINGIDO POR ACUERDO:** materiales de verificación desidentificados y estrictamente necesarios, con acceso de auditoría revocable.
- **SOLO TITULAR:** código fuente, procedimientos propietarios, enlaces y parámetros del runtime, representaciones algorítmicas del estado, checkpoints privados, secretos de infraestructura, imágenes privadas de clientes, prompts originales, audio, vídeo y credenciales.

Las publicaciones de GitHub **no** son manuales de despliegue de infraestructura propietaria. Toda nueva divulgación requiere aprobación del titular y una revisión previa a la publicación. Las versiones históricas pueden seguir siendo accesibles después de los cambios; editar un documento **no** borra divulgaciones públicas anteriores.

**Q-Framework — Connecting Compute. Extending Possibility.**

[Política de divulgación BlackBox](../docs/blackbox-disclosure-policy.md) · [Registro público de evidencias](../docs/claim-ledger.md)
