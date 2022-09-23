from collections import deque

paint = [list(input()) for _ in range(8)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def bfs(y, x):
    q = deque()
    tmp = deque()
    q.append([y, x])
    tmp.append([y, x])
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < 8 and 0 <= nx < 9:
                if paint[ny][nx] == '#':
                    q.append([ny, nx])
                    tmp.append([ny, nx])
                    paint[ny][nx] = '_'
    return tmp

def bfs2(y, x):
    q = deque()
    q.append([y, x, 0])
    while q:
        y, x, level = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < 8 and 0 <= nx < 9:
                if paint[ny][nx] == '_':
                    q.append([ny, nx, level+1])
                else:
                    return level

for i in range(8):
    for j in range(9):
        if paint[i][j] == '#':
            tmp = bfs(i, j)
            break
        break

for i in range(len(tmp)):
    result = bfs2(tmp[i][0], tmp[i][1])
print(result)
