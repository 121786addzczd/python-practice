# Django Restful API & GraphQL

## 環境構築

### 初回のみ

#### python の仮想環境作成

```bash
python -m venv .venv
```

#### 仮想環境に切り替え

```bash
. .venv/bin/activate
```

その後、 which python コマンドを実行して django-rest-graph/.venv/bin/python と表示されれば OK
仮想環境から抜ける場合は、deactivate コマンド実行することで仮想環境終了できます。

### Django サーバー起動

first_rest_project ディレクトリにいる状態で以下コマンド実行でサーバー起動できます。

```bash
python manage.py runserver
```
