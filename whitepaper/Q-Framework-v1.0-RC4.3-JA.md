# Q-Framework × Temporal Möbius
## 異種 AI 計算の継続、ネイティブ生成、異種スーパーコンピュータ・ニューラルネットワーク技術白書

**HAVEFUN AI Studio 技術研究開発**  
**Q-Framework v1.0 RC4.3｜2026年10月25日｜日本語版**  
**編集基準：**RC4.3 繁体字中国語・統合レビュー版。RC4.2 の技術実績を保持し、単一 GPU の検証結果を追加。

> **証拠の取り扱い：**本書は、ネイティブ実行記録、条件を統制した比較試験、オーナーから報告されたが一次証跡の照合が未完了の成果、今後の研究目標を明確に区別する。異なるジョブ、解像度、GPU 数、フレーム数、ステップ数、シード、リトライ方針を同一条件の性能比較に流用しない。「RTX 2080 Ti 22GB」は、**VRAM を拡張した 22,528 MiB のカード**を指し、純正の 11GB 版ではない。

## 要旨：まず「単一 GPU で実行可能」を示し、その上で「複数 GPU で高速化」を検証する

HAVEFUN の Q-Framework は、4 基の GPU に作業を振り分けるだけのスケジューラではない。Foundation-00 の埋め込み型 Runtime Agent、MiniMax H3 の Sampler／DiT／Attention Hook、QmRNA による実行・VRAM 圧力管理、CPU／GPU 間の計算状態移送、Render Segment（RS）の時間分割、Temporal Möbius の数理的経路判断を組み合わせた技術体系である。長期目標は**異種スーパーコンピュータ・ニューラルネットワーク**の構築である。世代、性能、OS の異なる装置を、検証可能なタスク、再利用可能な計算状態、実行結果に基づく判断の更新によって協調させる。

現時点の技術成果には、**互いに異なる二つの実証軸**がある。

1. **単一 GPU の実行可能性。**VRAM を拡張した RTX 2080 Ti 22GB の A0／A1 環境で、MiniMax H3 のネイティブ動画生成を実際に実行した。Studio **#370／#371** は再生可能な短尺 MP4 を生成し、別途 A0 で **48 フレーム、24fps、14 Steps** の H3 実行が完了した。ジョブ **#365** は、**単一の A0** で 36 フレームの RS を10件順次処理し、最終的に **15 秒、360 フレーム** の MP4 を納品した。総時間は **3 時間 12 分 08 秒**。ネイティブ History には **9 回の CUDA OOM** があり、該当 RS 全体を新しい Prompt ID で再投入して成功した。つまり「単一 GPU による複数 RS の最終動画完成」であり、「360 フレームを一度にサンプリングした」「OOM が一度も起きなかった」という意味ではない。
2. **4 GPU の納品効率。**正式ジョブ **#361** では、独立した4基の RTX 2080 Ti 22GB（A0／A1／B0／B1）が H3 の10 RSを処理し、CPU が9か所の継ぎ目を編集した。出力は **15.000 秒、360 フレーム、24fps、480×832**、エンドツーエンドで **14 分 37 秒**。ネイティブ QmRNA Gate の接続は確認されているが、このジョブで QFREEZE や完全な QVRAM オフロード／リストアが発火したと推定することはできない。

特に意味のある**同一 GPU の対照試験**が 2026年10月4日に実施された。同じ A1 GPU、同じ Static 参照・シード、480×832、36 フレーム、24fps、10 Steps という設定で、**QmRNA Guard を使わないベースライン**は Step 1 で **PRE-OOM** 救済条件を検出し、所定の単独ワーカー MP4 を完成できなかった。一方 **QmRNA Pre-step Guard** を有効にした経路ではキャッシュを回収し、10 Steps を完了して MP4 を出力した。**PRE-OOM は事前保護条件であり、CUDA HARD_OOM の発生そのものではない。**この比較は、測定された負荷条件における「単一 GPU の実行可能性の違い」を示す。

オーナーからは**単一 GPU で H3 の 1080p 実行を完了した**との報告もある。本版ではこれを**達成報告／一次実行レシート未照合**として保持する。今後初めて着手する目標とは記さないが、第三者向けの定量主張に使う前に、ジョブ／Prompt ID、Sampler 本来の幅と高さ（後処理アップスケーリングとの区別）、フレーム数、時間、OOM History、成果物仕様、SHA を照合する必要がある。

### 代表的な実証結果

| 領域 | 実験・レシート | 結果と適用範囲 |
|---|---|---|
| GPU 間の計算継続 | 20 Steps：GPU0 の Step 1–10 → GPU1 の Step 11–20 | 対照と bitwise 一致、最大絶対差 0.0 |
| 計算状態の移送 | 約 250 MiB、GPU→CPU→SharedMemory／Bridge→GPU | 送信元・Bridge・転送先の SHA-256 が一致 |
| H3 ネイティブ制御 | QmRNA Static Carrier、DiT、Sampler Hook | Checkpoint 間隔の実変更、`QMRNA_DIT_ENTER/EXIT` |
| QmRNA 同一 Seed 比較 | 22 フレーム、同じ参照と Seed | デコード済み 22/22 フレーム一致、単回の Sampler 窓は 81→76 秒 |
| 単一 GPU の短尺動画 | #370／#371、A0 | 約 39 フレーム、16fps、2.437 秒の H3 MP4 |
| 単一 GPU の15秒納品 | #365、A0 | 36フレーム×10 RS、9回のCUDA OOM後にRS再実行、計3:12:08 |
| 4 GPU の正式納品 | #361、A0/A1/B0/B1 | 10 RS＋CPU 9継ぎ目、15秒／360フレーム、14:37 |
| 階層型メモリと停止・再開 | Q7 CUDA、QFREEZE の統制試験 | 32 MiB CUDA 実体の退避／再ロードと Pause／Resume |
| Windows／Mac 協調 | 4 Windows Ollama、Mac LAN Math | 実ノード対話、24/24 バッチの分散数値検証 |
| 重み学習 | Möbius MLP、DistilGPT2 部分更新 | それぞれ独立した重み更新記録 |

---

## 1. 技術的位置づけと基礎アーキテクチャ

### 1.1 GPU 数の増加より「計算の継続性」

従来の生成 AI ワークフローは、単一のモデル前向き計算、固定ワーカー、1基の GPU に常駐できる VRAM を実行単位とすることが多い。Q-Framework は、互換条件下で**計算状態**を識別、保存、ハッシュ照合、転送、復元、継続できるかを研究する。Temporal Möbius は依存関係、時間、利用可能な資源、過去の結果を数理的な経路選択に反映させる。

4基×22GB は総計約 **88GB の分散した物理 VRAM 資源**であって、**単一の連続した 88GB VRAM 空間ではない**。本研究の価値は、計算の分割・状態管理・時間軸の構成によって、従来の経路では完了困難な負荷を実行可能にし、分割可能な仕事の全体納品効率を高める点にある。

### 1.2 Foundation-00：Master と埋め込み Runtime Agent

Foundation-00 は、新しい4 GPU用 JSON や Studio の UI 制御より前に設計された基礎レイヤーである。Master が仕事・資源・方針を指示し、H3／ComfyUI 内の Runtime Agent が ModelPatcher、Sampler、Attention、DiT のネイティブ実行位置で制御を受け、検証可能なレシートを返す。

実装位置には `HFQmRNAGate`、`HFQmRNAStaticLoader`、`ModelPatcher.set_model_patch_replace`、`optimized_attention` および Sampler Hook が含まれる。#341 の GPU レシートには `gpu_model_gate_present=true`、`gpu_model_gate_match=true`、`gpu_workflow_receipt_verified=true` と記録されている。後発 UI の OFF 状態や Heartbeat 欠落だけを理由に、既存のネイティブ Q 系統が動作していなかったと判断してはならない。

### 1.3 実際の異種ノード構成

| レイヤー | 実体 | 確認済みの役割 |
|---|---|---|
| Studio／Owner | HAVEFUN AI Studio | 正式なジョブ指示、状態、成果物契約、納品 |
| Production Master | Windows YUYU3D | スケジューリング、RS レシート、CPU 編集、MP4 検証 |
| GPU Worker | Node A A0/A1、Node B B0/B1 | 独立した RTX 2080 Ti 22GB の H3 実行 |
| CPU／Bridge | QWorker、Compute Bridge | 分散数学、状態移送、SHA 照合、前後処理 |
| Windows Möbius Brain | YUYU3D、Node A/B、Utility03 | 独立 Ollama 応答、ノード間の会話 |
| Mac Möbius | iMac、M2、MacBook、追加 M1 | LAN 行列分割、独立再計算、MLP／LLM 学習実験 |

現状の異種性は OS、CPU／GPU、役割の違いで実証されている。**異なる GPU 世代間で任意の H3 状態を汎用的に再開する機能**は、なお研究課題である。

## 2. Q-Framework：Foundation-00 と Q01–Q19 の技術系譜

QMobius と Temporal Möbius、QMater と QMaster の歴史的な呼称は維持する。ただし名称の違いだけで独立した2系統の計算エンジンが実証されたと見なさない。

| 索引 | 技術資産 | 機能・ネイティブ証拠 |
|---|---|---|
| Foundation-00／Q13 | 埋め込み Runtime Agent | Master→ネイティブ Gate／Sampler／DiT→実行レシート |
| Q01 | QmRNA Gate | 制御信号を H3 に注入。#341 Gate の存在、適合、ワークフロー実行が確認済み |
| Q02 | QmRNA Flag Control | Job／Seed／RS 別のチェックポイント・VRAM圧力方針。10/3 に `checkpoint_every=2→1` |
| Q03 | QVRAM | GPU VRAM／CPU RAM／Bridge の階層化。250 MiB GPU間転送と独立した32 MiB CUDA退避試験 |
| Q04 | QSTATIC／Motion Static | 参照フレーム、アンカー、状態情報。Static Carrier、デコード22フレーム比較 |
| Q05 | QFREEZE | 保存可能な位置での停止と再開。B1の制御 CUDA Sampler Step 1→5 |
| Q06 | QAnswer／Finalizer | Checkpoint を Answer Packet として再利用。残り1 Stepのみを計算する統制実験 |
| Q07 | QSearch | Worker・結果・分岐・経路探索。4分岐完了記録 |
| Q08 | QRebuild | 保存状態の数値 Tensor を再構成。PyTorch 正確 Roundtrip |
| Q09 | QSTATE | Step、Seed、Tensor をハッシュ保存。Replica ACK、Bridgeアーカイブ |
| Q10 | Temporal Möbius／QMobius | 依存 DAG、資源・時間・リスクを考慮する候補経路判断 |
| Q11 | QMater／QMaster／RS | 映像時間を追跡可能な Render Segment に分割して実行 |
| Q12 | FaceOff | 人物 ID と顔品質の検証、特定 RS の再実行判断 |
| Q14 | Drip Feed | QKV／FFN の有界な分割実行。H3 ネイティブ `ffn_chunk=512` |
| Q15 | Sampler Hook | ネイティブ Callback／Sampler の制御インターフェース |
| Q16 | Master Message Transport | Job／Prompt／Worker／Event／ACK／Receipt の照合 |
| Q17 | CPU Frame Editor／PostEdit | CPU による継ぎ目編集、フレーム整合と MP4 検証 |
| Q18 | Mixed GPU／ノード間継続 | A0→B0 CUDA 継続、GPU間数値一致、4 GPU RS生産 |
| Q19 | Studio Q-Framework Controls | オーナー操作、ディスパッチと表示。UI有効化だけでは実体実行の証拠ではない |

派生コンポーネントには HF Compute Bridge／Motion Bridge、QWorker Lite、Streamed-QKV／Page Attention、QBLOCK／QLINEAGE／QREV、QBonus、Windows Möbius Brain、Mac Math Stream、Möbius Neural／LLM、Partner Node 認証、Network Map が含まれる。**インストール済み、ロード済み、ネイティブ実行済み、実測検証済み**は異なる段階である。

~~~text
Studio / Director → Foundation-00 Master → Temporal Möbius 経路判断
  → RS コンパイル・QSearch / 適格 Worker 選択
  → QmRNA Gate / QSTATIC / H3 ネイティブ GPU
  → RS / QSTATE レシート
  → CPU Frame Editor / FFmpeg
  → 動画の長さ・フレーム・FPS・SHA・納品検証
~~~

## 3. 計算状態の継続：Tensor から H3 へ

### 3.1 20 Steps の決定論的な GPU 間継続

統制試験では GPU0 が Step 1–10 を計算し、CPU／RAM に数値状態を保存した後、GPU1 が Step 11–20 を実行した。結果は直接20 Steps を実行した対照と**bitwise identical**で、`max_abs_diff=0.0`。単に Prompt や画像を渡すのではなく、実際の数値計算状態を引き継いでいる。

### 3.2 約 250 MiB の実データ移送

2026年9月28日、**262,144,000 bytes（約250 MiB）**を GPU0 VRAM → CPU RAM → Windows Named Shared Memory → HF Compute Bridge → GPU1 VRAM と移動させた。送信元、Bridge、転送先の SHA-256 は一致した。

`330674e23bf109a4f5e3983608ce118274373deae669e3d3bacee2f77639d5a6`

元の CUDA Tensor を削除すると割り当てメモリがゼロになった。これは検証したバイト列の移送・整合性の証明であり、任意のモデルから見える「単一の88GB VRAM」が実装された証明ではない。

### 3.3 H3 のネイティブ状態復元とホスト間継続

X1／Motion Bridge には H3 の `RESTORE`／`SAMPLER_RESUME` イベントがある。別の受控経路では B0 checkpoint → B1 restore → H3 動画出力まで到達した。10月17日の Q7 では A0 が真の CUDA `HF_SAMPLER_STATE_V1` を保存し、Bridgeの複製と SHA を検証した後、B0 が読み込み、次の CUDA Step を計算した。任意の GPU モデル・モデル世代への完全互換を示すものではない。

## 4. QmRNA：モデル内部の制御を実証する

### 4.1 Static Carrier と Sampler の設定変更

10月3日、PNG iTXt `HF_QMRNA` Carrier を別ノードへ送り、SHA一致を確認。A1 Runtime が `QMRNA_CARRIER_LOADED` を記録し、`checkpoint_every` が実際に2から1へ変更された。後続の checkpoint と `QMRNA_COMPLETE` も残っている。CPU信号→Carrier→ネイティブGPU→Sampler挙動という連鎖が確認された。

### 4.2 H3 DiT のネイティブ Hook

10月6日、`QMRNA_DIT_ENTER/EXIT` を実 H3 モデル実行中に観測。隠れ特徴幅5,376、シーケンス長36,988、FFN Chunk 512 が記録された。単なるダッシュボード上の状態ではない。

### 4.3 同一 Seed A/B の測定

| Sampler条件 | ベースライン | QmRNA | 単回の観測 |
|---|---:|---:|---|
| 8フレーム／4Steps／同Static・Seed | 約34秒 | 約30秒 | 約11.8%短縮 |
| 22フレーム／10Steps／同Static・Seed | 約81秒 | 約76秒 | 約6.2%短縮 |

22フレームについて MP4コンテナのSHAは異なるが、**デコード後22/22フレームのframemd5は一致**した。単回の比較であり、一般的な高速化率を保証しない。

### 4.4 PRE-OOM 前の VRAM 回収

強制 Guard のテストでは重い Step の前に残り VRAM **460–492MB**、キャッシュ回収後 **2,668MB**。22フレーム／10Stepsを完成させ、HARD_OOMは記録されなかった。キャッシュ削除と CUDA Tensor の真のオフロード／ロードは区別される。

### 4.5 Streamed-QKV の数値整合性

Online Softmax を用いる CPU 参考実装を 257 tokens ×4 heads ×32 head_dim で比較し、最大絶対誤差は約 **2.09×10⁻⁷～2.98×10⁻⁷**、評価した分割パターンは `allclose` を満たした。H3 のすべての設定で数値同一性が確認されたわけではない。

## 5. QFREEZE／QVRAM／QSTATE／QAnswer／QRebuild

2026年10月17日の Q7 等では、複数の**別個の統制試験**が成立した。

- **同一 GPU Pause／Resume：**B1 CUDA マイクロ Sampler は Step 1 に `HF_QFREEZE_PAUSED` を記録し、再開して Step 5 に到達。
- **CUDAメモリ実体の解放と再ロード：**8,388,608個の float32、**33,554,432 bytes／32MiB** の Tensor を GPU→CPU／Bridge→GPU と移動。CUDA allocation は **33,554,432→0→33,554,432**。SHAが一致し次のCUDA計算が完了した。
- **QSTATE：**真の Sampler 状態、二つの Replica ACK、Bridgeアーカイブ、Master による遠隔 SHA 照合。
- **CPU QAnswer／QRebuild：**PyTorch による計算と `torch.save/load` の正確な往復。
- **ホスト間計算継続：**A0からB0へ状態を運び、B0上で次のCUDAステップを実行。

これらの機能が存在することと、#361／#365の各ジョブ中にそれぞれの機能が発動したことは同義ではない。

## 6. MiniMax H3：4 GPU 動画生産ライン

Node A／B は各2基の RTX 2080 Ti 22GB を備え、YUYU3D が Master・CPU編集・納品を担う。

| Job／日付 | 処理経路 | 記録された成果 |
|---|---|---|
| #135／9月29日 | 4 GPU H3／Bridge／Rescue | 15.000秒／36fps／540フレームの動画とSHA |
| #243／10月4日 | 4 GPU の並列QRS | 17 QRS完了、動画公開 |
| #327／10月13日 | 4 GPU H3、7/7 RS | 10秒・1080×1920に設定、MP4取得可、エンドツーエンド約1:55:44 |
| #341／10月16日 | 元のQmRNA Gate、10/10 RS | ネイティブRS約11分18秒、Studio全体約34分18秒、OOMリトライあり |
| #344／10月17日 | Möbiusの二島RSルート | 10 RSと15秒／360フレームのMP4検証 |
| #360／10月19日 | 4 GPU 10 RS＋CPU 9継ぎ目 | 15秒／360フレーム、**15分01秒** |
| **#361／10月19日** | **4 GPU 10 RS＋CPU 9継ぎ目** | **15秒／360フレーム、14分37秒** |
| T195／10月21日 | 各RS固有のPrompt SHA×10 | 10 RS、15秒／360フレームの出力 |

### #361 Golden Baseline

台湾時間2026年10月19日 **23:07:24～23:22:01** の **877秒**。GPUによるRS生成は23:21:07に完了。CPU側は9か所の編集を42.609秒で終了し、`gpu_invoked=false` と記録。最終成果物は H.264、**480×832、24fps、360フレーム、15.000秒**、デコード検証 PASS。

SHA-256：

`a219bb7e78c0e4b0d74823c45d6b0458515583e351c785a686f5c56c424254d8`

近接する #360 の901秒より24秒（2.66%）短い。GPU単体の演算カーネルの速度比較ではなく、制作フロー全体の実績である。

10月23日には PostEdit V2 により #365 の既存10 RSを再使用し、**360/360フレーム、24fps**の動画を再編した。元の映像との SSIM は **0.984182**、音声トラックなしの成果物も検証された。GPUを使った生成部分の再計算なしでCPU編集が可能となった例である。

## 7. Studio の5種類の制作モードと追加モデル

2026年10月20日の Studio **#368～#372** は、それぞれネイティブ ComfyUI History と結果メディアを取得した。

| モード | Job・モデル・ノード |
|---|---|
| Text-to-Image | #368／SDXL／B1 |
| Image-to-Image | #369／SDXL／B1 |
| Text-to-Video | #370／MiniMax H3／A0 |
| Image-to-Video | #371／MiniMax H3／A0 |
| Video-to-Video | #372／Wan VACE 1.3B／A0 |

#370／#371は**約39フレーム／16fps／2.437秒**のネイティブ短尺動画であり、15秒の単発サンプリングと表現しない。後続実験にはQwen-Image-2512 FP8、Qwen-Image-Edit-2511 FP8、A0上のMiniMax H3 **480×832／48フレーム／24fps／14Steps** がある。後者のGPU実行時間は約 **549.31秒**。#377ではオーナーによる画像編集成果の確認もあるが、モデル完走はあらゆる実用品質・人物ID保持の承認と同じではない。

## 8. Windows Möbius：複数の独立したAIノード

YUYU3D、Node A、Node B、Utility03の4台は独立したOllama応答と、Studio上の相互議論のレシートを残した。単純な算術問題で以前の14Bモデルの遅延が **66.186秒** だったのに対し、独立CPU-onlyのQwen2.5 3Bサービスではモデル応答 **1.094／1.265秒**、Studio側の作成から完了まで約 **4秒** が記録された。異なるモデルと構成による限定的な測定であり、全推論に一定倍率の改善があるとの主張ではない。

## 9. Mac Möbius：LAN数学分割と独立検証

- **iMac：**Teacher、入力生成、行列の前半128行を計算。
- **Mac mini M2：**Coordinator、後半128行と中央結果の統合。
- **MacBook Pro：**Evaluator、異なるアルゴリズムで行列全体を独立再計算。
- **Mac mini M1：**4台目のOwner Macとして32×256の追加分割を実行。

**MOBIUS-MATH-001：**256×256整数行列でM2とMacBookの最終SHA-256一致。

**MOBIUS-MATH-002：**実際のLAN配布・分算・返送・再計算を実施。3台の役割別計算時間は **895.542／578.363／2,646.046 ms**。役割が異なるため、単純な機種性能順位にはできない。

**MOBIUS-MATH-STREAM-001：**異なるSeed／Jobの **24/24バッチ VERIFIED**。第24バッチの合成結果と独立検証のSHA：

`c8219ed9d202697cb93d771e8124d89d02e593fe8a297d89e80cda668cb88f57`

M1も割り当てられた行列部分の計算・検証を実行している。4台がすでに任意の大規模AI学習を共同で実行できることまでは証明していない。

## 10. Temporal Möbius：数理的経路判断と実際の重み学習

### 10.1 ネイティブ結果から経路を推定

Windows World Model の履歴評価は実際の **41件**（Success 24、OOM 15、その他失敗2）を使用。時間順序を保持したテストで Brier Score **0.338335**、比較基準 **0.375438**。限定的なモデル評価として改善したが、全体最適を自律的に求める完成済みスケジューラとの証明ではない。

### 10.2 Möbius Neural：数理戦略MLP

**5×12×3** のTanh／Softmax MLPで合成数学Kernelを選択。iMacが54件の訓練例を生成し、M2で**95Epoch**更新。Lossは **1.083127→0.098988**。MacBookの**未見24件**で正解率 **91.7%**、当該合成課題でNaiveとの時間比 **2.1161倍**。実際の重み変更と独立評価のレシートがある。

### 10.3 Möbius LLM：事前学習済みモデルの部分更新

M2 MPS上のDistilGPT2試験。総パラメータ **81,912,576**、訓練対象 **7,089,408**。合成学習42件・検証12件、16Steps、実行 **18.71秒**、Validation Loss **5.720391→5.176930**。28,362,810バイトの更新重みとSHAを記録した。これは部分重み訓練の実行証拠であり、汎用自律AI完成を意味しない。

## 11. Windows／macOSの異種協調が持つ意義

HAVEFUNが目指すのは、全機器に同じソフトを入れることではない。異なる計算役割を、ジョブID、状態、ネイティブレシート、独立検証で結ぶことである。WindowsはH3生成・GPU Hook・CPU編集・成果物契約、MacはLAN数学分割と学習実験など、それぞれ実体のある仕事を担う。

技術の主張は「2080 Tiの物理帯域がH100／H200になった」ではなく、**既存ハードウェアで完了できるタスクの範囲を広げる**ことであり、さらに完成率・品質・総時間・コストを踏まえた経路選択へ進む。

## 12. 検証方法と主な一次証跡

| 証拠方法 | 対応結果 |
|---|---|
| 数値完全性 | GPU間20Steps `max_abs_diff=0.0`、Streamed-QKV誤差 約2～3×10⁻⁷ |
| データ完全性 | 250 MiBの送信元・Bridge・転送先SHA一致 |
| モデル実行 | `QMRNA_DIT_ENTER/EXIT`、#341 H3 Gate Receipt |
| Callback | QAnswer Finalizerの残りStep実行 |
| 物理CUDAメモリ | 32MiB Allocation 33,554,432→0→33,554,432 |
| 映像デコード | 22/22フレームのframemd5一致 |
| MP4契約 | #361 15.000秒／360フレーム／24fps／480×832 |
| CPU後編集 | GPU再生成なしで9継ぎ目を処理。V2 360/360フレーム、SSIM 0.984182 |
| Mac LAN計算 | 24/24バッチを独立検証 |
| 学習 | MLP 95Epoch、DistilGPT2部分16Steps |

個人画像、私的Prompt、認証鍵、顧客素材などは公開資料に含めない。

## 13. 結論：単一 GPU で「完了可能」にすることも技術成果

Q-Frameworkの意義は、単にGPUの配分を改善することではない。**従来の経路で失敗する高負荷の仕事を、既存の限られたハードウェアでどのように完了可能にするか**という研究である。単一の22GB RTX 2080 Ti による H3 実行、A1 の同条件 PRE-OOM 比較、#361 の4GPU短時間納品、状態継続、Macの分散数値検証と小規模な重み学習が、その異なる段階を示している。

Temporal Möbius の判断モデルは、**過去の実績→将来の候補経路予測→現在の資源・実行判断→実際の結果→判断の更新**というループを目指す。これは異種スーパーコンピュータ・ニューラルネットワークへの実践的な開発路線である。異種GPU世代をまたぐ一般的な復元、ネットワーク全体の継続学習、H100／H200との同条件性能優位は、今後検証すべき課題として明示する。

**Q-Framework — Connecting Compute. Extending Possibility.**

---

## 付録A｜公開技術資料

- [旧版公開白書RC3（日本語）](Q-Framework-v1.0-RC3-JA.md)
- [Validated Execution Paths](../docs/validated-execution-paths.md)
- [Public Claim Ledger](../docs/claim-ledger.md)
- [Architecture Overview](../docs/architecture.md)

## 付録B｜内部レシート対照索引

ジョブIDと資料種別のみを記載し、オーナーの写真・元Prompt・鍵・顧客データ・非公開ワークフローを公開しない。

- 状態移送：HF Compute Bridge F-Block XCOPY（2026/9/28）、Q7 Integration（10/17）。
- QmRNA／QSTATIC：10/3 PNG iTXt Carrier、10/4 A1 A/B、DiT Job #303、#341 Gate。
- H3動画：#135、#243、#327、#341、#344、#360、#361、#365、#370、#371、T195。
- Windows脳：10/15 Möbius Brain Chat、4ノードのOllama応答記録。
- Mac：MATH-001／002／STREAM-001、MOBIUS-EIGHT-001、NEURAL-001、LLM-001。
- CPU：HF_RS_POSTEDIT_V2_IMPLEMENTED（2026/10/23）。

## 付録C｜単一のRTX 2080 Ti 22GBにおけるH3実行能力

**追加理由：**RC4.2第6章は4GPU生産に重点があった。RC4.3は単一GPUの証拠を独立して整理する。ここでの「単一」は、H3のネイティブGPU推論がA0またはA1の1基だけで行われるという意味であり、CPU編集や通常のファイル転送を否定するものではない。

| 実験 | ネイティブ実証 | 条件・制限 |
|---|---|---|
| #370／#371 | A0のH3 Text-to-Video／Image-to-Video | 約39フレーム、16fps、2.437秒。15秒ではない |
| 10/21の48フレーム | A0、480×832、24fps、14Steps、約549.31秒 | 2秒のネイティブ動画 |
| #365 | A0が36フレーム×10RSを順番に生成、最終15秒／360フレーム | 3:12:08、9回のCUDA OOM後にRS再投入 |
| #361（別実験） | 4基のRTX 2080 Ti | 8-Step条件が異なる。全体納品14:37 |

**1080pの証拠ステータス：**オーナーは単一22GB GPUでH3の1080p作業を完了したと報告している。これは「報告済み達成事項／対応する一次レシートの収集待ち」として残す。ジョブ、ネイティブ解像度、アップスケーリングの有無、フレーム数、時間、OOM履歴、FFprobe、SHAを照合するまでは、独立検証済み1080pネイティブ性能として公開しない。

## 付録D｜PRE-OOM未完了から同一GPUの完了へ

**日付：**2026年10月4日。**GPU：**A1 RTX 2080 Ti、VRAM 22,528MiB。**比較設定：**同Static／Seed、480×832、24fps、36フレーム、10Steps。

- **QmRNA Guardなし：**Step1の空きVRAMは**108MB**。ランタイムが `RESCUE_ARMED reason=PRE_OOM` を記録。単一ワーカーの所定MP4は生成されなかった。
- **QmRNA Guardあり：**Step1～9の前に空きVRAMが**76～140MB**まで低下したが、キャッシュ回収後に約**3,212～3,244MB**となり、全10Stepsを完了して**188,242バイトのMP4**を生成。該当実行にHARD_OOMは記録されていない。
- **別のGuard試験：**22フレーム／10Stepsで空きVRAM **460～492MB→2,668MB**、実行完了。
- **モデル内の実行記録：**DiTのENTER／EXIT、`ffn_chunk=512`。

**適切な結論：**測定された負荷では、Guardのない基準経路がPRE-OOM条件で単独完了できず、Guard導入経路が完了した。すべての未導入2080TiのH3タスクでCUDA HARD_OOMが必ず発生するという一般命題でも、Guardが永久にあらゆるOOMを防ぐという命題でもない。別途実証した32MiB CUDA退避がこのジョブで発動したとも断定しない。

## 付録E｜長期目標：異種スーパーコンピュータ・ニューラルネットワーク

1. **ネイティブ実行層：**Foundation-00／QmRNAがSampler、DiT、Attentionを制御する。
2. **状態とメモリ層：**QVRAM／QSTATIC／QSTATE／QFREEZEが検証可能な保存・転送・再ロード・継続を支援する。
3. **分散協調層：**QSearch／QWorker／RS／Compute Bridgeが単一GPU、4GPU、Windows／Macの異なるタスクを協調する。
4. **判断と学習層：**Temporal Möbiusが過去の結果から候補経路、リスク、時間、必要資源を評価し、実行結果により判断を更新する。

**既に実証した範囲：**QmRNAの同GPU比較、単一GPUのH3ネイティブ動画、#365の単一GPU 15秒（リトライを含む）、#361の4GPU生産、CUDA状態移送、MacのLAN数学、限定的なMLP学習。

**汎用化が未検証の範囲：**任意のGPU世代間のH3ネイティブ復元、ネットワーク全体の信頼性ある自律判断・継続学習、H100／H200との完全同条件の性能比較。

異種スーパーコンピュータ・ニューラルネットワークは、VRAMの総量だけでなく、**タスクを完了できるか、数値状態を検証できるか、判断が改善しているか、映像品質、納品時間、総資源コスト**によって評価されるべきである。
