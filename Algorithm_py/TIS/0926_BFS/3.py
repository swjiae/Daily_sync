# flood fill - bfs (bloom / virus)

# direct
# 배열 범위
# 이미 꽃이 핀 곳

from collections import deque

N = int(input()) # 5
y, x = map(int, input().split()) # 3, 1
arr = [[0]*N for _ in range(N)]

q = deque()
q.append([y, x])
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

while q:
    now = q.popleft()
    y, x = now[0], now[1]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if arr[ny][nx] == 0:
                arr[ny][nx] = arr[y][x]+1
                q.append([ny, nx])

date = arr[0][0]
print(f'{date}일 후')