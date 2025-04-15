#20250410 4-2-1
print("print html")
html = """ 
<html>
    <body>
        これは <a href="http://example.com">Example</a>です。
    </body>
</html>
"""
print(html)

from bs4 import BeautifulSoup

def clean_html(html, strip=False):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text(strip=strip)
    return text

sol = clean_html(html)
print("print sol")
print(sol)

import re
text = '今度からMkDosでドキュメント書こう.#Pthon'

def clean_hashtag(text):
    cleaned_text = re.sub(r'#[a-zA-Z]+', '', text)
    return cleaned_text#[a-zA-Z]+aned_text

print('He\nllo')
print(r'he\nllo')
print(clean_hashtag(text))

text = '機器学習やるなら#Python がいいよね。#jupyter'
print(clean_hashtag(text))

#page 64
#def clean_hashtag_new(text):
#    clean_text = re.sub(r' #[a-zA-Z]+$', '', text)
#    clean_text = re.sub(r' #[a-zA-Z] ', r'\1', clean_text)
#    return clean_text

#print(clean_hashtag_new(text))

#4-2-2
#形態素解析
from janome.tokenizer import Tokenizer
text = '彼女と国立新美術館へ行った'

t = Tokenizer()
print(type(t))
for token in t.tokenize(text):
    print(token)

t1 = Tokenizer(wakati=True)
word_list_tokenize = t1.tokenize(text)
list_new = []
for worlist in word_list_tokenize:
    list_new.insert(len(list_new), worlist)
    
print(list_new)

print(word_list_tokenize)

from janome.analyzer import Analyzer
from janome.tokenfilter import POSKeepFilter

token_filters = [POSKeepFilter('名詞')]
a = Analyzer(token_filters=token_filters)
for token in a.analyze(text):
    print(token)
    
#辞書定義　PAGE 68
#自分定義の辞書を使って、文章を形態素解析を行う
my_tokenizer = Tokenizer(udic="userdic.csv", udic_enc="utf-8")
for token in my_tokenizer.tokenize(text):
    print(token)

#4-2 3-1
#単語正規化
#正規化とは？単語の文字種を統一、単語を置き換える処理をする　(同じ種の文字処理しやすい)
#PYTHONで小文字の処理を行う(英語) 
text_p70_1 = "President Obama is speaking at the White House"
print(text_p70_1.lower())
print(text_p70_1.upper())
print(text_p70_1.title())

#4-2 3-2
#数字置き換え
