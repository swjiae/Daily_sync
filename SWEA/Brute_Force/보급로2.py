from collections import deque

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
acc = [[0]*N for _ in range(N)]

q = deque()
q.append((0,0))
acc[0][0] = 1

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if acc[ny][nx] == 0 or acc[y][x] + arr[ny][nx] < acc[ny][nx]:
                acc[ny][nx] = acc[y][x] + arr[ny][nx]
                q.append((ny, nx))

print(acc[N-1][N-1]-1)

