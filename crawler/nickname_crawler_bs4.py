
import requests
from bs4 import BeautifulSoup
from konlpy.tag import Okt
import csv

# 키워드 기반 위키 문서 수집
wiki_keywords = [
    "사랑", "감정", "기억", "별", "햇살", "바람", "고양이", "눈물", "기쁨", "행복", "희망", "위로"
]

okt = Okt()
adjectives = set()
nouns = set()

def is_emotional_adjective(word):
    return word.endswith("은") or word.endswith("는") or word.endswith("운")

def is_valid_noun(word):
    return (
        len(word) >= 2 and
        not word.endswith("도") and
        not word.endswith("시") and
        not word.endswith("청") and
        word not in ["충청북도", "서울특별시", "묘비"]
    )

for keyword in wiki_keywords:
    try:
        url = f"https://ko.wikipedia.org/wiki/{keyword}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.select("p")
        text = " ".join(p.get_text() for p in paragraphs)
        morphs = okt.pos(text)

        for word, pos in morphs:
            if pos == "Adjective" and is_emotional_adjective(word):
                adjectives.add(word)
            elif pos == "Noun" and is_valid_noun(word):
                nouns.add(word)
    except Exception as e:
        print(f"{keyword} 처리 실패: {e}")

# CSV 저장
with open("../emotional_adjectives.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["형용사"])
    for adj in sorted(adjectives):
        writer.writerow([adj])

with open("../emotional_nouns.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["명사"])
    for noun in sorted(nouns):
        writer.writerow([noun])
