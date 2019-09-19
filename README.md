# Blog

[![Build Status](https://travis-ci.org/marush-in/blog.svg?branch=master)](https://travis-ci.org/marush-in/blog)

# 開発環境

## 構成

- Docker で使用するバージョン一覧

|Python(alpine)|Postgresql|
|:-|:-|
|3.7|11.0|

## コマンド一覧

※ Dockerを立ち上げる

・開発環境の構築
```
app内に.envファイルを作成し、必要情報を入力する
./command init
```

・開発環境を起動する
```
./command up
```

・開発環境を停止する
```
./command down
```

・開発環境を再起動する
```
./command restart
```

・DBを初期化する
```
./command initdb
```

・アプリケーションのコンテナに入る
```
./command login
```

・Postgresqlのシェルにログインする
```
./command postgres
```

・管理ユーザーを作成する
```
./command createsuperuser
```

・マイグレーションファイルを作成する
```
./command makemigrations
```

・マイグレーションファイルをDBに適用する
```
./command migrate
```

・文法を確認する
```
./command flake8
```

・テストを実行する
```
./command test
```

## デプロイ

`Fabric` でのデプロイ方法　　

deployフォルダ内のfabfile.py.sampleをfabfile.pyに変更し、必要情報を入力する

・デプロイコマンド
```
cd deploy
fab production
```
