import string
import pandas as pd

def filter_by_ascii_rate(text, threshold=0.9):
    ascii_letters = set(string.printable)
    rate = sum( c in ascii_letters for c in text ) / len(text)
    return rate <= threshold

def load_dataset(filename, n=5000, state=6):
    df = pd.read_csv(filename, sep="\t")

    is_jp = df.review_body.apply(filter_by_ascii_rate)
    df = [is_jp]

    return