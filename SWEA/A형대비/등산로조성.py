from copy import deepcopy
from collections import deque

# direct 더 작으면 이동
def Climb(y, x):
    q = deque()
    max_level = 0
    q.append((y, x, 1))
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    while q:
        y, x, level = q.popleft()
        max_level = max(level, max_level)
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] < arr[y][x]:
                    q.append((ny, nx, level+1))
    return max_level


# max 높이인 곳 좌표 찾기 start
def Max(arr):
    max_loc = 0
    for y in range(N):
        for x in range(N):
            if arr[y][x] >= max_loc:
                max_loc = max(max_loc, arr[y][x])
    return max_loc


# 입력받기
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    bu = deepcopy(arr)


    # K 깎기
    max_len = 0
    for i in range(N):
        for j in range(N):
            arr = deepcopy(bu)
            arr[i][j] = max(arr[i][j] - K, 0)
            max_loc = Max(arr)
            for sy in range(N):
                for sx in range(N):
                    if arr[sy][sx] == max_loc:
                        result = Climb(sy, sx)
                        max_len = max(max_len, result)

    print(f'#{t}', max_len)