# `.github/skills` スキル一覧

調査対象: `E:\Program\yt3\.github\skills`。各スキルの `SKILL.md` に書かれた用途を要約した。確認時点で **51 スキル**（直下に 46、`.system` に 5）がある。リンクはこの文書から各 `SKILL.md` への相対パス。

## ディレクトリ構成

```text
.github/skills/
├── .system/    # スキルやプラグインの管理、画像生成など（5件）
├── <スキル名>/ # 用途別のスキル（40件）
└── <固有スキル名>/ # このリポジトリ固有のスキル（6件）
```

各スキルは `<スキル名>/SKILL.md`、または `<区分>/<スキル名>/SKILL.md` を中心に配置される。下表の「補助」は、そのスキル直下に実在するサブディレクトリを示す。`agents` はエージェント向け設定、`assets` は画像やテンプレート、`references` / `reference` は参考資料、`scripts` は補助プログラム、`examples` は使用例、`evaluations` は評価用資料。`LICENSE.txt` などの直下ファイルは表では省略した。

## このリポジトリ固有のスキル（6件）

| スキル | 主な用途 | 補助 |
| --- | --- | --- |
| [ai-resource-efficiency](../.github/skills/ai-resource-efficiency/SKILL.md) | モデルを問わず、品質を保ちながら AI の利用枠と計算量を効率的に使う | なし |
| [work-guidelines](../.github/skills/work-guidelines/SKILL.md) | 日本語での説明、既存設計、仕様確認などの共通方針 | なし |
| [ui-design](../.github/skills/ui-design/SKILL.md) | ダーク調 UI のデザイン方針 | なし |
| [app-structure](../.github/skills/app-structure/SKILL.md) | `src/` の構成、Windows 起動、変換成果物 | なし |
| [readme](../.github/skills/readme/SKILL.md) | README の記載内容と更新判断 | なし |
| [quality-checks](../.github/skills/quality-checks/SKILL.md) | 公開 API の説明、テスト、変更後の確認と報告 | なし |

## 用途別スキル（`skills/` 直下、40件）

| スキル | 主な用途 | 補助 |
| --- | --- | --- |
| [aspnet-core](../.github/skills/aspnet-core/SKILL.md) | ASP.NET Core アプリの構築、レビュー、改善 | agents, assets, references |
| [chatgpt-apps](../.github/skills/chatgpt-apps/SKILL.md) | ChatGPT Apps SDK のアプリ構築・修正 | agents, references, scripts |
| [cli-creator](../.github/skills/cli-creator/SKILL.md) | API や既存ツールから Codex 用 CLI を作成 | agents, references |
| [cloudflare-deploy](../.github/skills/cloudflare-deploy/SKILL.md) | Cloudflare Workers / Pages などへのデプロイ | agents, assets, references |
| [define-goal](../.github/skills/define-goal/SKILL.md) | 具体的で測定可能な目標の定義 | agents |
| [figma](../.github/skills/figma/SKILL.md) | Figma のデザイン情報取得とコードへの反映 | agents, assets, references |
| [figma-code-connect-components](../.github/skills/figma-code-connect-components/SKILL.md) | Figma コンポーネントとコードの対応付け | agents, assets, references, scripts |
| [figma-create-design-system-rules](../.github/skills/figma-create-design-system-rules/SKILL.md) | プロジェクト固有のデザインシステム規則を作成 | agents, assets, references, scripts |
| [figma-create-new-file](../.github/skills/figma-create-new-file/SKILL.md) | Figma / FigJam の新規ファイル作成 | agents, assets |
| [figma-generate-design](../.github/skills/figma-generate-design/SKILL.md) | アプリの画面やページを Figma 上に作成・更新 | agents, assets |
| [figma-generate-library](../.github/skills/figma-generate-library/SKILL.md) | コードベースから Figma の変数・コンポーネント群を構築 | agents, assets, references, scripts |
| [figma-implement-design](../.github/skills/figma-implement-design/SKILL.md) | Figma デザインをアプリの UI コードに実装 | agents, assets |
| [figma-use](../.github/skills/figma-use/SKILL.md) | Figma ファイル内の読み書きに使う操作手順 | agents, assets, references |
| [gh-address-comments](../.github/skills/gh-address-comments/SKILL.md) | GitHub PR のレビュー・Issue コメントへの対応 | agents, assets, scripts |
| [gh-fix-ci](../.github/skills/gh-fix-ci/SKILL.md) | GitHub Actions の失敗した PR チェックを調査・修正 | agents, assets, scripts |
| [hatch-pet](../.github/skills/hatch-pet/SKILL.md) | Codex 用アニメーションペットとスプライトシートの作成・検証 | agents, references, scripts |
| [jupyter-notebook](../.github/skills/jupyter-notebook/SKILL.md) | 実験・チュートリアル用 Notebook の作成・編集 | agents, assets, references, scripts |
| [linear](../.github/skills/linear/SKILL.md) | Linear の Issue・プロジェクト管理 | agents, assets |
| [migrate-to-codex](../.github/skills/migrate-to-codex/SKILL.md) | 指示ファイル、スキル、エージェント、MCP 設定を Codex 向けに移行 | agents, references, scripts |
| [netlify-deploy](../.github/skills/netlify-deploy/SKILL.md) | Netlify へのサイト公開・連携 | agents, assets, references |
| [notion-knowledge-capture](../.github/skills/notion-knowledge-capture/SKILL.md) | 会話や決定事項を Notion のナレッジに整理 | agents, assets, evaluations, examples, reference |
| [notion-meeting-intelligence](../.github/skills/notion-meeting-intelligence/SKILL.md) | Notion の情報を使った会議資料・議題の準備 | agents, assets, evaluations, examples, reference |
| [notion-research-documentation](../.github/skills/notion-research-documentation/SKILL.md) | 複数の Notion 情報を調査し、文書にまとめる | agents, assets, evaluations, examples, reference |
| [notion-spec-to-implementation](../.github/skills/notion-spec-to-implementation/SKILL.md) | Notion の仕様から実装計画・タスク・進捗管理を作成 | agents, assets, evaluations, examples, reference |
| [openai-docs](../.github/skills/openai-docs/SKILL.md) | OpenAI 製品・API・Codex の公式文書を調べる | agents, assets, references, scripts |
| [pdf](../.github/skills/pdf/SKILL.md) | PDF の読み取り、作成、描画による確認 | agents, assets |
| [playwright](../.github/skills/playwright/SKILL.md) | ターミナルから実ブラウザーを自動操作 | agents, assets, references, scripts |
| [playwright-interactive](../.github/skills/playwright-interactive/SKILL.md) | 対話的なブラウザー・Electron 操作と UI 調査 | agents, assets |
| [render-deploy](../.github/skills/render-deploy/SKILL.md) | Render へのアプリ公開と Blueprint 作成 | agents, assets, references |
| [screenshot](../.github/skills/screenshot/SKILL.md) | デスクトップやウィンドウのスクリーンショット取得 | agents, assets, scripts |
| [security-best-practices](../.github/skills/security-best-practices/SKILL.md) | 対応言語のセキュリティ推奨事項に沿ったレビュー | agents, references |
| [security-ownership-map](../.github/skills/security-ownership-map/SKILL.md) | Git 履歴から機密コードの所有者や属人化を分析 | agents, references, scripts |
| [security-threat-model](../.github/skills/security-threat-model/SKILL.md) | リポジトリを基に脅威・攻撃経路・対策を整理 | agents, references |
| [sentry](../.github/skills/sentry/SKILL.md) | Sentry の障害・イベント・稼働状況を調査 | agents, assets |
| [speech](../.github/skills/speech/SKILL.md) | テキストから音声やナレーションを生成 | agents, assets, references, scripts |
| [transcribe](../.github/skills/transcribe/SKILL.md) | 音声・動画から文字起こし、話者の識別 | agents, assets, references, scripts |
| [vercel-deploy](../.github/skills/vercel-deploy/SKILL.md) | Vercel へのアプリ・サイトのデプロイ | agents, assets, scripts |
| [webapp-delivery](../.github/skills/webapp-delivery/SKILL.md) | ローカル実行できる Web アプリと起動手順を納品 | agents |
| [winui-app](../.github/skills/winui-app/SKILL.md) | WinUI 3 デスクトップアプリの構築・設計・検証 | agents, assets, references |
| [yeet](../.github/skills/yeet/SKILL.md) | 明示的な依頼に基づき Git のステージから PR 作成まで実施 | agents, assets |

## `.system`（5件）

| スキル | 主な用途 | 補助 |
| --- | --- | --- |
| [imagegen](../.github/skills/.system/imagegen/SKILL.md) | ラスター画像の生成・編集 | agents, assets, references, scripts |
| [openai-docs](../.github/skills/.system/openai-docs/SKILL.md) | OpenAI 製品・API・Codex の公式文書を調べる | agents, assets, references, scripts |
| [plugin-creator](../.github/skills/.system/plugin-creator/SKILL.md) | Codex プラグインのひな形と設定を作成 | agents, references, scripts |
| [skill-creator](../.github/skills/.system/skill-creator/SKILL.md) | Codex スキルの作成・更新 | agents, references, scripts |
| [skill-installer](../.github/skills/.system/skill-installer/SKILL.md) | カタログや GitHub から Codex スキルを導入 | agents, assets, scripts |

`openai-docs` は `skills/` 直下と `.system` の両方に配置されているため、それぞれ別件として数えた。この文書は配置と記載内容の目録であり、外部サービスへの接続状態や各スキルの動作可否までは検証していない。
