# DB_app
web app for JHPS_CPS 

2021/12/10 

Ryo Mikami

# 概要
「くらしの好みと満足度についてのアンケート」の調査票に記載されている質問内容をデータベース化したExcelファイルをWeb上で検索するアプリ。

https://www.iser.osaka-u.ac.jp/survey_data/panelsummary.html

# 使用方法
https://share.streamlit.io/iser-panels/db_app/main.py
にアクセスし、ブラウザから操作する。

# 内容

* db.xlsx

データベースファイル。新規の質問を追加したり内容を修正する場合はこのファイルを編集すれば結果が反映されます。
"https://github.com/ISER-panels/DB_app/raw/main/db.xlsx"

* main.py 

メインのプログラムファイル。ブラウザ上で入力された情報をdb.xlsxから検索し、下記のTextフォルダの文章を表示する。

* make_sentence.py

db.xlsxをもとに、下記のTextフォルダの内容を自動で書き換えるプログラム。db.xlsxを編集した場合に使用してください。


* Textフォルダ
アプリで表示される大問区分、小問区分にの関する説明文章と各設問の問題文が格納されている。


