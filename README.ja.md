# Q-Framework

**異種混在型AI基盤のための計算状態仮想化・適応型フロー制御アーキテクチャ**

Q-Framework は、長時間の生成AIワークロードを「GPUメモリが不足したら終了する処理」ではなく、観測・制御・停止・保存・復元・移動が可能な計算状態として扱うための実験的コンピューティング基盤です。

> **本リポジトリは実際に稼働しているシステムを記録しますが、プロダクション用の中核エンジンは公開しません。**

**Version:** Development & Validation Whitepaper v1.0 RC1  
**Snapshot:** 2026-10-07

[English](README.md) · [繁體中文](README.zh-TW.md)

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
