"""
사건의 종속성 vs 독립성
사건 A의 발생 여부가 사건 B의 발생 여부에 대한 정보를 제공한다면,
사건 A와 사건 B는 종속 사건(dependent event).
사건 A의 발생 여부가 사건 B의 발생 여부와 상관이 없다면,
사건 A와 사건 B는 독립 사건(independent event).

동전 2개를 던지는 경우,
A: 첫번째 동전이 앞면
B: 두번째 동전이 뒷면
C: 두 동전 모두 뒷면(앞면)
A와 B는 독립 사건.
A와 C는 종속 사건.

P(A): 사건 A가 일어날 확률
P(B): 사건 B가 일어날 확률
P(A,B): 사건 A와 사건 B의 교집합이 일어날 확률

P(A,B) = P(A) * P(B)이 성립하면, 두 사건은 독립 사건.
"""
from collections import Counter

from scratch06.ex01 import experiment

# 자녀가 2명인 경우,
# A: 첫째가 딸인 경우
# B: 둘째가 아들인 경우
# C: 둘 다 딸인 경우
# A와 B가 독립 사건, A와 C는 종속 사건임을 증명
# P(A), P(B), P(C), P(A, B), P(A, C)

child = [1, 0]   # 1: 딸, 0: 아들
exp = experiment(child, 2, 10_000)
counts = Counter(exp)
trials = 10_000

num_of_counts = 0
for ev, cnt in counts.items():
    if ev[0] == 1: # 첫째가 딸인 경우
        num_of_counts += cnt
p_a = num_of_counts / trials
print('P(A) =', p_a)

num_of_counts = 0
for ev, cnt in counts.items():
    if ev[1] == 0: # 둘째가 아들인 경우
        num_of_counts += cnt
p_b = num_of_counts / trials
print('P(B) =', p_b)

num_of_counts = 0
for ev, cnt in counts.items():
    if ev[0] == 1 and ev[1] == 1: # 둘 다 딸인 경우
        num_of_counts += cnt
p_c = num_of_counts / trials
print('P(C) =', p_c)

num_of_counts = 0
for ev, cnt in counts.items():
    if ev[0] == 1 and ev[1] == 0:
        num_of_counts = cnt
p_ab = num_of_counts / trials
print('P(A, B) =', p_ab, 'P(A)P(B) =', p_a * p_b)

num_of_counts = 0
for ev, cnt in counts.items():
    if ev[0] == 1 and (ev[0] == 1 and ev[1] == 0):
        num_of_counts = cnt
p_ac = num_of_counts / trials
print('P(A, C) =', p_ac, 'P(A)P(C) =', p_a * p_c)