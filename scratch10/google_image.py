import numpy
import requests
from lxml.html import parse
from io import StringIO
import os, sys
from PIL import Image
import urllib.request


# 검색할 이미지의 키워드 입력
keyword = input("검색할 이미지를 입력하세요 : ")
url = 'https://www.google.co.kr/search?q='+keyword+'&source=lnms&tbm=isch&sa=X&ved=0ahUKEwic-taB9IXVAhWDHpQKHXOjC14Q_AUIBigB&biw=1842&bih=990'


# html 소스 가져오기
text = requests.get(url).text

# html 문서로 파싱
text_source = StringIO(text)
parsed = parse(text_source)

# root node
doc = parsed.getroot()

# img 경로는 img 태그안에 src에 있음
imgs = doc.findall('.//img')

img_list = []   # 이미지 경로가 담길 list
for a in imgs:
    img_list.append(a.get('src'))
    print(a.get('src'))

print(img_list)

for url in img_list:
    name = 'test'
    fullname = name + '.jpg'
    urllib.request.urlretrieve(url, fullname)

