# Q-Framework

**異種混在型AI基盤のための計算状態仮想化・適応型フロー制御アーキテクチャ**

Q-Framework は、長時間の生成AIワークロードを「GPUメモリが不足したら終了する処理」ではなく、観測・制御・停止・保存・復元・移動が可能な計算状態として扱うための実験的コンピューティング基盤です。

> **本リポジトリは実際に稼働しているシステムを記録しますが、プロダクション用の中核エンジンは公開しません。**

**Version:** Evidence Whitepaper v1.0 RC3  
**Snapshot:** 2026-10-07

[English](README.md) · [繁體中文](README.zh-TW.md)

## 🔴 ライブ計算ストリーム

**[Q-Framework Live Compute Stream を開く](https://yuyu19761121.github.io/q-framework/)**

現在実行中の Job、4 GPU の branch 状態、GPU / VRAM 使用状況、QmRNA / QSTATE の進行、production node の heartbeat、実行ステータスをリアルタイムで確認できます。これは静的なデモではなく、継続更新される公開 live telemetry です。


## ホワイトペーパー PDF

**[English PDF](whitepaper/Q-Framework-v1.0-RC2-EN.pdf)** · **[繁體中文 PDF](whitepaper/Q-Framework-v1.0-RC2-ZH-TW.pdf)** · **[日本語 PDF](whitepaper/Q-Framework-v1.0-RC2-JA.pdf)**

## Sponsor Q-Framework

**[Sponsorship Overview](SPONSORSHIP.md)** · **[繁體中文贊助說明](SPONSORSHIP.zh-TW.md)** · **[Sponsorship Prospectus PDF](sponsorship/Q-Framework-Sponsorship-Prospectus-v1.0-ZH-TW.pdf)**

Funding, hardware, cloud credits and research collaboration can expand Q-Framework validation capacity while the production engine remains proprietary.

## 公開している概念

- **QmRNA** — runtime telemetry / control plane
- **Qvram** — persistent compute state / checkpoint / residency layer
- **Qsearch** — state and working-set retrieval
- **Qanswer** — heterogeneous CPU/GPU orchestration
- **QSTATIC** — precomputed visual/static-state source layer
- **QSTATE / QBLOCK / QLINEAGE / QREV** — state, block, lineage, revision primitives

## Evidence policy

Q-Framework は「構想」「実装」「部分的検証」「実証済み」を分離して記録します。

現在公開可能な実証内容には、クロスGPU状態転送、CPU/RAM を介した continuation、lineage/checkpoint 管理、H3 model-forward 内で動作する QmRNA candidate、exact FFN token chunking、CPU-only global streamed attention の数値検証などが含まれます。

一方、22GB GPU 上での 15秒 full-length H3 の最終 production PASS、完全な streamed-QKV data-plane、汎用 working-set virtualization は引き続き検証中です。

## Disclosure policy

**Open Specification · Open Evidence · Open Reference Interfaces · Closed Production Engine**

本リポジトリでは、実運用の pressure scoring、page/residency selection、eviction/prefetch、restore sequencing、scheduler weight、Qsearch ranking、production streamed-QKV、資格情報・内部ネットワーク情報を公開しません。
\n\n## Validation Evidence\n\n[Validated Execution Paths](docs/validated-execution-paths.md)\n

## RC3 公開版

最新のEvidence Whitepaper（日本語Markdown）：[Q-Framework-v1.0-RC3-JA.md](whitepaper/Q-Framework-v1.0-RC3-JA.md)

RC3では、実測証拠を公開しながら、production mechanismをブラックボックスとして維持します。
