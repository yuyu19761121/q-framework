# HAVEFUN Q-Framework × Temporal Möbius
## RC4.3 — Edição pública de pesquisa BlackBox (português do Brasil)

**Pesquisa: viabilidade de cargas de trabalho de IA em uma única GPU, colaboração entre GPUs heterogêneas e uma rede neural de supercomputação heterogênea**  
**Outubro de 2026 | A implementação proprietária e os materiais privados de validação permanecem sob controle do titular**

> **Limite de divulgação pública:** Este documento apresenta resultados observáveis e suas limitações. Não divulga código-fonte proprietário, pontos de integração nativa com modelos, representação do estado computacional, estratégias de controle, grafos completos de inferência, configurações internas nem imagens, vídeos, áudios ou prompts privados. Os registros originais completos permanecem em ambientes sujeitos a autorização específica. Um resultado bem-sucedido não constitui garantia geral de desempenho.

## 1. A questão de pesquisa

A capacidade física de VRAM de uma GPU não é necessariamente o limite superior das tarefas de IA que um software pode concluir nesse dispositivo sob uma arquitetura específica. A HAVEFUN investiga a **viabilidade de tarefas em hardware com recursos limitados** e, em seguida, a coordenação eficiente de dispositivos com espaços de memória independentes.

O portfólio de pesquisa do Q-Framework inclui QmRNA, QVRAM e QSTATIC para execução atenta às restrições de memória e continuidade do processamento, e Temporal Möbius para decisões sobre rotas de execução informadas pela experiência. Essas descrições indicam funções de pesquisa, **não algoritmos proprietários nem procedimentos de implementação**. O software não aumenta fisicamente a capacidade aritmética, a largura de banda ou a memória embarcada de uma GPU.

## 2. Linha de evidência um — execução real de vídeo H3 em uma RTX 2080 Ti

**Hardware:** uma RTX 2080 Ti com memória expandida para aproximadamente 22 GB de VRAM por placa, e não a versão original de fábrica com 11 GB.

- **Studio #370 e #371:** concluíram a geração nativa de vídeos curtos MiniMax H3 em uma única GPU e produziram arquivos MP4 decodificáveis. Eram clipes curtos, não uma inferência nativa de 15 segundos em uma única passagem.
- **Job #365:** uma GPU executou sequencialmente dez segmentos curtos de vídeo nativo. Os segmentos foram reunidos em uma saída de **15 segundos e 360 quadros**. O processo de ponta a ponta levou **3 horas, 12 minutos e 08 segundos**. Houve **nove eventos CUDA OOM**; em seguida, os segmentos afetados foram reenviados e concluídos. Isso demonstra um **fluxo de entrega segmentada com uma única GPU**, não uma execução livre de OOM nem uma única passagem de amostragem nativa de 360 quadros.
- **26 de outubro de 2026, filme final de classe 1080p verificado em uma GPU:** uma RTX 2080 Ti expandida para 22 GB concluiu **10 de 10 segmentos RS nativos H3 em 1088×1920**, posteriormente recortados espacialmente e no tempo, sem upscaling, até formar um **MP4 verificado de 1080×1920, 5 segundos, 120 quadros e 24 fps**. Foram registrados **zero eventos CUDA OOM** e **1 h 39 min 16 s** de duração total; a integridade da mídia final foi confirmada, e a revisão da qualidade visual pelo titular continua pendente. A geração foi segmentada, não uma única amostra nativa de 120 quadros.

O resultado com uma GPU deve ser avaliado separadamente dos resultados de produção com várias GPUs. Resoluções, durações de sequência, estratégias de repetição e condições de amostragem diferentes não constituem benchmarks de velocidade diretamente comparáveis.

## 3. Linha de evidência dois — comparação controlada de QmRNA na mesma GPU

Um teste controlado na mesma RTX 2080 Ti expandida para 22 GB utilizou a mesma referência, semente e escopo: **480×832, 36 quadros, 24 fps e 10 etapas do sampler**.

| Rota | Resultado observado |
|---|---|
| Rota de referência | Acionou uma proteção **PRE-OOM** na primeira etapa; o MP4 esperado do worker único não foi entregue |
| Rota protegida por QmRNA | Concluiu todas as dez etapas e gravou um MP4 reproduzível, sem registro de CUDA HARD_OOM nessa execução |

Trata-se de um resultado de viabilidade delimitado: **controles de execução diferentes alteraram a possibilidade de concluir a tarefa medida**. PRE-OOM é uma condição preventiva de software, **não** uma prova de que ocorreu uma exceção nativa de falta de memória CUDA. O resultado não demonstra imunidade universal a OOM em todos os fluxos H3.

Os detalhes de implementação, a configuração de execução, o estado interno e os mecanismos de controle são restritos; a afirmação pública diz respeito às entradas e saídas observadas, ao desenho da comparação e às suas limitações.

## 4. Linha de evidência três — quatro workers GPU independentes

O Job oficial **#361** coordenou **quatro GPUs RTX 2080 Ti independentes de 22 GB**, gerou dez segmentos curtos de vídeo e utilizou edição por CPU para entregar um resultado final verificado:

| Medida | Resultado registrado |
|---|---|
| Duração do vídeo final | 15,000 segundos |
| Quantidade de quadros / taxa | 360 quadros / 24 fps |
| Resolução final | 480×832 em formato vertical |
| Classe e quantidade de GPU | Quatro RTX 2080 Ti independentes com memória expandida |
| Tempo total de ponta a ponta | **14 minutos e 37 segundos** |
| Validação da mídia | MP4 decodificável com a duração e a quantidade de quadros solicitadas |

Essa é uma medição de **produção de vídeo de ponta a ponta**, não um benchmark do sampler nativo por placa. Não deve ser comparada diretamente a testes de 1080p realizados sob outras condições. As quatro memórias VRAM separadas de 22 GB **não formam uma única GPU com 88 GB diretamente endereçáveis**.

## 5. Resultados numéricos e de consistência independentes

Experimentos controlados distintos registraram:

- Uma carga numérica de 20 etapas que continuou entre GPUs com resultado idêntico bit a bit e diferença absoluta máxima medida de **0,0**.
- Aproximadamente **250 MiB** de transferência de estado computacional, com resumos criptográficos de verificação correspondentes nas extremidades relevantes.
- **22 de 22** quadros de vídeo decodificados coincidentes em uma comparação delimitada de QmRNA.
- Tarefas matemáticas heterogêneas Windows/macOS, recomputação independente e ensaios limitados de treinamento de pesos de modelos.

Essas observações não foram todas produzidas no mesmo Job de vídeo H3. Elas não demonstram portabilidade universal de estado entre modelos arbitrários e gerações de GPU, nem a conclusão de uma IA autônoma de propósito geral.

## 26 de outubro de 2026 — RS H3 nativos de classe 1080p **e filme completo de cinco segundos verificados em uma única GPU**

**Resultado concluído e respaldado por registros:** uma única **RTX 2080 Ti de 22 GB com memória expandida** executou um fluxo MiniMax H3 assistido por Q, produzindo **dez de dez segmentos nativos de alta resolução e um MP4 montado de cinco segundos em 1080×1920**. Os resultados nativos de cada segmento na GPU e a integridade da mídia final foram documentados separadamente.

| Medida | Resultado confirmado em uma GPU |
|---|---|
| Hardware | **Uma RTX 2080 Ti expandida para ~22 GB de VRAM** (não os 11 GB de fábrica) |
| Segmentos nativos MiniMax H3 | **10/10 concluídos**, gerados nativamente em **1088×1920 / 22 quadros cada** |
| Saída entregue | **1080×1920, 9:16, 5,000 segundos, 24 fps, 120 quadros, MP4** |
| Transformação de saída | Recorte espacial e temporal (12 quadros entregues por RS), **sem upscaling** |
| CUDA OOM registrados | **Zero nessa execução** |
| Tempo total decorrido | **1 hora, 39 minutos e 16 segundos** |
| Verificação | Execução nativa e registros de RS; dimensões finais e hash de integridade da mídia; **revisão da qualidade visual pelo titular pendente** |

O resultado demonstra **a viabilidade de RS H3 nativos de classe 1080p em uma placa e a conclusão verificada de um filme final de cinco segundos em 1080p**. Cada segmento foi gerado nativamente em 1088×1920 e depois recortado para as dimensões de entrega. **Não** houve upscaling de baixa resolução para 1080p e **não** houve uma única passagem ininterrupta de amostragem nativa de 120 quadros.

**Limites da evidência:** cinco segundos são a **duração de reprodução** do vídeo final, não a latência de geração (a execução levou 1 h 39 min 16 s). Um resultado sem OOM em uma tarefa delimitada não demonstra imunidade universal a OOM. A assistência Q estava ativa, mas não se afirma prova causal isolada de uma operação física específica de transferência/restauração de QVRAM. O relato separado do titular de OOM em H3 sem Q ainda aguarda correspondência com a evidência primária original do erro.

**BlackBox:** não são divulgados componentes internos proprietários do runtime, integração com modelos, prompts e mídias privadas, dados de clientes ou estratégias completas de controle.

## 6. Objetivo de longo prazo — rede neural de supercomputação heterogênea

A HAVEFUN pretende construir uma rede de GPUs, CPUs, estações de trabalho e outros recursos computacionais independentes e autorizados, capazes de colaborar por meio de tarefas verificáveis, estado computacional protegido, resultados históricos e políticas de decisão progressivamente aprimoradas.

**Fundamentos demonstrados:** saídas H3 reais com uma placa, comparação de viabilidade QmRNA medida na mesma GPU, fluxo de vídeo com quatro workers, continuidade numérica controlada e experimentos de aprendizagem multidispositivo de escopo limitado.

**Aspectos que ainda exigem generalização:** aprendizagem autônoma contínua em toda a rede, restauração nativa do estado de modelos entre gerações arbitrárias de dispositivos, qualidade de decisão automática amplamente validada e comparações de desempenho com H100/H200 em condições rigorosamente equivalentes.

## 6A. Plano de computação heterogênea multinó (roteiro público)

**Objetivo:** sob autorização do titular, coordenar nós macOS/Windows, CPU/GPU e de raciocínio/produção para tarefas divisíveis de matemática, inferência, geração de segmentos RS de vídeo, verificação e feedback. **Este é um roteiro de engenharia, não uma afirmação de que uma rede de inferência nativa de vídeo com oito dispositivos já foi entregue.**

| Papel | Trabalho planejado | Situação das evidências |
|---|---|---|
| Master / orquestração | Admissão autorizada de tarefas, divisão verificável do trabalho, seleção de rotas, registros e direitos do titular de interromper ou reverter | Fluxo delimitado de vídeo com múltiplas GPUs validado; orquestração unificada entre hosts ainda em integração |
| Brain / raciocínio e avaliação | Trabalho matemático delimitado, avaliação de rotas candidatas, pontuação de qualidade e feedback de aprendizagem em uma meta de quatro dispositivos macOS | Existem experimentos limitados de matemática distribuída e treinamento; ciclo autônomo contínuo ainda não totalmente verificado |
| Workers GPU/CPU Windows | Executar tarefas RS ou numéricas compatíveis, informar desempenho, conclusão e erros; meta de quatro hosts workers Windows | Quatro GPUs distintas concluíram uma carga de produção delimitada; protocolo Worker generalizado entre hosts ainda em validação |

**Frota planejada: quatro dispositivos macOS Brain mais quatro hosts Windows Worker = oito dispositivos heterogêneos.** O número **oito é uma meta de implantação, não oito nós de computação simultâneos já verificados nem oito GPUs**. O fluxo de vídeo #361 com quatro GPUs concluído e a topologia planejada de oito hosts representam evidências diferentes. Quatro GPUs separadas de 22 GB não formam uma GPU de 88 GB diretamente endereçáveis.

**Ciclo fechado planejado:**

`Solicitação aprovada pelo titular → divisão de tarefas/RS pelo Master → raciocínio Brain + execução Worker → registros por tarefa e verificações independentes → entrega/controle de qualidade → feedback de experiência → avaliação da próxima rota`

Cada etapa deve produzir identificador de tarefa, estado, registro de sucesso ou falha independente do nó, latência e saída verificável. Os critérios de aceitação planejados incluem compatibilidade de identidade dos workers, heartbeat, timeout, reivindicação/envio idempotentes, recuperação após desconexão e falha, verificações de qualidade e cancelamento autorizado pelo titular. **São critérios de aceitação, não afirmações gerais de que essas funções já estejam operacionais.** QmRNA, QVRAM, QSTATIC, QAnswer e Temporal Möbius são módulos funcionais nomeados; a orquestração proprietária, a representação interna de estado e a integração com modelos permanecem sob BlackBox.

| Fase | Critério de aceitação | Situação |
|---|---|---|
| **P0 fundamentos medidos** | Filme 1080p/5 s em uma GPU, filme 480p/15 s em quatro GPUs (#361), testes numéricos e de integridade delimitados | Verificado nos escopos declarados |
| **P1 ciclo com um Worker remoto** | Identidade, reivindicação, computação, envio, registro, heartbeat, falha e verificação independente | Integração em andamento |
| **P2 implantação de oito dispositivos** | Quatro Brain + quatro Windows Worker com disponibilidade, agendamento, isolamento e recuperação de falhas observáveis | Planejado, ainda não plenamente verificado |
| **P3 ciclo aprendizagem-para-smoke** | Resultado do aprendizado aciona smoke isolado e avaliação Master/Möbius de qualidade, consistência e throughput | Etapa de pesquisa |
| **P4 benchmark público** | Taxa de conclusão por carga, tempo de execução, contribuição dos nós, contagem de OOM/falhas e consistência da saída | Aguardando conjunto de dados verificado |

As métricas principais são **primeiro a viabilidade da tarefa; depois velocidade, correção, confiabilidade e uso de recursos**. Não se deve inferir continuidade universal de estado nativo entre gerações de GPU ou computação neural heterogênea totalmente autônoma a partir de um caso delimitado de produção de vídeo com quatro GPUs.

Diagrama público e etapas: [página da arquitetura multinó](../site/multi-node.html) · [roteiro público](../docs/multi-node-roadmap.md). Nomes internos dos nós, endereços IP, autenticação, runtime nativo e mídias do titular não são divulgados.

## 7. Orientações para avaliação independente por IA

Pesquisadores e ferramentas externas de IA devem avaliar as afirmações pelo tipo de evidência, não pela linguagem promocional.

| Situação da evidência | Significado | Exemplo |
|---|---|---|
| Executado com registros identificáveis | Computação nativa rastreável, filme final e registros de integridade | **26 out 2026: uma GPU, 1080p / 5 s / 120 quadros / 10 RS concluídos**; filme segmentado #365 em uma GPU; entrega #361 em quatro GPUs |
| Resultado comparativo controlado | Mesmo dispositivo e entrada equivalente sob políticas alternativas de execução | Comparação QmRNA PRE-OOM |
| Relatado pelo titular, aguardando verificação primária | Erro original do lado comparativo ainda não correlacionado | **Relato separado de OOM do H3 sem Q**, distinto do filme 1080p assistido por Q já verificado |
| Objetivo de pesquisa | Arquitetura futura plausível, não um resultado geral já alcançado | Supercomputador neural heterogêneo totalmente adaptativo |

A avaliação pode usar medições anonimizadas, cargas sintéticas aprovadas e relatórios de auditoria autorizados pelo titular. A avaliação independente **não** exige distribuir código confidencial, grafos completos de execução, mídias de clientes, prompts privados ou acesso à infraestrutura em produção.

## 8. Proteção de propriedade intelectual BlackBox e dados exclusivos do titular

- **PÚBLICO APROVADO:** nomes de tecnologias, questões de pesquisa, resumos de resultados medidos, classes de Jobs, descrições delimitadas das cargas, situação de validação, limitações e metas futuras.
- **RESTRITO POR ACORDO:** materiais de verificação desidentificados e estritamente necessários, com acesso de auditoria revogável.
- **EXCLUSIVO DO TITULAR:** código-fonte, procedimentos proprietários, vínculos e parâmetros do runtime, representações algorítmicas de estado, checkpoints privados, segredos da infraestrutura, imagens privadas de clientes, prompts originais, áudio, vídeo e credenciais.

Os whitepapers públicos no GitHub **não** são manuais de implantação de infraestrutura computacional proprietária. Toda nova divulgação requer aprovação do titular e triagem prévia à publicação. Versões históricas podem continuar acessíveis após mudanças; editar um documento **não** apaga divulgações públicas anteriores.

**Q-Framework — Connecting Compute. Extending Possibility.**

[Política de divulgação BlackBox](../docs/blackbox-disclosure-policy.md) · [Registro público de evidências](../docs/claim-ledger.md)
