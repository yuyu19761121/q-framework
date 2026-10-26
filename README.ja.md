# Q-Framework × Temporal Möbius

**単一 RTX 2080 Ti の H3 成功事例 · 4 GPU 生産ライン · 異種スーパーコンピュータ・ニューラルネットワーク**

HAVEFUN の Q-Framework は**マルチ GPU だけのシステムではない**。VRAM を拡張した**単一の RTX 2080 Ti 22GB** で、MiniMax H3 のネイティブ動画生成に**実際に成功**している。QmRNA の VRAM 圧力管理と状態継続、Temporal Möbius の経路判断は、「処理可能か」と「異種装置でどう効率良く完了するか」を同時に研究する。

### 検証された単一 GPU／複数 GPU の成果

- **最新：単一GPUで1080p完成動画：**RTX 2080 Ti 22GB×1でネイティブRS10/10成功、1080×1920／5秒／120フレームを納品。アップスケールなし、該当実行のCUDA OOM記録なし。

- **単一 GPU と QmRNA：**同じ A1 RTX 2080 Ti 22,528MiB の H3 36フレーム／10Steps 対照試験では、QmRNA Pre-step Guard を有効にした処理は**MP4 を完成**。Guard 無しのベースラインは最初の Step で**PRE-OOM**を検知し、所定の単独ワーカー MP4 を完成しなかった。PRE-OOM は CUDA HARD_OOM とは異なる。
- **単一 GPU での H3 動画成功：****#370／#371** は A0 の単一 GPU で H3 ネイティブ短尺 MP4 を出力。**#365** は**単一 A0 GPU**で36フレームのRSを10件順次計算し、最終的に**15秒／360フレーム**の動画を完成した。合計 **3時間12分08秒**、途中で **9回の CUDA OOM** が発生し、該当RS全体を再投入して成功した。単発の360フレーム Sampling や「一度もOOMしない実行」ではない。
- **4 GPU の高速納品：****#361** は独立した4基の RTX 2080 Ti と CPU 編集により、**14分37秒**で**15秒／360フレーム／480×832／24fps**の動画を完成。
- **ネイティブ制御：**H3 Sampler／DiT Hook、QmRNA 統制試験で22/22フレームの一致、20-Steps のGPU間bitwise一致、約250MiBの状態移送とSHA照合。
- **異種研究：**Windows／Mac間で実際の分散数学、独立検証、AI対話、局所的なモデル重み訓練の記録。

**2026年10月26日・単一GPUの1080p完成動画に成功：**VRAM拡張版 **RTX 2080 Ti 22GB×1** でネイティブ **1088×1920 H3 RSを10/10個**生成。クロップとトリミングのみでアップスケールせず、**1080×1920／5秒／120フレーム／24fps MP4**を完成。CUDA OOM記録 **0回**、総所要時間 **1時間39分16秒**（5秒は映像の再生時間）。RSと完成映像の技術レシートは検証済み、画質はオーナー確認待ち。QなしH3のOOM対照は元エラーとの照合待ち。[証拠](docs/claim-ledger.md)。

### マルチノード異種計算計画

[公開構成ページ](site/multi-node.html) · [工程計画](docs/multi-node-roadmap.md) · [実際のページ画像](assets/multi-node-plan.png)。**4 GPU の動画生成は実証済み。macOS Brain 4台＋Windows Worker 4台の8デバイスは今後の目標。**

### 日本語・英語・繁體中文 画像ギャラリー

[**9枚の公開画像を見る**](docs/visual-gallery.md) — 参加募集、システム構成、単一GPU／複数GPU比較の3言語版。実証済みの成果と開発中の計画は区別しています。

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
