"""
while 반복문:
[초기식]
while 조건식:
    조건식이 참인 동안에 실행할 문장
    [조건을 변경할 수 있는 식]
"""
# 1 2 3 ... 10
n = 1
while n <= 10:
    print(n, end=' ')
    n += 1  # n = n + 1
print()


n = 1
while n < 10:
    print(f'2 x {n} = {2 * n}')
    n += 1

# 2중 while문을 사용해서 2단부터 9단까지 출력
n = 2
while n < 10:
    m = 1
    while m < 10:
        print(f'{n} x {m} = {n * m}')
        if n == m:
            break
        m += 1
    n += 1
    print('----------')