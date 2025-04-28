from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.model_selection import train_test_split

from preprocessing import tokenize
from ch5_utils import train_and_eval
from ch5_utils import load_data
from preprocessing import clean_html
import matplotlib.pyplot as plt
import random
def main():
    
    df = load_data()
    #
    df["label"].value_counts().plot(kind='bar')
    plt.title("Label distribution")
    plt.show()

    x = df["text"]
    y = df["label"]
    print("len of x is")
    print(len(x))
    print("len of y is")
    print(len(y))
    
    #index = 0
    #for textx in x:
    #    print(textx)
    #    index = index + 1
    #    if index > 10:
    #        break
    #index = 0     
    #for texty in y:
    #    print(texty)
    #    index = index + 1
    #    if index > 10:
    #        break

        
    #for indexy in y:
    #    print(indexy)

    #print(df.head())
    #分割数据集

    x = [clean_html(text, strip=True) for text in x]
    print('Tokenization for faster experiments')
    x = [' '.join(tokenize(text)) for text in x]

    #index = 0
    #for textx in x:
    #    print(textx)
    #    index = index + 1
    #    if index > 10:
    #        break
    #index = 0     
    #for texty in y:
    #    print(texty)
    #    index = index + 1
    #    if index > 10:
    #        break

    x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                      test_size=0.2,
                                                      random_state=42)
    #训练数据4000 测试数据1000
    print(f"train data {len(x_train)} test data {len(x_test)}")
    index = 0
    for textx in x_train:
        print(textx)
        index = index + 1
        if index > 10:
            break
    index = 0     
    for texty in y_train:
        print(texty)
        index = index + 1
        if index > 10:
            break

    print("Binary")
    vectorizer = CountVectorizer(binary=True)
    train_and_eval(x_train, y_train, x_test, y_test, vectorizer)    

    print("Count")
    vectorizer = CountVectorizer(binary=False)
    train_and_eval(x_train, y_train, x_test, y_test, vectorizer) 

    print("TF-IDF")
    vectorizer = TfidfVectorizer()
    train_and_eval(x_train, y_train, x_test, y_test, vectorizer) 

    print("Bigram")
    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    train_and_eval(x_train, y_train, x_test, y_test, vectorizer) 

if __name__ == "__main__":
    main()