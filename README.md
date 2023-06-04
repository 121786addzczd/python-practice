# python-practice
主にjupyter Labを使用してpython練習するリポジトリです。</br>
## 環境構築</br>

### コンテナ作成・起動
```shell
docker-compose up --build -d
```
コンテナ作成・起動後、http://localhost:8888/にアクセスすることでjupyter Labが使用可能になります。

## Dockerの全削除の方法</br>
Dockerのイメージやコンテナを削除します。下記を上から下まで実行した上で、それを3回繰り返してください。</br>
他のイメージやコンテナも削除されるのでそれをしっかり理解した上で使いましょう。</br>
```docker image prune -af```</br>
```docker volume prune -f```</br>
```docker container prune -f```</br>
```docker system prune -f```</br>
