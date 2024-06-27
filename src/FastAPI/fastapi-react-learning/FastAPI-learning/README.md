公式ドキュメント：https://fastapi.tiangolo.com/ja/

FastAPI を使用する際に必要なライブラリをインストール

```shell
pip install fastapi ; pip install "uvicorn[standard]"
```

以下のコマンドでサーバーを起動します

```shell
uvicorn main:app --reload
```

## 自動対話型の API ドキュメント

http://127.0.0.1:8000/docs にアクセスすることで自動対話型の API ドキュメントが表示されます。
