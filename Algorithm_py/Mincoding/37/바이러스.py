from collections import deque

# 입력받기
N = int(input())
arr = [[0]*N for _ in range(N)]
y1, x1, y2, x2 = map(int, input().split())

# bfs를 이용한 바이러스 전파
q = deque()
q.append([y1, x1])
arr[y1][x1] = 1
q.append([y2, x2])
arr[y2][x2] = 1
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if arr[ny][nx] == 0:
                arr[ny][nx] = arr[y][x] + 1
                q.append([ny, nx])

# 출력하기
for i in range(N):
    print(*arr[i], sep='')