import string
import pandas as pd
from bs4 import BeautifulSoup
from janome.tokenizer import Tokenizer
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from datasets import load_dataset

def filter_by_ascii_rate(text, threshold=0.9):
    ascii_letters = set(string.printable)
    rate = sum(c in ascii_letters for c in text) / len(text)
    return rate <= threshold


def load_data(n=5000, state=6):
    dataset = load_dataset("SetFit/amazon_reviews_multi_ja")
    dataset.set_format(type="pandas")
    df = dataset["train"][:]
    df = df.sample(frac=1, random_state=6)
    df = df.head(n=5000)
    #x = df["text"]
    #y = df["label"]

    # Converts multi-class to binary-class.
    mapping = {0: 0, 1: 0, 3: 1, 4: 1}
    df = df[df.label != 2]
    df.label = df.label.map(mapping)

    # extracts Japanese texts.
    is_jp = df.text.apply(filter_by_ascii_rate)
    df = df[is_jp]

    # sampling.
    df = df.sample(frac=1, random_state=state)  # shuffle
    grouped = df.groupby('label')
    df = grouped.head(n=n)
    return df.text.values, df.label.values

t = Tokenizer(wakati=True)

def tokenize(text):
    return t.tokenize(text)
def clean_html(html, strip=False):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text(strip=strip)
    return text


def train_and_eval(x_train, y_train, x_test, y_test, vectorizer):
    x_train_vec = vectorizer.fit_transform(x_train)
    x_test_vec = vectorizer.transform(x_test)
    clf = LogisticRegression(solver='liblinear')
    clf.fit(x_train_vec, y_train)
    y_pred = clf.predict(x_test_vec)
    score = accuracy_score(y_test, y_pred)
    print('{:.4f}'.format(score))

    print('Tokenization for faster experiments')

def main():
    #url = 'https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_multilingual_JP_v1_00.tsv.gz'
    #x, y = load_dataset(url, n=5000)
    


    #dataset = load_dataset("SetFit/amazon_reviews_multi_ja")
    #dataset.set_format(type="pandas")
    #df = dataset["train"][:]
    #df = df.sample(frac=1, random_state=6)
    #df = df.head(n=5000)
    #x = df["text"]
    #y = df["label"]
    x,y = load_data(n=5000)
    x = [clean_html(text, strip=True) for text in x]
    x_tokenized = [' '.join(tokenize(text)) for text in x]
    x_train, x_test, y_train, y_test = train_test_split(x_tokenized, y, test_size=0.2, random_state=42)

    print('Binary')
    vectorizer = CountVectorizer(binary=True)
    train_and_eval(x_train, y_train, x_test, y_test, vectorizer)

    print('Count')
    vectorizer = CountVectorizer(binary=False)
    train_and_eval(x_train, y_train, x_test, y_test, vectorizer)

    print('TF-IDF')
    vectorizer = TfidfVectorizer()
    train_and_eval(x_train, y_train, x_test, y_test, vectorizer)

    print('Bigram')
    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    train_and_eval(x_train, y_train, x_test, y_test, vectorizer)

if __name__ == "__main__":
    main()