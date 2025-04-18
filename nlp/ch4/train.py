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

from sklearn.model_selection import train_test_split
from preprocessing import clean_html, normalize_number, tokenize, tokenize_base_form
from utils import load_dataset, train_and_eval
from datasets import load_dataset
import random

def main():
    datasize = 100
    dataset = load_dataset("SetFit/amazon_reviews_multi_ja")
    dataset.set_format(type="pandas")
    df = dataset["train"][:]
    df = df.sample(frac=1, random_state=6)
    df = df.head(n=5000)
    x = df["text"]
    y = df["label"]
    print("len of x is")
    print(len(x))
    print("len of y is")
    print(len(y))
    #for indexy in y:
    #    print(indexy)

    print(df.head())
    x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                      test_size=0.2,
                                                      random_state=42)
    print('Tokenization only.')
    train_and_eval(x_train, y_train, x_test, y_test, tokenize=tokenize)

    print('Clean html.')
    train_and_eval(x_train, y_train, x_test, y_test, tokenize=tokenize, preprocessor=clean_html)

    print('Normalize number.')
    train_and_eval(x_train, y_train, x_test, y_test, tokenize=tokenize,
                   preprocessor=normalize_number)

    print('Base form.')
    train_and_eval(x_train, y_train, x_test, y_test, tokenize=tokenize_base_form)

    print('Lower text.')
    train_and_eval(x_train, y_train, x_test, y_test, tokenize=tokenize, lowercase=True)

if __name__ == '__main__':
    main()
