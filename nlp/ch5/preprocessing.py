import string
import pandas as pd
from bs4 import BeautifulSoup
from janome.tokenizer import Tokenizer
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from janome.tokenizer import Tokenizer

t = Tokenizer(wakati=True)


def tokenize(text):
    return t.tokenize(text)


def clean_html(html, strip=False):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text(strip=strip)
    return text