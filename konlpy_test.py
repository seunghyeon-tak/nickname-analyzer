from konlpy.tag import Okt

okt = Okt()
text = "용감한 고양이가 춤추는 냉장고를 바라보았다."
print(okt.pos(text))
