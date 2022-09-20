from collections import deque
# 고정 값
Map = [
    [0, 0, 1, 1, 1, 1], # (0,0) tank
    [0, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1, 0] # (3,5) prince
]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
used = [[0]*6 for _ in range(4)]

def bfs(y, x):
    q = deque()
    q.append([y, x, 0, 2])
    used[y][x] = 1
    while q:
        y, x, level, cnt = q.popleft() # level : 거리
        if y == 3 and x == 5:
            return level
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 4 and 0 <= nx < 6:
                if used[ny][nx] == 1: continue
                if Map[ny][nx] == 1:
                    if cnt > 0:
                        cnt -= 1
                        used[ny][nx] = 1
                        q.append([ny, nx, level+1, cnt])
                    else:
                        continue
                used[ny][nx] = 1
                q.append([ny, nx, level+1, cnt])

print(bfs(0, 0))