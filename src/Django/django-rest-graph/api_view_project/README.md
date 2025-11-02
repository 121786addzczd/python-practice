# api_view_project

## マイグレーション手順

Django では、モデルの変更内容をデータベースへ反映するために マイグレーション (migration) を行います。
以下の手順で初期設定およびモデル変更時の反映を行います。

### 1. 初期マイグレーションの適用（Django 標準アプリ用）

まず、Django がデフォルトで持つ管理用アプリ（auth、admin、sessions など）のテーブルを作成します。
これは プロジェクト作成後、最初の 1 回だけ実行 します。

```bash
python manage.py migrate
```

### 2. モデルの変更を検知してマイグレーションファイルを作成

アプリ内の models.py に新しいモデルを定義したり、既存のモデルを変更した場合は、以下を実行してマイグレーションファイル（データベース構造の設計書）を生成します。

```bash
python manage.py makemigrations
```

### 3. データベースに定義

作成されたマイグレーションファイルをもとに、データベースへ実際に変更を反映します。

```bash
python manage.py migrate
```

### 4. データベースの確認（任意）

本プロジェクトでは SQLite を使用しています。
データベースの中身を確認するには、VSCode の拡張機能 [alexcvzz.vscode-sqlite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite) を使用すると便利です。
