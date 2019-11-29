"""
1) R의 ggplot2 패키지에 포함된 mpg 데이터 프레임을 csv 파일 형식으로 저장
2) 저장된 csv 파일을 파이썬 프로젝트의 scratch08 폴더에 복사
3) 저장된 csv 파일을 읽어서 배기량(displ) [4]과 시내 연비(cty) [8]
    데이터를 추출
4) 선형 회귀식
	cty = slope * displ + intersect
    의 기울기(slope)와 절편(intersect)을 경사 하강법의 3가지 방법
    (stochastic, batch, mini-batch)으로 결정하고 값을 비교
5) 배기량과 시내 연비 산점도 그래프(scatter plot)과 선형 회귀 직선을 하나의 plot으로 출력해서 결과 확인
"""
import csv
import random

from scratch08.ex03 import gradient_step
from scratch08.ex04 import linear_gradient

import matplotlib.pyplot as plt

"""
line_counter = 0
header = []
mpg_list = []
with open('mpg.csv') as mpg:
    while True:
        line = mpg.readline()
        if not line:
            break
        if line_counter == 0:
            header = line.split(",")
        else:
            mpg_list.append(line.split(","))
        line_counter += 1

print('header: ', header)
print('mpg_list: ', mpg_list)
"""
line_counter = 0
header = []
mpg_list = []
displ_data = []
cty_data = []

with open('mpg.csv') as mpg:
    mpg_data = csv.reader(mpg)
    for row in mpg_data:
        if line_counter == 0:
            header = row
        else:
            displ_data.append(float(row[3]))
            cty_data.append(int(row[8]))
        line_counter += 1



print(f'header = {header}')
print(f'displ = {displ_data}')
print(f'cty = {cty_data}')

# 그래프
plt.scatter(displ_data, cty_data)
plt.show()


# 4) 선형 회귀식
#	cty = slope * displ + intersect
#    의 기울기(slope)와 절편(intersect)을 경사 하강법의 3가지 방법
# dataset = [(displ, 5 * cty + 1) for displ in displ_data for cty in cty_data]

dataset = [(cty, displ) for displ in displ_data for cty in cty_data]
print(dataset[0:5])


if __name__ == '__main__':
    print('=== 확률적 경사 하강법 ===')
    theta = [10, 1]
    step = 0.001

    for epoch in range(1000):
        random.shuffle(dataset)
        for x, y in dataset:
            gradient = linear_gradient(x, y, theta)
            theta = gradient_step(theta, gradient, -step)
        if (epoch + 1) % 100 == 0:
            print(f'{epoch}: {theta}')






