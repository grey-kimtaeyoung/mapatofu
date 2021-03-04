from urllib.request import urlopen
from bs4 import BeautifulSoup

## for문 기본 문법

# things = ['사과', '포도', '딸기', '과자']

# for thing in things:
#     print(thing)


## 리스트 안에 들어있는 값들을 돌아가며 출력 해주는 코드

# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     # len : 전달된 변수의 길이를 확인
#     print(w, len(w))


## 언론사 url 리스트를 돌아가며 호출

# media_urls = ['http://www.hcsinmoon.co.kr/',
#               'http://www.kbsm.net/',
#               'http://www.busan.com/']

# for url in media_urls:
#     html = urlopen(url)
#     bsObject = BeautifulSoup(html, "html.parser")
#     print(bsObject)
#     break
