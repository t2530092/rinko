import re
def clean_text(text):
    # 去除换行符、制表符
    text = text.replace("\n", "").replace("\r", "").replace("\t", "")
    # 删除控制字符和不可见字符（ASCII < 32 除了常规空格）
    text = re.sub(r"[\x00-\x1F\x7F]", "", text)
    # 可选：去除全角空格、奇异标点、其他特殊符号（按需调整）
    text = re.sub(r"[^\x00-\x7F\u3000-\u30FF\u4E00-\u9FFF\uFF00-\uFFEF]", "", text)
    return text