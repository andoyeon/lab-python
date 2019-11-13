"""
반복문 연습
"""
# Shift+F6: refactor/rename
# 1 + 2 + 3 + ... + 100 = ?
# numbers = []
# for i in range(1, 101):
#     numbers.append(i)
# print(sum(numbers))

sum = 0
for x in range(1, 101):
    sum += x
print(f'sum = {sum}')



# 1 + 2 + 3 + ... + x <= 100
n = 1
total = 0
while True:
    total += n
    print(f'n = {n}, sum = {total}')
    if total > 100:
        break
    n += 1


# 13번
for n in range(1, 8):
    print('T' * n)

# 14번
# 1)
for n in range(1, 8):
    print(' ' * (7-n), 'T' * n)

# 2)
for n in range(1, 8):
    for m in range(0, 8-n):
        if n + m == 8:
            break
    print(' ' * m, 'T' * n)


# 15번
