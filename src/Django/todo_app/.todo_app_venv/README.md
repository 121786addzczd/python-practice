# Django/todo_app

CRUD 操作とログインやユーザー新規登録、タスク検索機能を備えた本格的な Todo リストを構築しながら Django の基礎を学習

## 環境構築

#### 仮想環境を有効にする

```
source .todo_app_venv/Scripts/activate
```

#### 仮想環境を無効かする場合

```
deactivate
```

#### Django インストール

```
pip install django
```

#### Django が入っているか確認

```
pip freeze
```

Django==4.2.6 といった具合で表示されれば導入 OK

#### ひな形作成

```
django-admin startproject todoproject
```

#### 作成した todoproject に移動

```
cd todoproject
```

#### プロジェクトを作成したのでアプリ作成

```
python manage.py startapp todoapp
```

#### python のサーバーを起動する

```
python manage.py runserver
```
