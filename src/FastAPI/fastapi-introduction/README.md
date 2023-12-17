# FsatAPI入門

## FastAPIとは
- APIを構築するためのモダンで高速なPython Webフレームワーク
  - パファーマンスが高速
  - 開発が高速

- 2018年にリリースされ、PythonWebフレームワークとしては後発
- 型ヒントに基づいて開発を行う

## FastAPIの特徴
- パファーマンス・開発が高速
  - シンプルで直感的な記述により簡単にAPIが作成でき処理も高速
- 型ヒントを使用した安全な開発
  - 高品質でメンテナンス性の高いAPIが誰でも作成可能
- 自動ドキュメント生成機能
  - OpenAPI標準に則ったドキュメントが自動生成されコードとドキュメントの不整合が発生しない
- 公式ドキュメントさ充実
  - 後発ながらコミュニティが非常に活発でドキュメントが豊富

## FastAPIが使われている例
- Netflix
- Microsoft
- Uber


## 他のWebフレームワークとの比較
### Django
- オールインワンなWebフレームワーク
- 大規模なコミュニティと豊富なドキュメント
- 多くの組み込み機能が存在するため大規模なアプリケーション向け
- 学習難易度はやや高め

### Flask
- マイクロフレームワークとして設計され、必要最低限の機能のみ提供
- 柔軟に拡張可能な一方、多くの機能やツールを自分で追加する必要がある


## 環境構築

Python仮想環境の作成
```shell
python -m venv .venv
```
上記のコマンドは.venvという名前のディレクトリを作成し、そこに新しい仮想環境をセットアップします。


仮想環境のアクティベート
```shell
source .venv/bin/activate
```
仮想環境がアクティベートされると、コマンドラインのプロンプトに仮想環境の名前が表示されます。これにより、現在アクティベートされている仮想環境を簡単に識別できます。

FastAPIをダウンロードする
```
pip install fastapi
```

FastAPIを実行するために必要なサーバーをインストール
```
pip install "uvicorn[standard]"
```

FastAPIのuvicornサーバ起動
```shell
uvicorn main:app --reload
```

レスポンスがあるか確認
```
curl localhost:8000
```

データベース操作に使用するライブラリsqlalchemyをinstall
```
pip install sqlalchemy
```

sqlalchemyのモデルを使用したマイグレーションするために必要なライブラリをinstall
```
pip install alembic psycopg2-binary
```

migrationsディレクトリ作成
```
alembic init migrations
```


migrationsファイルを作成
```
alembic revision --autogenerate -m "Create items table"
```

migration実行
```
alembic upgrade head
```

## FastAPIドキュメント確認
http://localhost:8000/docsにアクセスします。
APIの更新があると自動的に内容は更新されます。
http://localhost:8000/docs画面でAPIの動作確認を行うことができます。


## ルータ
- webアプリやAPIにおけるエンドポイントの管理を助けるツール
- ユーザーがアクセスするURLと、それに対応する処理を関連づける役割
- 対応する処理を関連づけることをルーティングと呼びます

### ルーターを使用するメリット
・機能や責務ごとにエンドポイントをグループ化して別ファイルとして整理することができる
・エンドポイントの再利用が可能になる
・異なるモジュールやアプリケーションの部分を分離して開発可能になる


pytestライブラリ導入
```shell
pip install pytest
```

httpxライブラリ導入
```
pip install httpx
```


## 環境周りのライブラリ
環境変数を管理するためのライブラリを導入
```
pip install python-dotenv
```
設定ファイルにおいてバリデーションを行うライブラリを導入
```
pip install pydantic-settings
```