#解決策（quick-fix）

#HuggingFace Hubに公開されているデータセットを使う
#手順

#HuggingFace Datasetsをインストール。
#!pip install -Uq datasets
#load_datasetで読み込む。
#from datasets import load_dataset

#dataset = load_dataset("SetFit/amazon_reviews_multi_ja")
#dataset.set_format(type="pandas")
#df = dataset["train"][:]
#df.head()



import string
import pandas as pd

from datasets import load_dataset

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

    
def mapping_dfdata(df):
    mapping = {1:0,
            2:0,
            4:1,
            5:1}
    df = df[df.label != 3]
    df .star_rating = df.star_rating.map(mapping)
    return df

def load_data():
    dataset = load_dataset("SetFit/amazon_reviews_multi_ja")
    dataset.set_format(type="pandas")
    df = dataset["train"][:]
    df = df.sample(frac=1, random_state=6)

    #mapping = {1:0,
    #        2:0,
    #        4:1,
    #        5:1}
    #df = df[df.label != 3]
    #df .label = df.label.map(mapping)
    #label 0 1 2 3 4
    new_df = {"text":[], "label":[]}
    index = 0
    x = df["text"]
    y = df["label"]
    index = 0
    for textx in x:
        print(textx)
        index = index + 1
        if index > 10:
            break
    index = 0     
    for texty in y:
        print(texty)
        index = index + 1
        if index > 10:
            break
    index = 0
    for star in y:
        if star == 0 or star == 1:
            new_df["text"].append(x[index])
            new_df["label"].append(0)
        elif star == 3 or star == 4:
            new_df["text"].append(x[index])
            new_df["label"].append(1)
        index = index + 1
    return new_df

def train_and_eval(x_train, y_train, x_test, y_test, vectorizer):
    x_train_vec = vectorizer.fit_transform(x_train)
    x_test_vec = vectorizer.transform(x_test)

    #使用Liblinear 模型
    clf = LogisticRegression(solver="liblinear")
    clf.fit(x_train_vec, y_train)

    #开始预测
    y_pred = clf.predict(x_test_vec)
    score = accuracy_score(y_test, y_pred)
    print("{:.4f}".format(score))