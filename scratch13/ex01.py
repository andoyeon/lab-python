"""
ex01.py
"""
from sklearn.datasets import load_diabetes

# X, y = load_diabetes(return_X_y=True)
# print(X[:5])
# print(X.shape, y.shape)

datasets = load_diabetes()
X = datasets.data
y = datasets.target
print(X.shape, y.shape)
features = datasets.feature_names
print(features)
print(X[0])
# 모든 특성(컬럼)들이 평균=0, 표준편차=1 로 전처리가 되어 있는 데이터 세트.
print(y[0])

# 선형 회귀(linear regression)
# y = b + a * x
# y = b0 + b1 * x1 + b2 * x2 + ...

# 1개의 figure에 10개의 subplot를 그려서, 변수들과 당뇨병(y)의 대략적인 관계를 파악.
# y ~ age, y ~ sex, y ~ bmi, ...

