import os
import chardet
import pandas as pd
import re

def detect_encoding(file_path, num_bytes=10000):
    """文件编码自动检测"""
    with open(file_path, "rb") as f:
        raw = f.read(num_bytes)
        result = chardet.detect(raw)
        return result['encoding'] or 'utf-8'
    
def read_txt_files_from_folder(folder_path, group_label):
    data = []
    print(f"reading data from path {folder_path}")
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            encoding = detect_encoding(file_path)
            with open(file_path, "r", encoding=encoding) as f:
                content = f.read()
                data.append({
                    "group": group_label,
                    "filename": filename,
                    "content": content
                })
    return data

def get_alldata():
    # 各フォルダのパスを指定（必要に応じて変更）
    #KR（韓国人学習者データ）
    #TM（台湾人学習者データ）
    #JP（日本人母語話者データ）

    folder_a = "./data/KRjp_txt"
    folder_b = "./data/TMjp_txt"
    folder_c = "./data/jp_txt"

    print("カレントディレクトリ:", os.getcwd())

    # 各フォルダのデータを読み込み
    data_a = read_txt_files_from_folder(folder_a, "KR")
    data_b = read_txt_files_from_folder(folder_b, "TM")
    data_c = read_txt_files_from_folder(folder_c, "JP")
    # データ結合
    all_data = data_a + data_b + data_c
    # pandasのDataFrameに変換
    df = pd.DataFrame(all_data)
    # 確認
    print(df.head())

def preprogress(df):
    return df

def main():
    df = get_alldata()
    df = preprogress(df)

if __name__ == "__main__":
    main()