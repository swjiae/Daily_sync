from copy import deepcopy
from collections import deque

# direct 더 작으면 이동하면서 cnt+=1, max 갱신
def Climb(y, x):
    q = deque()
    q.append((y, x, 1))
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    while q:
        y, x, level = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] < arr[y][x]:
                    q.append((ny, nx, level+1))
    return level

# max 높이인 곳 좌표 찾기 start
def MAX(arr):
    Max = 0
    for y in range(N):
        for x in range(N):
            if arr[y][x] >= Max:
                Max = max(Max, arr[y][x])
    return Max


# 입력받기
N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
bu = deepcopy(arr)

# K 깎기
for i in range(N):
    for j in range(N):
        arr = deepcopy(bu)
        arr[i][j] = arr[i][j] - K
        tmp = MAX(arr)
        maxx = 0
        for yy in range(N):
            for xx in range(N):
                if arr[yy][xx] == tmp:
                    result = Climb(yy, xx)
                    maxx = max(maxx, result)

print(maxx)