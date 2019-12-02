"""
1) csv 파일(stock_price.csv) write
6/20/2019,AAPL,90.91
6/20/2019,MSFT,41.68
6/21/2019,AAPL,90.86
6/21/2019,MSFT,41.51

2) csv 파일을 csv.reader를 사용해서 파일의 내용을 리스트로 변환
각 주식 종목의 주식 가격 평균을 계산해서 출력

3) csv 파일을 csv.DictReader를 사용해서 파일의 내용을 리스트로 변환
각 주식 종목의 주식 가격 평균을 계산해서 출력
"""
import csv

from numpy import mean

data = [
    ['6/20/2019','AAPL', 90.91],
    ['6/20/2019','MSFT', 41.68],
    ['6/21/2019','AAPL', 90.86],
    ['6/21/2019','MSFT', 41.51]
]

# 파일을 쓰기 모드로 열기
with open('stock_price.csv', mode='w', encoding='utf-8', newline='') as f:
    # csv writer 객체 생성
    writer = csv.writer(f, delimiter=',')
    # 리스트에서 아이템을 하나씩 반복
    for row in data:
        # CSV 형식으로 파일에 쓰기
        writer.writerow(row)


# 파일을 읽기 모드로 열기
with open('stock_price.csv', mode='r', encoding='utf-8') as f:
    # csv.reader 객체를 생성
    reader = csv.reader(f)
    # 파일에서 한 줄씩 읽어서 리스트에 추가
    df = [line for line in reader]
print(df)

# 'AAPL' 종목의 주식 가격들의 리스트
aapl_prices = [float(row[2]) for row in df if row[1] == 'AAPL']
aapl_avg = mean(aapl_prices)
print(f'aapl_avg: {aapl_avg}')

# 'MSFT' 종목의 주식 가격들의 리스트
msft_prices = [float(row[2]) for row in df if row[1] == 'MSFT']
msft_avg = mean(msft_prices)
print(f'msft_avg: {msft_avg}')


with open('stock_price.csv', mode='r', encoding='utf-8') as f:
    # csv.DictReader 객체를 생성
    # csv 파일에 컬럼 이름이 없는 경우,
    # 생성자의 fieldnames 파라미터에 컬럼 이름 값들을 전달하면 됨.
    col_names = ['date', 'stock', 'price']
    reader = csv.DictReader(f, fieldnames=col_names)
    df = [row for row in reader]

print(df)

aapl_prices = [float(row['price']) for row in df if row['stock'] == 'AAPL']
aapl_avg = mean(aapl_prices)
print(f'aapl_avg: {aapl_avg}')

msft_prices = [float(row['price']) for row in df if row['stock'] == 'MSFT']
msft_avg = mean(msft_prices)
print(f'msft_avg: {msft_avg}')