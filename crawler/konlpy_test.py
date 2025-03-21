import csv
import random

import wikipedia
from konlpy.tag import Okt


def get_random_korean_article():
    wikipedia.set_lang("ko")
    try:
        title = random.choice(wikipedia.random(pages=5))
        content = wikipedia.page(title).content
        return content
    except Exception as e:
        print(f"Error fetching Wikipedia page: {e}")
        return ""


# 형태소 분석
def extract_words(text):
    okt = Okt()
    nouns = []
    adjectives = []
    words = okt.pos(text, norm=True, stem=True)

    stopwords = set(['것', '수', '들', '하다', '되다', '같다', '그것', '있다', '없다', '우리', '너무', '이것'])

    for word, tag in words:
        if word in stopwords or len(word) < 2:
            continue
        if tag == 'Noun':
            nouns.append(word)
        elif tag == 'Adjective':
            adjectives.append(word)
    return list(set(adjectives)), list(set(nouns))


# csv 저장
def save_to_csv(adjectives, nouns, filename='nickname_words_auto.csv'):
    with open(filename, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["형용사", "명사"])
        for _ in range(min(len(adjectives), len(nouns))):
            writer.writerow([random.choice(adjectives), random.choice(nouns)])
    return filename


if __name__ == "__main__":
    text = get_random_korean_article()
    adjectives, nouns = extract_words(text)
    path = save_to_csv(adjectives, nouns)
    print(f"CSV 저장 완료: {path}")
