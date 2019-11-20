"""
선형 대수(Linear Algebra)
"""
from math import sqrt

def add(v, w):
    """
    주어진 두 개의 n차원 벡터에서 성분별로 더하기를 해서,
    새로운 n차원 벡터를 리턴

    >>> add([1, 2], [3, 4])
    [4, 6]
    >>> add([1, 2, 3], [4, 5, 6])
    [5, 7, 9]

    :param v: n차원 벡터(성분이 n개인 벡터)
    :param w: n차원 벡터(성분이 n개인 벡터)
    :return: 각 성분별로 더하기 결과를 갖는 벡터
    """
    # result = []
    # for i in range(len(v)):
    #     result.append(v[i] + w[i])
    # return result
    if len(v) != len(w):
        raise ValueError('v와 w는 같은 length를 가져야 함.')
    return [l + l2 for l, l2 in zip(v, w)]


def subtract(v, w):
    """
    주어진 두 개의 n차원 벡터에서 성분별로 뺄셈을 수행

    >>> subtract([1, 2], [3, 4])
    [-2, -2]
    >>> subtract([10, 9, 8], [1, 2, 3])
    [9, 7, 5]

    :param v: n차원 벡터(성분이 n개인 벡터)
    :param w: n차원 벡터(성분이 n개인 벡터)
    :return: 각 성분별로 뺄셈 결과를 갖는 벡터
    """
    if len(v) != len(w):
        raise ValueError('v와 w는 같은 length를 가져야 함.')
    return [l - l2 for l, l2 in zip(v, w)]


def vector_sum(vectors):
    """
    모든 벡터들에서 각 성분별 합을 더하기를 수행
    vector_sum([1, 2], [3, 4], [5, 6]) = [9, 12]

    :param vectors: n차원 벡터들의 리스트(2차원 리스트)
    :return: n차원 벡터
    """
    num_of_elements = len(vectors[0])
    for vector in vectors[1:]:
        if num_of_elements != len(vector):
            raise ValueError('모든 벡터는 길이가 같아야 함.')

    # result = [0 for _ in range(num_of_elements)]    # [0, 0, 0, ...]
    # for i in range(num_of_elements):
    #     for vector in vectors:
    #         result[i] += vector[i]
    # return result
    result = vectors[0]
    for vector in vectors[1:]:
        result = add(result, vector)
    return result

# 벡터 스칼라 곱
def scalar_multiply(c, vector):
    """
    c * [x1, x2, x3, ...] = [c*x1, c*x2, c*x3, ...]

    :param c: 숫자(스칼라, scalar)
    :param vector: n차원 벡터(n개의 아이템을 갖는 1차원 리스트)
    :return: n차원 벡터
    """
    # result = []
    # for item in vector:
    #     result.append(c * item)
    # return result
    return [c * item for item in vector]

# 내적(dot product)
def dot(v, w):
    """
    [v1, v2, v3, ...] @ [w1, w2, w3, ...] = v1*w1 + v2*w2 + v3*w3 + ...

    :param v: n차원 벡터
    :param w: n차원 벡터
    :return: 숫자(스칼라)
    """
    if len(v) != len(w):
        raise ValueError('두 벡터의 길이(length)는 같아야 함.')
    sum = 0
    for v_i, w_i in zip(v, w):
            sum += v_i * w_i
    return sum


def vector_mean(vectors):
    """
    주어진 벡터들의 리스트에서 각 항목별 평균으로 이루어진 벡터

    :param vectors: n차원 벡터들의 리스트
    (길이가 n인 1차원 리스트를 아이템으로 갖는 2차원 리스트)
    :return: n차원 벡터(길이가 n인 1차원 리스트)
    """
    length = len(vectors)
    return scalar_multiply(1/length, vector_sum(vectors))


def sum_of_squares(vector):
    """
    vector = [x1, x2, ..., xn]일 때,
    x1 ** 2 + x2 ** 2 + ... xn ** 2을 리턴

    :param vector: n차원 벡터(길이가 n인 1차원 리스트)
    :return: 숫자
    """
    # return [x ** 2 for x in vector]
    # sum = 0
    # for v_i in vector:
    #     sum += v_i ** 2    # v_i * v_i
    # return sum
    return dot(vector, vector)


def magnitude(vector):
    """
    벡터의 크기를 리턴 - math.sqrt(sum_of_squares)

    :param vector:
    :return:
    """
    return sqrt(sum_of_squares(vector))


def squared_distance(v, w):
    """
    v = [v1, v2, ..., vn], w = [w1, w2, ..., wn]일 때,
    (v1-w1) ** 2 + (v2-w2) ** 2 + ... + (vn-wn) ** 2 리턴

    :param v: n차원 벡터(길이가 n인 1차원 리스트)
    :param w: n차원 벡터(길이가 n인 1차원 리스트)
    :return: 숫자
    """
    # sum = 0
    # for v_i, w_i in zip(v, w):
    #     sum += (v_i - w_i) ** 2
    # return sum
    return sum_of_squares(subtract(v, w))


def distance(v, w):
    """
    두 벡터 v와 w 사이의 거리를 리턴 - sqrt(squared_distance)

    :param v: n차원 벡터(길이가 n인 1차원 리스트)
    :param w: n차원 벡터(길이가 n인 1차원 리스트)
    :return: 숫자
    """
    return sqrt(squared_distance(v, w))


if __name__ == '__main__':
    v = [1, 2]
    w = [3, 4]

    result = add(v, w)
    print('add =', result)

    result2 = subtract(v, w)
    print('subtract =', result2)

    vectors = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result3 = vector_sum(vectors)
    print('vector_sum =', result3)

    vector = [1, 2, 3]
    result4 = scalar_multiply(5, vector)
    print('scalar_multiply =', result4)

    v = [2, 3]
    unit_x = [1, 0] # x축 단위 벡터
    unit_y = [0, 1] # y축 단위 벡터
    dot1 = dot(v, unit_x)
    dot2 = dot(v, unit_y)
    print('dot1 =', dot1)
    print('dot2 =', dot2)

    result5 = vector_mean(vectors)
    print('vector_mean =', result5)

    vector = [3, 4]
    result6 = sum_of_squares(vector)
    print('sum_of_squares =', result6)
    norm = magnitude(vector)
    print('magnitude =', norm)

    v = [1, 2]
    w = [3, 4]
    result7 = squared_distance(v, w)
    print('squared_distance =', result7)

    result8 = distance(v, w)
    print('distance =', result8)
