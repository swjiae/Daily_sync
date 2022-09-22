from collections import deque
# 입력받기
arr = [list(input()) for _ in range(7)]

# 새우, 오징어 위치 확인하기
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# pass or fail 출력하기
print('pass' if flag else 'fail')