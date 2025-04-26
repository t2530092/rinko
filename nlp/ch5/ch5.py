#chapter5-2-1
#質的変数の処理
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
#形態素解析
from janome.tokenizer import Tokenizer


def test_chapter_5_2_1():
    df = pd.DataFrame(
        [
            ["Cola", "S"],
            ["Cola", "M"],
            ["Green Tea", "L"],
            ["Milk", "M"],
        ],
        columns=["drink", "size"]
    )
    print(df.head())

def test_chapter_5_2_1_1():
    df = pd.DataFrame(
        [
            ["Cola", "S"],
            ["Cola", "M"],
            ["Green Tea", "L"],
            ["Milk", "M"],
        ],
        columns=["drink", "size"]
    )

    size2int = {
            "S":0,
            "M":1,
            "L":2,
            }
    
    df["size"] = df["size"].map(size2int)
    print(df.head)
    print(df["size"].unique())

#5.2.1.2名義特徴量の変換
#Cola -> 0
#Green Tea -> 1
#Milk -> 2
def test_chapter_5_2_1_2():
    df = pd.DataFrame(
        [
            ["Cola", "S"],
            ["Cola", "M"],
            ["Green Tea", "L"],
            ["Milk", "M"],
        ],
        columns=["drink", "size"]
    )

    size2int = {
            "S":0,
            "M":1,
            "L":2,
            }
    
    df["size"] = df["size"].map(size2int)

    encoder = LabelEncoder()
    #df["drinkLabel"] = encoder.fit_transform(df["drink"])
    #print(df.head())
    print(pd.get_dummies(df))
    
#5.2.2  量的変数の処理
#二値化と丸め

def test_chapter_5_2_2():
    df = pd.DataFrame(
        [
            [7.2500],
            [71.2833],
            [7.9250],
            [53.1000],
        ],
        columns=["Fare"]
    )
    print(df["Fare"])

#5.2.2.1 2値化
def test_chapter_5_2_2_1():
    df = pd.DataFrame(
        [
            [7.2500],
            [71.2833],
            [7.9250],
            [53.1000],
        ],
        columns=["Fare"]
    )
    print(df["Fare"] > 10)
    print((df["Fare"] > 10).astype(int))

#5.2.2.1 丸め　（整数化？）
def test_chapter_5_2_2_2():
    df = pd.DataFrame(
        [
            [7.2500],
            [71.2833],
            [7.9250],
            [53.1000],
        ],
        columns=["Fare"]
    )
    df["FareInt"] = df["Fare"].round().astype(int)
    print(df[["Fare", "FareInt"]].head())

#5.3    テキストのベクトル表現
#N-gram ベクトル
#シーケンスベクトル

#5.3.1.1    One-hot エンコーディング
def test_chapter_5_3_1_1():
    #one-hot エンコーディングの実装
    vectorizer = CountVectorizer(binary=True)
    docs = ["the cat is out of the bag", "dogs are"]
    bow = vectorizer.fit_transform(docs)
    print(bow.toarray())
    print(vectorizer.vocabulary_)

    #日本語を試す
    vectorizer_jp = CountVectorizer(binary=True)
    docs_jp = ["天気がいいから、散歩しましょう"]
    bow_jp = vectorizer_jp.fit_transform(docs_jp)
    print(bow_jp.toarray())#[[1 1]]
    
    #t = Tokenizer()
    #docs_jp_list = t.tokenize(docs_jp)
    #vectorizer_jp = CountVectorizer(binary=True)
    #bow_jp = vectorizer_jp.fit_transform(docs_jp_list)
    #print(bow_jp.toarray())
    #print(vectorizer_jp.vocabulary_)

def test_chapter_5_3_1_2():
    #Count エンコーディング
    vectorizer = CountVectorizer(binary=False)
    docs = ["the cat is out of the bag", "dogs are"]
    bow = vectorizer.fit_transform(docs)
    print(bow.toarray())

def test_chapter_5_3_1_2():
    

def main():
    index_str = input("input index:")
    index_list = index_str.split(".")
    index = "test_chapter"
    for i in index_list:
        index = f"{index}_{i}"
    print(index)
    globals()[index]()

if __name__ == "__main__":
    main()