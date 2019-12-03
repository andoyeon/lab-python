"""
ex06.py
"""
# gapminder.tsv 파일을 읽어서 데이터 프레임 생성
import pandas as pd
import os

df = pd.read_csv('gapminder.tsv', sep='\t', encoding='UTF-8')
print(df.iloc[0:5])

# boolean indexing:
# 컬럼의 값을 이용해서 특정 레코드(행, row)들을 선택하는 방법
# DataFrame[컬럼의 값을 이용한 조건식]
# SQL: select * from DataFrame where column == '';
df_afg = df[df['country'] == 'Afghanistan']
print(df_afg)

df_korea = df[df['country'] == 'Korea, Rep.']
print(df_korea)

# 대한민국(Korea, Rep.)의 인구(pop)과 1인당 GDP(gdpPercap)을 출력
# print(df_korea[['pop', 'gdpPercap']])
print(df[df['country'] == 'Korea, Rep.'][['pop', 'gdpPercap']])

# mpg.csv 파일을 읽어서 DataFrame을 생성
file_path = os.path.join('..', 'scratch08', 'mpg.csv')
mpg = pd.read_csv(file_path, encoding='UTF-8')
print(mpg.dtypes)

# cty 컬럼의 평균을 계산
print(type(mpg['cty'])) # mpg['cty']의 데이터 타입: Series
print(mpg['cty'])

print(type(mpg[['cty']]))   # mpg[['cty']]의 데이터 타입: DataFrame
print(mpg[['cty']]) # select cty from mpg;

cty_mean = mpg['cty'].mean()
print('cty mean:', cty_mean)    # cty mean: 16.858974358974358

# cty 컬럼의 값이 crt 평균보다 큰 레코드들을 출력
mpg_cty_above = mpg[mpg['cty'] >= cty_mean]
print(mpg_cty_above)

# cty가 평균 이상인 자동차들의 model, displ, cty, hwy 컬럼을 출력
print(mpg_cty_above[['model', 'displ', 'cty', 'hwy']])