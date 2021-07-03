Created by ハッカソンチームA  at  [RareTech](https://raretech.site/)

# RareStudy
![](https://img.shields.io/badge/Python-3.7.2-blue) ![](https://img.shields.io/badge/Django-3.2.3-orange)

![RareStudy_readme](https://user-images.githubusercontent.com/84213832/122702029-e8a2b400-d291-11eb-9cf8-0e9301c41bc5.gif)


## 目次

- [RareStudy](#rarestudy)
  - [目次](#目次)
  - [RareStudyとは](#rarestudyとは)
  - [開発メンバー](#開発メンバー)
  - [機能](#機能)
  - [動作保証環境](#動作保証環境)
  - [インストールについて](#インストールについて)
  - [使用技術](#使用技術)
  - [追加予定機能](#追加予定機能)

## RareStudyとは
**アウトプット記事を通して知識を共有するアプリケーションです。**
* ターゲット
    *   RareTechメンバー
    *   駆け出しエンジニア
    *   Qiitaハードル高すぎ無理！！な人
    *   復習がてらちょっと何かアウトプットしてみたい人
* 目的
    *   アウトプットを通して知識の定着をはかる
    *   メンバー同士の交流
    *   文章構成力を身に付ける

## 開発メンバー
- [AOI](https://github.com/orang-0840)  限界大学生
- [REIMEI](https://github.com/Reimei1213)   毎日がデスマの大学生
- [RINA](https://github.com/Rinasham)   南半球在住IT初心者アラサー女
- [Shiny-a](https://github.com/shiny-a) 不器用なアラサー会社員

## 機能
*   メイン機能
    *   最新記事一覧表示
    *   記事の投稿/編集
    *   コメント機能/編集
    *   プロフィールを設定/編集
    *   アカウント登録/削除
*   サブ機能
    *   称号機能(post数によって変動)
    *   アイコン選択

## 動作保証環境
```
Python 3.7.2
Django 3.2.3
```

## インストールについて
```
git clone https://github.com/shiny-a/RareStudy.git
cd RareStudy
brew install mysql
pip install -r requirements.txt
python manage.py migrate
# settings.pyのSECRET_KEYを入力
python manage.py runserver
```
## 使用技術
![img](https://user-images.githubusercontent.com/84213832/122710005-ba79a000-d2a2-11eb-84f6-b5c5a2ca380b.JPG)



## 追加予定機能
- 検索機能
- グループ機能
