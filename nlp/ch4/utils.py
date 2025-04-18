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

def filter_by_ascii_rate(text, threshold=0.9):
    ascii_letters = set(string.printable)
    rate = sum( c in ascii_letters for c in text ) / len(text)
    return rate <= threshold

def load_dataset(filename, n=5000, state=6):
    df = pd.read_csv(filename, sep="\t")

    is_jp = df.review_body.apply(filter_by_ascii_rate)
    df = [is_jp]
    #sampling
    df = df.sample(frac=1, random_state=state) #shuffle
    grouped = df.groupby("star_rating")
    df = grouped.head(n=n)
    return df.review_body.values, df.star_rating.values

def filter_by_ascii_rate(text, threshold=0.9):
    ascii_letters = set(string.printable)
    rate = sum(c in ascii_letters for c in text) / len(text)
    return rate <= threshold

import re
from bs4 import BeautifulSoup
from janome.tokenizer import Tokenizer

t = Tokenizer()
def clean_html(html, strip=False):
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(strip=strip)
    return text

def tokenize(text):
    tokens = [token.base_form for token in t.tokenize(text)]
    return tokens

def normalize_number(text, reduce=False):
    if reduce:
        normalized_text = re.sub(r'\d+', '0', text)
    else:
        normalized_text = re.sub(r'\d', '0', text)
    return normalized_text

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def train_and_eval(x_train, y_train, x_test, y_test, lowercase=False,\
                   tokenize=None, preprocessor=None):
    return

