from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.model_selection import train_test_split

#from preprocessing import  tokenize
from utils import train_and_eval

from datasets import load_dataset
import random
def main():
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

    #print(df.head())
    #分割数据集
    x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                      test_size=0.2,
                                                      random_state=42)
    #训练数据4000 测试数据1000
    
    print("Binary")
    vectorizer = CountVectorizer(binary=True)
    train_and_eval(x_train, y_train, x_test, y_test, vectorizer)    

    print("Count")
    vectorizer = CountVectorizer(binary=True)
    train_and_eval(x_train, y_train, x_test, y_test, vectorizer) 

    print("TF-IDF")
    vectorizer = TfidfVectorizer()
    train_and_eval(x_train, y_train, x_test, y_test, vectorizer) 

    print("Bigram")
    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    train_and_eval(x_train, y_train, x_test, y_test, vectorizer) 

if __name__ == "__main__":
    main()