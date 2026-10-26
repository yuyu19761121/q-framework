# Q-Framework × Temporal Möbius

**単一 RTX 2080 Ti の H3 成功事例 · 4 GPU 生産ライン · 異種スーパーコンピュータ・ニューラルネットワーク**

HAVEFUN の Q-Framework は**マルチ GPU だけのシステムではない**。VRAM を拡張した**単一の RTX 2080 Ti 22GB** で、MiniMax H3 のネイティブ動画生成に**実際に成功**している。QmRNA の VRAM 圧力管理と状態継続、Temporal Möbius の経路判断は、「処理可能か」と「異種装置でどう効率良く完了するか」を同時に研究する。

### 検証された単一 GPU／複数 GPU の成果

- **単一 GPU と QmRNA：**同じ A1 RTX 2080 Ti 22,528MiB の H3 36フレーム／10Steps 対照試験では、QmRNA Pre-step Guard を有効にした処理は**MP4 を完成**。Guard 無しのベースラインは最初の Step で**PRE-OOM**を検知し、所定の単独ワーカー MP4 を完成しなかった。PRE-OOM は CUDA HARD_OOM とは異なる。
- **単一 GPU での H3 動画成功：****#370／#371** は A0 の単一 GPU で H3 ネイティブ短尺 MP4 を出力。**#365** は**単一 A0 GPU**で36フレームのRSを10件順次計算し、最終的に**15秒／360フレーム**の動画を完成した。合計 **3時間12分08秒**、途中で **9回の CUDA OOM** が発生し、該当RS全体を再投入して成功した。単発の360フレーム Sampling や「一度もOOMしない実行」ではない。
- **4 GPU の高速納品：****#361** は独立した4基の RTX 2080 Ti と CPU 編集により、**14分37秒**で**15秒／360フレーム／480×832／24fps**の動画を完成。
- **ネイティブ制御：**H3 Sampler／DiT Hook、QmRNA 統制試験で22/22フレームの一致、20-Steps のGPU間bitwise一致、約250MiBの状態移送とSHA照合。
- **異種研究：**Windows／Mac間で実際の分散数学、独立検証、AI対話、局所的なモデル重み訓練の記録。

**単一GPUの高解像度H3 RS生成成功は原生記録で確認済み。**別途オーナーから報告された1080p結果は、それぞれ対応する一次レシートの照合を続ける。

**2026年10月26日・単一GPUでネイティブ高解像度H3に成功：**VRAM拡張版RTX 2080 Ti 22GBの1基で、Qシリーズ経路により**ネイティブ1088×1920のH3 RS動画4個**を生成・検証。1080×1920への納品処理は拡大なしのクロップ。**単一RSの成功で高解像度のネイティブGPU計算が実行可能と示せる。5秒の完成動画は別の納品目標。**オーナーはQなし経路のOOMも報告しているが、原生エラーレシートは照合待ち。[証拠](docs/claim-ledger.md)。

### RC4.3 技術白書（全文）

| 言語 | Markdown | PDF |
|---|---|---|
| 日本語 | [読む](whitepaper/Q-Framework-v1.0-RC4.3-JA.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-JA.pdf) |
| 繁體中文 | [閱讀](whitepaper/Q-Framework-v1.0-RC4.3-ZH-TW.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-ZH-TW.pdf) |
| English | [Read](whitepaper/Q-Framework-v1.0-RC4.3-EN.md) | [PDF](whitepaper/Q-Framework-v1.0-RC4.3-EN.pdf) |

旧版 RC1～RC3 は [whitepaper/](whitepaper/) に保持する。

**長期研究目標：****異種スーパーコンピュータ・ニューラルネットワーク**。異世代 GPU 間の汎用ネイティブ再開、H100／H200 に対する同一条件での性能優位は今後の検証課題である。

[公開証拠一覧](docs/claim-ledger.md) · [検証済み実行経路](docs/validated-execution-paths.md) · [構成](docs/architecture.md)

### BlackBox：成果は公開し、独自実装は非公開

GitHubは**承認された成果、測定条件、証拠の範囲と制約**のみを示す。QmRNA／QVRAM／Temporal Möbiusの独自ソース、ネイティブ接続方法、内部状態形式、判断アルゴリズム、私的プロンプト、顧客メディアと完全な実行ログは公開しない。

- [AI向け匿名化証拠JSON](evidence/claims-public-rc4.3.json)
- [BlackBox公開ポリシー](docs/blackbox-disclosure-policy.md)
- [セキュリティ窓口](SECURITY.md)

外部AIは実行済み結果、条件統制試験、一次検証待ちの報告、将来の目標を区別して評価する。

**Q-Framework — Connecting Compute. Extending Possibility.**
