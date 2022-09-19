from copy import deepcopy
from collections import deque

# 입력받기
N = int(input())
target = list(map(int, input().split()))

# dfs를 통해 점수 구하기
used = [0]*N
dy = [-1, 0, 1]
path = []
Max = 0
def dfs(level):
    global used, Max, result
    if 0 not in used:
        total = sum(path)
        if total > Max:
            Max = total
            result = deepcopy(path)
        return
    for i in range(N):
        backup = deepcopy(used)
        if used[i] == 1: continue
        path.append(target[i])
        for j in range(3):
            ny = dy[j] + i
            if 0 <= ny < N:
                used[ny] = 1
        dfs(level+1)
        path.pop()
        used = deepcopy(backup)
dfs(0)

# 출력하기
q = deque(result)
for i in range(len(result)):
    add = q.popleft()
    q.append(add)
    q.append('+')
q.pop()
q.append('=')
q.append(Max)
print(*q, sep='')