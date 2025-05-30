# KWIC分析ツール

このアプリケーションはWikipediaの記事に対してKWIC（Key Word In Context）分析を行うWebアプリケーションです。検索語句の前後の文脈を品詞ごとに整理して表示します。
2025年4月~5月にかけて英語の授業で制作しました。

Webアプリに至るまでの小さなタスクも、このリポジトリ内にあります。

generated by chatGPT!!

## 機能

- Wikipediaから指定したトピックの記事を取得
- 指定した検索語句の文脈を表示
- 結果を品詞（名詞、動詞、形容詞）ごとにグループ化
- 検索語句をハイライト表示（色の選択が可能）
- 文脈の表示範囲（ウィンドウサイズ）を調整可能
- 英語と日本語の両方に対応
- 検索モードの選択（Wikipedia検索またはURL直接入力）
- 部分一致検索機能
- 検索結果の出現頻度によるソート
- 検索語句の次の単語の品詞による分類

## セットアップ

1. 必要なパッケージをインストール



2. アプリケーションを起動

```bash
python app.py
```

3. ブラウザで以下のURLにアクセス

```
http://127.0.0.1:5000/
```

## 使い方

1. 検索モードの選択
   - Wikipedia検索モード：Wikipediaの記事から検索
   - URL検索モード：任意のウェブページのURLを直接入力して検索

2. 検索内容の入力
   - Wikipedia検索モードの場合：
     - 「Wikipedia記事のトピック」に検索したいWikipediaの記事名を入力（例：「Banana (fruit)」）
   - URL検索モードの場合：
     - 「URL」に分析したいウェブページのURLを入力（例：「https://example.com/article」）

3. 分析設定
   - 「検索語句」に分析したい単語やフレーズを入力（例：「bananas are」）
   - 「表示する前後の単語数」で文脈として表示する語数を設定
   - 検索語句のハイライト色を選択
   - 言語を選択（英語または日本語）

4. 分析の実行
   - 「分析する」ボタンをクリックして結果を表示
   - 結果は品詞ごとにグループ化され、出現頻度順に表示されます

## 技術スタック

- Python 3
- Flask
- NLTK
- Wikipedia API
- MeCab（日本語形態素解析） 
