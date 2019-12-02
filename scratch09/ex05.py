"""
gapminder.tsv 파일을 pandas 패키지의 read_csv() 함수를 사용해서
DataFrame으로 변환.
DataFrame의 행과 열의 개수 확인
DataFrame의 앞쪽 데이터 5개를 출력(head)
DataFrame의 뒤쪽 데이터 5개를 출력(tail)
DataFrame의 컬럼 이름들을 출력
DataFrame의 각 컬럼의 데이터 타입들을 출력
DataFrame에서 'country', 'lifeExp', 'gdpPercap' 컬럼들만 출력
DataFrame에서 행 인덱스가 0, 99, 999인 행들을 출력
DataFrame에서 행 레이블이 840~851인 행들의
나라 이름, 기대 수명, 1인당 GDP를 출력
DataFrame에서 연도(year)별 기대 수명의 평균을 출력
DataFrame에서 연도(year)별, 대륙(continent)별 기대 수명의 평균을 출력
"""
import os

import pandas as pd


file_path = os.path.join('gapminder.tsv')
df = pd.read_csv(file_path, delimiter='\t')
print('shape:', df.shape)   # 행:1704, 열:6
print(df.head())
print(df.tail())
print('data types:', df.dtypes)

print(df[['country', 'lifeExp', 'gdpPercap']])

rows = [0, 99, 999]
print(df.iloc[rows])

cols = ['country', 'lifeExp', 'gdpPercap']
print(df.loc[840:851, cols])

print('연도별 기대수명 평균')
print(df.groupby('year').mean()['lifeExp'])

print()
print('연도별, 대륙별 기대수명 평균')
print(df.groupby(['year', 'continent']).mean()['lifeExp'])
