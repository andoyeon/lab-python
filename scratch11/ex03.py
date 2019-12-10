"""
ex03.py
"""
import numpy as np


def train_test_split(X, y, test_size):
    """
    :param X: numpy.ndarray. n x m
    :param y: numpy.ndarray. 원소의 개수가 n개인 1차원 배열
    len(X) == len(y) 가정.
    test_size: 0.0 ~ 1.0
    """
    length = len(X)
    # 인덱스를 저장하는 배열
    indices = np.array([i for i in range(length)])
    print('shuffle 전:', indices)
    # 인덱스를 임의로 섞음
    np.random.shuffle(indices)
    print('shuffle 후:', indices)
    # Train set의 개수
    cut = int(length * (1 - test_size)) # 소수점 버림
    X_train = X[indices[:cut]]  # Train set points
    y_train = y[indices[:cut]]  # Train set labels
    X_test = X[indices[cut:]]   # Test set points
    y_test = y[indices[cut:]]   # Test set labels
    return X_train, X_test, y_train, y_test


class MyScaler:
    def fit(self, X):
        """ X의 각 특성(컬럼)들의 평균과 표준 편차를 저장 """
        # 컬럼별로 평균을 계산해서 저장
        self.feature_means = np.mean(X, axis=0) # axis=0: 컬럼별 계산, axis=1: row별 계산
        # 컬럼별로 표준 편차를 계산해서 저장
        self.feature_stds = np.std(X, axis=0)
        print(self.feature_means)
        print(self.feature_stds)

    def transform(self, X):
        """ X의 평균을 0, 표준 편차를 1로 변환해서 리턴 """
        # X와 같은 크기를 갖는 배열을 생성.
        # 행(row)과 열(column)의 개수가 같은 배열을 생성.
        dim = X.shape
        transformed = np.empty(dim)
        for row in range(dim[0]):   # row 개수만큼 반복
            for col in range(dim[1]):   # column 개수만큼 반복
                # x_new = (x - mean) / std
                transformed[row, col] = (X[row, col] - self.feature_means[col]) / self.feature_stds[col]
        return transformed


class MyKnnClassifier:
    def __init__(self, n_neighbors=5):  # 객체 생성
        pass

    def fit(self, X_train, y_label):    # 모델 훈련
        pass

    def predict(self, X_test):  # 예측
        pass

    # 거리 계산 메소드(함수), 투표 메소드


if __name__ == '__main__':
    np.random.seed(1210)
    X = np.random.randint(10, size=(5, 2))  # Points
    print(X)
    y = np.array(['a', 'b', 'a', 'b', 'a']) # labels
    print(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    print(X_train)
    print(y_train)
    print(X_test)
    print(y_test)

    scaler = MyScaler() # 객체 생성
    scaler.fit(X_train) # 객체가 가지고 있는 메소드 호출
    X_train_scaled = scaler.transform(X_train)
    print(X_train_scaled)
    X_test_scaled = scaler.transform(X_test)
    print(X_test_scaled)