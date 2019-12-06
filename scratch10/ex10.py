"""
ex10.py
"""
import requests
from bs4 import BeautifulSoup

# 접속할 사이트(웹 서버) 주소
url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&DA=YZR&spacing=0'

# 사이트(웹 서버)에 요청(request)를 보냄
html = requests.get(url).text.strip()   # 요청의 결과(응답, response - HTML)를 저장
print(html[0:100])  # 전체 문자열에서 100자만 확인

# HTML 문서의 모든 링크에 걸려 있는 주소들을 출력
# 관심 있는 링크(뉴스 링크)들만 찾을 수 있는 방법을 고민(주말 동안)
soup = BeautifulSoup(html, 'html5lib')
for link in soup('a'):
    print(link.get('href'))

