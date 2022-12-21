from collections import deque

# 입력받기
Map = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 0, 1, 0]
]
sy, sx = map(int, input().split())
ey, ex = map(int, input().split())

# 최단 횟수 구하기
q = deque()
q.append([sy, sx, 0])
Map[sy][sx] = 1
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while q:
    y, x, level = q.popleft()
    if y == ey and x == ex: break
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < 4 and 0 <= nx < 4:
            if Map[ny][nx] == 1: continue
            Map[ny][nx] = 1
            q.append([ny, nx, level+1])

# 출력하기
print(f'{level}회')
