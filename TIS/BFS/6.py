from collections import deque

Map = [
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 0, 1, 1]
]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    q = deque()
    q.append([y, x])
    Map[y][x] = 0
    size = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 5 and 0 <= nx < 5:
                if Map[ny][nx] == 1:
                    q.append([ny, nx])
                    Map[ny][nx] = 0
                    size += 1
    return size

cnt = 0
SIZE = []
for y in range(5):
    for x in range(5):
        if Map[y][x] == 1:
            cnt += 1
            SIZE.append(bfs(y, x))

print('큰 섬:',max(SIZE))
print('작은 섬:', min(SIZE))
print('총:', cnt)