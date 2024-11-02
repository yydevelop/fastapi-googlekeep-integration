# fastapi-googlekeep-integration
## フォルダ構成
```
fastapi-googlekeep-integration/
├── app/
│   ├── api/                # APIエンドポイント
│   │   ├── v1/
│   │   │   ├── googlekeep.py
│   ├── core/               # アプリケーションの設定や共通部分
│   │   ├── config.py
│   ├── domain/             # ドメイン層
│   │   ├── models/         # エンティティや値オブジェクト
│   │   │   ├── note.py
│   │   ├── services/       # アグリゲートやドメインサービス
│   ├── infrastructure/     # インフラ層（リポジトリや外部API連携）
│   │   ├── googlekeep_repository.py
│   ├── usecases/           # ユースケース（アプリケーション層のロジック）
│   │   ├── create_note_usecase.py
│   ├── main.py             # アプリケーションのエントリーポイント
└── pyproject.toml
```