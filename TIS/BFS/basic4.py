from collections import deque

N = int(input()) # 5
arr = [[0]*N for _ in range(N)]
y1, x1, y2, x2= map(int, input().split()) # 4 1 2 6
level = 0
q = deque()
q.append([y1, x1, 0])
q.append([y2, x2, 0])

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while q:
    now = q.popleft()
    date = now[2]
    y, x = now[0], now[1]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if arr[ny][nx] == 0:
                arr[ny][nx] = arr[y][x]+1
                q.append([ny, nx, date+1])

print(date)