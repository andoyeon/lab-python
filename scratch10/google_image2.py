# 내장함수
import os
from urllib.request import urlopen
# 명령행 파싱 모듈 argparse 모듈 사용
import argparse
# request => 요청하는거를 웹에 요청한 결과값을 얻어올수 있는 모듈
import requests as req
# 웹에 요청한 결과를 보내주는 모듈
from bs4 import BeautifulSoup


def main(people):

    # 사용한 구글 url https://www.google.co.kr/search?q=%EB%B2%A4&tbm=isch

    url_info = "https://www.google.co.kr/search?q"

    #params에 딕션을 넣어줌
    params = {
        #명령행에서 받은 인자값을 people로 넣어줌
        "q" : people,
        "tbm":"isch"
    }
    #url 요청 파싱값
    html_object = req.get(url_info, params) #html_object html source 값

    if html_object.status_code == 200:
        #페이지 status_code 가 200 일때 2XX 는 성공을 이야기함
        bs_object = BeautifulSoup(html_object.text,"html.parser")
        #인스턴스 생성
        img_data = bs_object.find_all('img', {'src': True})
        print('img_data', img_data)
        #인스턴스의 find_all 이라는 함수에 img 태그가 있으면 img_data에 넣어줌

        i = 1
        for link in (img_data):
            if 'http' in str(link.attrs):  # 내부에 있는 항목들을 리스트로 가져옴
                t = urlopen(link.attrs['src']).read()
                # urllib.request.urlopen(i[1].attrs['src']).read()
                print('t', t)

                filename = 'jihyun' + str(i) + '.jpg'
                save_dir = os.path.join('..', 'dataset')
                if not os.path.exists(save_dir):
                    os.mkdir(save_dir)
                else:
                    save_img = os.path.join(save_dir, filename)
                    with open(save_img, "wb") as f:
                        f.write(t)
                    print("Img Save Success")
                    i += 1


        # for link in enumerate(img_data[1:]):
        #     print('link', link)
        #     print('link[1]', link[1])
        #     if 'src' in link[1]:  # 내부에 있는 항목들을 리스트로 가져옴
        #         # t = link.attrs['src']
        #         print('c', 'c')
        #         t = link[1].attrs['src']
        #         print('t', t)
        #         # filename = "jihyun" + str(link[0] + 1) + '.jpg'
        #         # with open(filename, "wb") as f:
        #         #     f.write(t)
        #         # print("Img Save Success")


if __name__=="__main__":
    people = '전지현'
    main(people)