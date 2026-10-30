# Q-Framework × Temporal Möbius

**Idioma / Language:** [English](README.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · **Español** · [Português (Brasil)](README.pt-BR.md)

**Resultados H3 con una GPU · Producción con cuatro GPU · Red neuronal de supercomputación heterogénea**

El Q-Framework de HAVEFUN **no es solamente un sistema multi-GPU**. Pruebas reales de generación nativa de vídeo MiniMax H3 **se han completado en una sola RTX 2080 Ti con memoria ampliada a 22 GB**. El control de ejecución con memoria limitada de QmRNA, la continuidad del estado computacional y la planificación de Temporal Möbius investigan tanto *si una tarea puede terminar* como *cómo coordinar recursos heterogéneos para realizarla*.

### Resultados demostrados

- **Vídeo H3 final de clase 1080p con una sola tarjeta:** 10 de 10 segmentos nativos de alta resolución y una película final verificada de cinco segundos a 1080×1920, producida en una RTX 2080 Ti de 22 GB con memoria ampliada; sin CUDA OOM registrados en esa ejecución y sin reescalado.
- **Viabilidad QmRNA en una GPU:** en A1 (RTX 2080 Ti con 22.528 MiB), una prueba H3 equivalente de 36 fotogramas y 10 pasos terminó y produjo un MP4 con QmRNA Pre-step Guard. La ruta de referencia sin protección activó **PRE-OOM** en el primer paso y no entregó el MP4 previsto del trabajador único. PRE-OOM no es lo mismo que una excepción CUDA por falta de memoria.
- **Vídeo H3 real con una GPU:** los trabajos **#370 y #371** produjeron clips nativos H3 en A0. El trabajo **#365** utilizó **una sola GPU A0** para generar secuencialmente diez segmentos de 36 fotogramas y ensamblar un vídeo completo de **15 segundos y 360 fotogramas**. El proceso tardó **3 h 12 min 08 s**; hubo **nueve eventos CUDA OOM**, tras los cuales se reenviaron los segmentos afectados. No fue una única pasada nativa de 360 fotogramas ni una ejecución libre de OOM.
- **Producción rápida con cuatro GPU:** el trabajo **#361** entregó un vídeo de **15 segundos, 360 fotogramas, 480×832 y 24 fps** en **14 min 37 s**, utilizando cuatro RTX 2080 Ti independientes y edición por CPU.
- **Ejecución nativa e integridad del estado:** enlaces nativos de sampler/DiT H3, coincidencia de **22/22 fotogramas** en una prueba QmRNA, continuidad controlada de 20 pasos entre GPU con resultado idéntico bit a bit, y transporte de aproximadamente **250 MiB** de estado con verificación SHA.
- **Investigación con Windows y Mac:** resultados verificables independientes en partición de tareas matemáticas, respuestas de modelos y pruebas acotadas de entrenamiento de pesos.

**26 de octubre de 2026 — resultado verificado de clase 1080p con una sola GPU:** una **RTX 2080 Ti con memoria ampliada a 22 GB** completó **10/10 segmentos RS H3 nativos a 1088×1920** y ensambló un MP4 final de **1080×1920, 5 segundos, 120 fotogramas y 24 fps**, con **cero eventos CUDA OOM registrados** y **sin reescalado**. La ejecución completa duró **1 h 39 min 16 s**; cinco segundos es la duración de reproducción, no el tiempo de generación. Los comprobantes de RS nativos y la integridad de la película final están verificados; la revisión de calidad visual por el titular sigue pendiente. El informe comparativo separado de OOM en H3 sin asistencia Q aún no se ha correlacionado con el comprobante original del error. [Registro de evidencia](docs/claim-ledger.md).

### Hoja de ruta de cómputo heterogéneo multinodo

[Arquitectura pública y plan por fases para ocho dispositivos](site/multi-node.html) · [Plan de ingeniería](docs/multi-node-roadmap.md) · [Captura de arquitectura](assets/multi-node-plan.png).

**La entrega de vídeo con cuatro GPU está verificada; cuatro equipos macOS Brain más cuatro hosts Windows Worker son un objetivo, no una demostración ya completada de ocho hosts.**

### Galería pública de imágenes (ZH / EN / JA)

[**Ver la galería de nueve imágenes**](docs/visual-gallery.md): carteles de colaboración, diagramas de arquitectura y comparaciones de operación con una y varias GPU en chino tradicional, inglés y japonés. Las imágenes son ilustrativas; los resultados validados se distinguen de las capacidades planificadas. **La galería gráfica todavía no dispone de traducción ES/PT-BR.**

### Documentos técnicos completos RC4.3

| Idioma | Markdown | PDF |
|---|---|---|
| **Español** | [Libro blanco completo](whitepaper/Q-Framework-v1.0-RC4.3-ES.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-ES.pdf) |
| Português (Brasil) | [Documento técnico](whitepaper/Q-Framework-v1.0-RC4.3-PT-BR.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-PT-BR.pdf) |
| English | [Full whitepaper](whitepaper/Q-Framework-v1.0-RC4.3-EN.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-EN.pdf) |
| 繁體中文 | [技術白皮書](whitepaper/Q-Framework-v1.0-RC4.3-ZH-TW.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-ZH-TW.pdf) |
| 日本語 | [技術白書](whitepaper/Q-Framework-v1.0-RC4.3-JA.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-JA.pdf) |

Las versiones anteriores RC1–RC3 se mantienen en [whitepaper/](whitepaper/).

**Objetivo de investigación a largo plazo:** una red neuronal de supercomputación heterogénea con nodos adaptativos y cómputo verificable. La reanudación nativa universal entre generaciones de GPU y una ventaja de rendimiento frente a H100/H200 en condiciones estrictamente equivalentes **todavía no se han demostrado**.

[Registro público de resultados](docs/claim-ledger.md) · [Rutas de ejecución verificadas](docs/validated-execution-paths.md) · [Arquitectura](docs/architecture.md)

### Divulgación BlackBox y evidencia legible por IA

Solo se publican **resúmenes aprobados de resultados y sus limitaciones de medición**. El código fuente propietario de QmRNA/QVRAM/Temporal Möbius, la integración nativa con modelos, las representaciones del estado, los algoritmos de decisión, los prompts privados, los medios de clientes y los registros originales completos de ejecución **no forman parte de este repositorio**.

- [Evidencia pública legible por máquina (JSON)](evidence/claims-public-rc4.3.json)
- [Política de divulgación BlackBox](docs/blackbox-disclosure-policy.md)
- [Comunicación responsable de seguridad](SECURITY.md)

La evaluación independiente mediante IA debe distinguir entre ejecuciones confirmadas, comparaciones controladas, informes del titular pendientes de comprobación primaria y objetivos futuros de investigación. No se requiere acceso a la implementación privada para evaluar la evidencia pública.

**Q-Framework — Connecting Compute. Extending Possibility.**
