"""
ex02.py
R을 활용한 머신 러닝 - 암 데이터 파일(csv)
scikit-learn 패키지 활용, kNN 결과
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

if __name__ == '__main__':
    print('\n=== 1. 데이터 준비 ===')
    dataset = pd.read_csv('wisc_bc_data.csv')
    print(dataset.shape)
    print(dataset.info())   # 569 x 32
    print(dataset.describe())   # scaling이 필요
    print(dataset.head())

    print('\n=== 2. 데이터 전처리 ===')
    # n차원 상의 point와 레이블로 구분
    # X = 전체 행, id, diagnosis를 제외한 나머지 모든 열 데이터
    X = dataset.iloc[:, 2:].to_numpy()
    # y = 전체 행, diagnosis 열 데이터
    y = dataset.iloc[:, 1].to_numpy()
    print(X[0])
    print(y[0])

    # train/test set로 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    print(len(X_train), len(X_test), len(y_train), len(y_test))

    print('\n=== 3. 표준화 ===')
    # Scaling
    scaler = StandardScaler()
    scaler.fit(X_train) # X_train 세트의 평균/표준편차 계산
    X_train = scaler.transform(X_train) # 학습 세트 변환
    X_test = scaler.transform(X_test)   # 테스트 세트 변환
    print(np.mean(X_train[:, 0]), np.std(X_train[:, 0]))

    print('\n=== 4. 학습/예측 ===')
    # k-NN 분류기 생성
    classifier = KNeighborsClassifier(n_neighbors=15)
    # 분류기 학습
    classifier.fit(X_train, y_train)
    # 검증 데이터의 예측 결과 추출
    y_pred = classifier.predict(X_test)
    print(y_pred)

    print('\n=== 5. 모델 평가 ===')
    conf_matrix = confusion_matrix(y_test, y_pred)  # 혼동 행렬
    print(conf_matrix)
    report = classification_report(y_test, y_pred)
    print(report)

    print('\n=== 6. 모델 개선(향상) ===')
    # k값 변경에 따른 모델 성능
    errors = []
    for i in range(1, 41):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train, y_train)
        pre_i = knn.predict(X_test)
        errors.append(np.mean(pre_i != y_test))
    print(errors)

    # a = np.array([1, 2, 3])
    # b = np.array([1, 4, 6])
    # print(a != b)
    # print(np.mean(a != b))

    # error값 그래프
    plt.plot(range(1, 41), errors, marker='x')
    plt.title('Mean Error with K-Value')
    plt.xlabel('k-value')
    plt.ylabel('mean error')
    plt.show()





