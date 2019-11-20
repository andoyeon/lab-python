"""
2차원 리스트를 이용한 행렬
"""


def shape(matrix):
    """
    행렬의 행과 열의 개수를 tuple 형태로 리턴

    :param matrix: n x m 행렬
    (행의 개수가 n개 이고, 열의 개수가 m개인 2차원 리스트)
    :return: tuple (n, m)
    """
    nrows = len(matrix) # 행의 개수
    ncols = len(matrix[0])  # 열의 개수
    return nrows, ncols


def get_row(matrix, index):
    """
    주어진 행렬(matrix)에서 index에 해당하는 row를 리턴

    :param matrix: n x m 행렬
    :param index: 행 번호
    :return: 벡터(원소가 m개인 1차원 리스트)
    """
    return matrix[index]

def get_column(matrix, index):
    """
    주어진 행렬에서 index에 해당하는 column을 리턴

    :param matrix: n x m 행렬
    :param index: 행 인덱스
    :return: 벡터(원소가 n개인 1차원 리스트)
    """
    # result = []
    # for x in matrix:
    #     result.append(x[index])
    # return result
    return [x[index] for x in matrix]


def make_matrix(nrows, ncols, fn):
    """
    함수 fn의 리턴값들로 이루어진 nrows x nclos 행렬을 완성

    :param nrows: 행의 개수
    :param ncols: 열의 개수
    :param fn: 함수(fn(nrows, ncols) = 숫자)
    :return: nrows x ncols 행렬
    """
    # matrix = [] # 빈 리스트 생성 -> 2차원 리스트
    # for i in range(nrows):    # 행의 개수만큼 반복
    #     row = []    # 빈 리스트 생성 -> 행렬에 추가될 행. 1차원 리스트
    #     for j in range(ncols):    # 열의 개수만큼 반복
    #         row.append(fn(i, j))    # row에 아이템을 추가
    #     matrix.append(row)  # 행렬에 row를 추가
    # return matrix
    return [[fn(i, j) for j in range(ncols)] for i in range(nrows)]


# 전치행렬(transpose)
def transpose(matrix):
    """
    주어진 행렬에서 행과 열을 뒤바꾼 행렬(전치 행렬)을 리턴

    :param matrix: n x m 행렬
    :return: m x n 행렬
    """
    # return [i for i in zip(*matrix)]



if __name__ == '__main__':
    # 2x3 행렬(row=2, column=3)
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    # 3x2 행렬(row=3, column=2)
    B = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

    print(A)
    print('Shape of A =', shape(A)) # (2, 3)
    print(B)
    print('Shape of B =', shape(B)) # (3, 2)

    print(get_row(B, 0))
    print(get_column(B, 0))

    def plus(x, y):
        return x + y

    m = make_matrix(3, 2, plus)
    print(m)

    m = make_matrix(2, 2, lambda i, j: i * j)
    print(m)

    # 항등행렬(Identity)
    def identity(x, y):
        # if x == y:
        #     result = 1
        # else:
        #     result = 0

        # result = 1 if x == y else 0 # 3항 연산자
        # return result

        return 1 if x == y else 0

    identity_matrix = make_matrix(3, 3,
                                  lambda x, y: 1 if x == y else 0)
    print(identity_matrix)

    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print('A =', A)
    test = transpose(A)
    print('test =', test)