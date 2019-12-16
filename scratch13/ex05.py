"""
ex05.py
Boston house prices dataset
"""
import numpy as np
from sklearn import linear_model
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt

# 보스턴 집값 데이터 세트 로딩
from sklearn.preprocessing import PolynomialFeatures

datasets = load_boston()
X = datasets.data
y = datasets.target
print('X[5] =', X[:5])
print('y[5] =', y[:5])
features = datasets.feature_names
print('feature names:', features)

print('X shape:', X.shape)
print('y shape:', y.shape)


# 데이터 탐색 -> 그래프
fig, ax = plt.subplots(3, 5)
# ax: 3x5 형태의 2차원 배열(ndarray)
ax_flat = ax.flatten()
for i in range(len(features)):
    subplot = ax_flat[i]
    subplot.scatter(X[:, i], y)
    subplot.set_title(features[i])
plt.show()



# 학습 세트/검증 세트 나눔
X_train = X[:-50]
X_test = X[-50:]
y_train = y[:-50]
y_test = y[-50:]

# 학습 세트를 사용해서 선형 회귀 - 단순 선형 회귀, 다중 선형 회귀
# 검증 세트를 이용해서 예측 -> 그래프
# y ~ RM
RM = X[:, np.newaxis, 5]
print('RM.shape:', RM.shape)
print('RM[5] =', RM[:5])

RM_train = RM[:-50]
RM_test = RM[-50:]

lin_reg = linear_model.LinearRegression()
lin_reg.fit(RM_train, y_train)
print('Coefficients:', lin_reg.coef_)   # 9.15398367

y_pred = lin_reg.predict(RM_test)

plt.scatter(RM_test, y_test)    # 실제값
plt.plot(RM_test, y_pred, 'ro-')    # 예측값
plt.title('House Price vs RM')
plt.xlabel('RM')
plt.show()

# MSE 계산


# y ~ DIS
DIS = X[:, np.newaxis, 7]
DIS_train = DIS[:-50]
DIS_test = DIS[-50:]

lin_reg.fit(DIS_train, y_train)
print('Coefficients:', lin_reg.coef_)   # 1.00229568

y_pred = lin_reg.predict(DIS_test)

plt.scatter(DIS_test, y_test)
plt.plot(DIS_test, y_pred, 'ro-')
plt.title('House Price vs DIS')
plt.xlabel('DIS')
plt.show()

# y ~ LSTAT
LSTAT = X[:, np.newaxis, 12]
LSTAT_train = LSTAT[:-50]
LSTAT_test = LSTAT[-50:]

lin_reg.fit(LSTAT_train, y_train)
print('Coefficients:', lin_reg.coef_)   # -0.95763084

y_pred = lin_reg.predict(LSTAT_test)

plt.scatter(LSTAT_test, y_test)
plt.plot(LSTAT_test, y_pred, 'ro-')
plt.title('House Price vs LSTAT')
plt.xlabel('LSTAT')
plt.show()


# y ~ RM + DIS
# X = np.c_[RM, DIS]
# print('X[5] =', X[:5])
#
# poly_feature = PolynomialFeatures(degree=2, include_bias=False)
# X_poly = poly_feature.fit_transform(X)
# print('X poly =', X_poly[:5])
#
# X_train = X_poly[:-50]
# X_test = X_poly[-50:]
#
# lin_reg.fit(X_train, y)
# print('절편(intercept) =', lin_reg.intercept_)
# print('계수(coefficients) =', lin_reg.coef_)
#
# y_pred = lin_reg.predict(X_test)
# print(y_pred[:5])

# plt.scatter(X_test, y_test)
# plt.plot(X_test, y_pred)
# plt.title('House Price ~ RM + DIS')
# plt.xlabel('RM + DIS')
# plt.show()

# Mean Square Error 계산


# R2-score 계산

