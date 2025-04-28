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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

def analyze_data(df):
    # 1. 检查标签的分布
    plt.figure(figsize=(8, 6))
    plt.countplot(x='label', data=df)
    plt.title("Label Distribution")
    plt.xlabel("Label")
    plt.ylabel("Count")
    plt.show()

    # 2. 查看文本的长度分布
    df['text_length'] = df['text'].apply(lambda x: len(x.split()))
    plt.figure(figsize=(8, 6))
    plt.histplot(df['text_length'], bins=50, kde=True)
    plt.title("Text Length Distribution")
    plt.xlabel("Number of Words in Text")
    plt.ylabel("Frequency")
    plt.show()

    # 3. 可视化前几个文本的内容（根据需要调整）
    plt.figure(figsize=(10, 8))
    for i in range(min(5, len(df))):  # 显示前5条记录
        plt.subplot(5, 1, i + 1)
        plt.text(0.5, 0.5, df["text"].iloc[i], wrap=True, ha='center', va='center')
        plt.axis("off")
        plt.title(f"Text Sample {i+1}")
    plt.tight_layout()
    plt.show()

    # 4. TF-IDF 特征分析（前 20 个重要特征词）
    vectorizer = TfidfVectorizer(max_features=20)
    X = vectorizer.fit_transform(df['text'])
    feature_names = vectorizer.get_feature_names_out()
    tfidf_scores = X.sum(axis=0).A1  # 按特征名的总权重来排序
    feature_score_pairs = list(zip(feature_names, tfidf_scores))
    feature_score_pairs = sorted(feature_score_pairs, key=lambda x: x[1], reverse=True)

    top_features = feature_score_pairs[:20]

    # 可视化 TF-IDF 分数
    features, scores = zip(*top_features)
    plt.figure(figsize=(10, 6))
    plt.barplot(x=scores, y=features)
    plt.title("Top 20 Important Features (TF-IDF Scores)")
    plt.xlabel("TF-IDF Score")
    plt.ylabel("Feature")
    plt.show()

    # 5. 标签与文本长度的关系
    plt.figure(figsize=(8, 6))
    plt.boxplot(x="label", y="text_length", data=df)
    plt.title("Text Length Distribution by Label")
    plt.xlabel("Label")
    plt.ylabel("Text Length")
    plt.show()
    

def old_load_dataset(filename, n=5000, state=6):
    df = pd.read_csv(filename, sep='\t')

    # Converts multi-class to binary-class.
    mapping = {1: 0, 2: 0, 4: 1, 5: 1}
    df = df[df.star_rating != 3]
    df.star_rating = df.star_rating.map(mapping)

    # extracts Japanese texts.
    is_jp = df.review_body.apply(filter_by_ascii_rate)
    df = df[is_jp]

    # sampling.
    df = df.sample(frac=1, random_state=state)  # shuffle
    grouped = df.groupby('star_rating')
    df = grouped.head(n=n)
    return df.review_body.values, df.star_rating.values


def filter_by_ascii_rate(text, threshold=0.9):
    ascii_letters = set(string.printable)
    rate = sum(c in ascii_letters for c in text) / len(text)
    return rate <= threshold

def mapping_dfdata(df):
    mapping = {1:0,
            2:0,
            4:1,
            5:1}
    df = df[df.label != 3]
    df .star_rating = df.star_rating.map(mapping)
    return df

def my_map(df):
    #analyze_data(df)
    df = df.sample(frac=1, random_state=6)
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

    sol_df = {"text":[], "label":[]}

    sol_df["text"] = new_df["text"][:5000]
    sol_df["label"] = new_df["label"][:5000]
    return pd.DataFrame({"text": sol_df["text"], "label": sol_df["label"]})

def load_data():
    dataset = load_dataset("SetFit/amazon_reviews_multi_ja")
    dataset.set_format(type="pandas")
    df = dataset["train"][:]
    
    new_df = my_map(df)
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