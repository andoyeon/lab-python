# 1부터 n까지 숫자들의 합을 리턴하는 함수
# 1 +2 + 3 + ... + n
# def fun_sum(*numbers: int) -> int:
#     total = 0
#     for num in numbers:
#         total += num
#     return total


# print(fun_sum(10, 20, 50))


def sum_to_n(n: int) -> int:
    return n * (n + 1) / 2


result = sum_to_n(10)
print(result)


def sum_to_n2(n:int) -> int:
    _sum = 0
    for x in range(1, n+1):
        _sum += x
    return _sum


result = sum_to_n2(10)
print(result)



def sum_to_n3(n:int) -> int:
    numbers = [x for x in range(1, n + 1)]
    print(numbers)
    return sum(numbers)


result = sum_to_n3(10)
print(result)


print()
# 1부터 n까지 숫자들의 제곱의 합을 리턴하는 함수
# 1**2 + 2**2 + 3**2 + ... + n**2
# def sum_of_squared(n:int) -> int:
#    total = 0
#    for num in range(1, n+1):
#        total += num**2
#    return total
#
#
# print(sum_of_squared(5))


def sum_to_squares(n: int) -> float:
    return n * (n+1) * (2*n + 1) / 6


def sum_to_squares2(n:int) -> int:
    _sum = 0
    for x in range(1, n+1):
        _sum += x**2
    return _sum


print(sum_to_squares(3))
print(sum_to_squares2(3))

print()
# 숫자들의 리스트를 전달받아서 최대값을 찾아서 리턴하는 함수
# def f_max(numbers:list) -> float:
#     max = numbers[0]
#     for num in numbers:
#         if max < num:
#             max = num
#     print(f'max = {max}')
#
#
# f_max([10, 20, 50, 80, 40])
def find_max(values:list) -> float:
    _max = values[0]
    # for x in values:
    #     if x > _max:
    #         _max = x
    for i in range(1, len(values)):
        if values[i] > _max:
            _max = values[i]
    return _max


numbers = [10, 95, 35, 25, 80]
print(find_max(numbers))


def find_max2(values:list) -> float:
    # sorted(list): list를 정렬한 새로운 리스트를 리턴
    # 원본 리스트(list)는 순서가 그대로 유지됨
    # list.sort(): 원본 리스트를 정렬해서 순서를 바꿈
    # None을 리턴함(값을 리턴하지 않음)
    sorted_values = sorted(values, reverse=True)    # reverse=True 내림차순 정렬
    print('values:', values)
    print('sorted_values', sorted_values)
    # return sorted_values[0]
    values.sort(reverse=True)       # values = values.sort() 는 None값을 가짐
    print('values:', values)
    return values[0]

print(find_max2(numbers))


print()

# 숫자들의 리스트를 전달받아서 최대값의 인덱스를 리턴하는 함수
def find_max_index(values:list) -> float:
    max_id, max_val = 0, values[0]
    for i, v in enumerate(values):      # enumerate 리스트 인덱스와 값을 전달
        print(f'i = {i}, v = {v}')
        if v > max_val:
            max_id, max_val = i, v
    return max_id


numbers = [80, 90, 99, 77, 100]
print(find_max_index(numbers))


def find_max_index2(values):
    _max = values[0]
    max_id = 0
    for i in range(1, len(values)):
        if values[i] > _max:
            _max = values[i]
            max_id = i
    return max_id


print(find_max_index2(numbers))


def find_max_index3(values):
    max_id, _max = 0, values[0]
    idx = 0
    for x in values:
        if x > _max:
            max_id, _max = idx, x
        idx += 1
    return max_id


print(find_max_index3(numbers))




print()
# 숫자들의 리스트를 전달받아서 중앙값을 리턴하는 함수(리스트 갯수 홀/짝에 따라 다르게)
# def median(numbers:list):
#    sorted_numbers = sorted(numbers)
#    result = None
#    if len(sorted_numbers) % 2 == 1:     # 홀수
#        result = sorted_numbers[int(max_index(sorted_numbers) / 2)]
#    elif len(sorted_numbers) % 2 == 0:    # 짝수
#        result = (sorted_numbers[int(max_index(sorted_numbers) / 2) - 1] +
#                 sorted_numbers[int(max_index(sorted_numbers) / 2)]) / 2
#    return result
#
#
# result = median([70, 20, 90, 100, 30])
# print(f'median = {result}')
#
# print(sorted([70, 20, 90, 100, 30, 50]))
# result = median([70, 20, 90, 100, 30, 50])
# print(f'median = {result}')


def median(values:list) -> float:
    # 리스트를 정렬(내림차순)
    sorted_values = sorted(values)
    length = len(sorted_values)   # 리스트의 크기
    mid = length // 2   # 리스트의 중간 위치
    if length % 2:  # 리스트의 원소 갯수가 홀수인 경우
        median_value = sorted_values[mid]
    else:   # 리스트의 원소 갯수가 짝수인 경우
        left = mid - 1
        median_value = (sorted_values[left] + sorted_values[mid]) / 2
    return median_value


numbers = [7, 5, 6, 4, 9]
print(median(numbers))
numbers = [7, 5, 6, 4, 9, 10]
print(median(numbers))


