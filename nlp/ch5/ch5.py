#chapter5-2-1
#質的変数の処理
import pandas as pd
from sklearn.preprocessing import LabelEncoder
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