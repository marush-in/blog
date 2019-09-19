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
./operate init
```

・開発環境を起動する
```
./operate up
```

・開発環境を停止する
```
./operate down
```

・開発環境を再起動する
```
./operate restart
```

・DBを初期化する
```
./operate initdb
```

・アプリケーションのコンテナに入る
```
./operate login
```

・Postgresqlのシェルにログインする
```
./operate postgres
```

・管理ユーザーを作成する
```
./operate createsuperuser
```

・マイグレーションファイルを作成する
```
./operate makemigrations
```

・マイグレーションファイルをDBに適用する
```
./operate migrate
```

・文法を確認する
```
./operate flake8
```

・テストを実行する
```
./operate test
```

## デプロイ

`Fabric` でのデプロイ方法　　

deployフォルダ内のfabfile.py.sampleをfabfile.pyに変更し、必要情報を入力する

・デプロイコマンド
```
cd deploy
fab production
```
