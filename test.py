import nltk
nltk.data.path.append("./.venv/nltk_data")  # 必要に応じて追加

# リソースがない場合のために再ダウンロード
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

from nltk import word_tokenize, pos_tag

text = "This is a test."
tokens = word_tokenize(text)
tags = pos_tag(tokens)

print(tags)
