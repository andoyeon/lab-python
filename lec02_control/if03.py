"""
가위(1)/바위(2)/보(3)
"""
import numpy as np


print('가위 바위 보 게임')
print('[1] 가위')
print('[2] 바위')
print('[3] 보')
print('---------------')
print('선택>>')

user = int(input())

computer = np.random.randint(1, 4)  # 1 <= com < 4 난수
print(computer)

# 1)
if user == 1:
    if computer ==1:
        print('무')
    elif computer ==2:
        print('computer 승')
    else:
        print('user 승')
elif user == 2:
    if computer ==1:
        print('user 승')
    elif computer ==2:
        print('무')
    else:
        print('computer 승')
else:
    if computer ==1:
        print('computer 승')
    elif computer ==2:
        print('user 승')
    else:
        print('무')

# 2)
if user == computer:
    pass
elif user == 1:
    if computer ==2:
        pass
    else:   # computer == 3
        pass
elif user == 2:
    if computer ==1:
        pass
    else:   # computer == 3
        pass
else:
    if computer ==1:
        pass
    else:   # computer == 2
        pass

# 3)
result = user - computer
if result == 0:     # 비김
    pass
elif result == 1 or result == -2:   # user
    pass
else:
    pass
