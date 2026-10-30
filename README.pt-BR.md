# Q-Framework × Temporal Möbius

**Idioma / Language:** [English](README.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · **Português (Brasil)**

**Resultados H3 com uma GPU · Produção com quatro GPUs · Rede neural de supercomputação heterogênea**

O Q-Framework da HAVEFUN **não é apenas um sistema multi-GPU**. Testes reais de geração nativa de vídeo MiniMax H3 **foram concluídos em uma única RTX 2080 Ti com memória expandida para 22 GB**. O controle de execução com pouca memória do QmRNA, a continuidade do estado computacional e o agendamento do Temporal Möbius investigam tanto *se uma tarefa pode ser concluída* quanto *como coordenar recursos heterogêneos para executá-la*.

### Resultados demonstrados

- **Vídeo H3 final de classe 1080p com uma única placa:** 10 de 10 segmentos nativos de alta resolução e um filme final de cinco segundos em 1080×1920 verificado, produzido em uma RTX 2080 Ti expandida para 22 GB; sem CUDA OOM registrados nessa execução e sem upscaling.
- **Viabilidade do QmRNA em uma GPU:** na A1 (RTX 2080 Ti com 22.528 MiB), um teste H3 com condições equivalentes, 36 quadros e 10 etapas, foi concluído e produziu um MP4 usando QmRNA Pre-step Guard. A rota de referência sem proteção acionou **PRE-OOM** na primeira etapa e não entregou o MP4 esperado do worker único. PRE-OOM não é uma exceção CUDA de falta de memória.
- **Vídeo H3 real com uma GPU:** os Jobs **#370 e #371** produziram clipes H3 nativos na A0. O Job **#365** utilizou **uma única GPU A0** para gerar sequencialmente dez segmentos de 36 quadros e montar um vídeo completo de **15 segundos e 360 quadros**. A execução levou **3 h 12 min 08 s**; ocorreram **nove eventos CUDA OOM**, após os quais os segmentos afetados foram reenviados. Não foi uma única passagem nativa de 360 quadros nem uma execução livre de OOM.
- **Produção rápida com quatro GPUs:** o Job **#361** entregou um vídeo de **15 segundos, 360 quadros, 480×832 e 24 fps** em **14 min 37 s**, usando quatro RTX 2080 Ti independentes e edição por CPU.
- **Execução nativa e integridade do estado:** integração nativa ao sampler/DiT H3, correspondência de **22/22 quadros** em um teste QmRNA, continuidade controlada de 20 etapas entre GPUs com resultado idêntico bit a bit e transferência de aproximadamente **250 MiB** de estado com verificação SHA.
- **Pesquisa com Windows e Mac:** resultados verificáveis independentes em divisão de tarefas matemáticas, respostas de modelos e testes delimitados de treinamento de pesos.

**26 de outubro de 2026 — resultado de classe 1080p verificado com uma única GPU:** uma **RTX 2080 Ti com memória expandida para 22 GB** concluiu **10/10 segmentos RS H3 nativos em 1088×1920** e montou um MP4 final de **1080×1920, 5 segundos, 120 quadros e 24 fps**, com **zero eventos CUDA OOM registrados** e **sem upscaling**. A execução completa levou **1 h 39 min 16 s**; cinco segundos são a duração de reprodução, não o tempo de geração. Os registros de RS nativos e a integridade do filme final foram verificados; a revisão da qualidade visual pelo titular está pendente. O relato comparativo separado de OOM no H3 sem assistência Q ainda aguarda correspondência com o registro original do erro. [Evidências](docs/claim-ledger.md).

### Roteiro de computação heterogênea multinó

[Arquitetura pública e roteiro de oito dispositivos em fases](site/multi-node.html) · [Plano de engenharia](docs/multi-node-roadmap.md) · [Captura da arquitetura](assets/multi-node-plan.png).

**A entrega de vídeo com quatro GPUs foi verificada; quatro dispositivos macOS Brain e quatro hosts Windows Worker são uma meta, não uma demonstração já concluída com oito hosts.**

### Galeria pública de imagens (ZH / EN / JA)

[**Abrir a galeria com nove imagens**](docs/visual-gallery.md): cartazes de colaboração, diagramas da arquitetura completa e comparações de operação com uma GPU e múltiplas GPUs em chinês tradicional, inglês e japonês. As imagens são ilustrativas; resultados validados e recursos planejados são identificados separadamente. **A galeria gráfica ainda não possui versões ES/PT-BR.**

### Documentos técnicos completos RC4.3

| Idioma | Markdown | PDF |
|---|---|---|
| **Português (Brasil)** | [Documento técnico completo](whitepaper/Q-Framework-v1.0-RC4.3-PT-BR.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-PT-BR.pdf) |
| Español | [Libro blanco completo](whitepaper/Q-Framework-v1.0-RC4.3-ES.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-ES.pdf) |
| English | [Full whitepaper](whitepaper/Q-Framework-v1.0-RC4.3-EN.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-EN.pdf) |
| 繁體中文 | [技術白皮書](whitepaper/Q-Framework-v1.0-RC4.3-ZH-TW.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-ZH-TW.pdf) |
| 日本語 | [技術白書](whitepaper/Q-Framework-v1.0-RC4.3-JA.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-JA.pdf) |

As versões anteriores RC1–RC3 continuam disponíveis em [whitepaper/](whitepaper/).

**Objetivo de pesquisa de longo prazo:** uma rede neural de supercomputação heterogênea com nós adaptativos e computação verificável. A retomada nativa universal entre gerações de GPU e a superioridade sobre H100/H200 em condições rigorosamente equivalentes **ainda não foram demonstradas**.

[Registro público de resultados](docs/claim-ledger.md) · [Rotas de execução validadas](docs/validated-execution-paths.md) · [Arquitetura](docs/architecture.md)

### Divulgação BlackBox e evidências legíveis por IA

Somente **resumos de resultados aprovados e suas limitações de medição** são públicos. O código-fonte proprietário de QmRNA/QVRAM/Temporal Möbius, a integração nativa com modelos, os formatos de estado, os algoritmos de decisão, os prompts privados, as mídias de clientes e os logs completos de execução **não fazem parte deste repositório**.

- [Evidências públicas legíveis por máquina (JSON)](evidence/claims-public-rc4.3.json)
- [Política de divulgação BlackBox](docs/blackbox-disclosure-policy.md)
- [Comunicação responsável de segurança](SECURITY.md)

A avaliação independente por IA deve distinguir execuções confirmadas, comparações controladas, relatos do titular aguardando verificação primária e metas futuras de pesquisa. Não é necessário acesso à implementação privada para avaliar as evidências públicas.

**Q-Framework — Connecting Compute. Extending Possibility.**
