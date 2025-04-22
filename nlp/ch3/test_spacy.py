# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy

# Load English tokenizer, tagger, parser and NER
#nlp = spacy.load("en_core_web_sm")

nlp = spacy.load("ja_core_news_sm")
# Process whole documents

text = ("P8でのファクトイド型（Factoid）の質問について調べました。「Factoid（ファクトイド）」とは、擬似事実です。ここでは、原文で触れられていなかった点を補足したいと思います。"
        "actoid型の質問は、本文にもあるように、短いテキストで答えることが可能ですが、その一方で先入観を含んでいることがあります。"
        "例えば、「2024年のオリンピックは日本のどこで開催されるのか？」という質問は、そもそも誤りです。"
        "なぜなら、2024年のオリンピックはパリで開催されるからです。"
        "この質問が2024年のオリンピック主催は日本にしました。"
        "このような質問が「擬似事実（Factoid）」であり、真偽の判断はAIにとっても一つの試練と言えます。"
        )
#text = (
#    "業務開発で一番使ったのがjsonだったので、CSVとTSVという二つのファイルを初めて知った。カンマとタブを使って、数値を区切られたものだね。でもタイプの定義が色々あるので、正しく認識できない場合もあるだろう。"
#    "疑問：P16の図2-3-4とP17の図2-3-5、二つの図はデータが同じですが、決定境界が違います。作者は「複雑な決定境界を描くこともできます」と言いましたから、この決定境界はAIが自ら学習して導き出したものではなく、私たちが自分で描いたものではないでしょうか。つまり、私たちがデータを分析して適切な決定境界を引き、それをもとにAIに判断させている感じですか。"
#)
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)