import numpy as np
import pandas as pd
import os

from scratch12.ex04 import summarize_by_class, calculate_class_probability, separate_by_class2


def train_test_split(df, test_size):
    """ df=데이터 프레임, test_size=테스트 세트의 비율
    학습 세트(X_train)와 검증 세트(X_test)를 리턴
    train/test set: 리스트 또는 np.ndarray
    [[x1, x2, ..., label1], [x1, x2, ..., label2], [], ...], [[], [], [], ...]
    """
    length = len(df)
    indices = [i for i in range(length)]
    np.random.shuffle(indices)

    cut = int(length * (1 - test_size))
    df_train = df.iloc[indices[:cut]]
    df_test = df.iloc[indices[cut:]]
    return np.array(df_train), np.array(df_test)



def predict(summaries, X_test):
    """ 테스트 세트의 예측값들의 배열(리스트)을 리턴
    [0, 1, 1, 2, 0, 0, 2, ...] """





if __name__ == '__main__':
    iris_file = os.path.join('..', 'scratch11', 'iris.csv')
    cancer_file = os.path.join('..', 'scratch11', 'wisc_bc_data.csv')

    # iris_dataset 레이블 값을 숫자로 변환
    iris_dataset = pd.read_csv(iris_file)
    for i in range(len(iris_dataset)):
        if iris_dataset.iloc[i, -1] == 'Iris-setosa':
            iris_dataset.iloc[i, -1] = 0
        elif iris_dataset.iloc[i, -1] == 'Iris-versicolor':
            iris_dataset.iloc[i, -1] = 1
        elif iris_dataset.iloc[i, -1] == 'Iris-virginica':
            iris_dataset.iloc[i, -1] = 2

    # 학습/테이트 데이터 분류
    iris_train, iris_test = train_test_split(iris_dataset, test_size=0.2)
    # print(iris_train)
    # print(iris_test)


    # print(iris_train[:, -1])

    summaries = summarize_by_class(iris_train)
    print(summaries)

    print(iris_train[0])
    probabilities = calculate_class_probability(summaries, iris_train[0])
    print(probabilities)

    # cancer_dataset = pd.read_csv(cancer_file)
