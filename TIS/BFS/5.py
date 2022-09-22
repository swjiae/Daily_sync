from collections import deque

Map = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# BFS 이용해서 cnt구하는 함수 만들기
def bfs(sy, sx, ey, ex):
    q = deque()
    q.append([sy, sx, 0])
    while q:
        used = [[0]*5 for _ in range(4)]
        y, x, level = q.popleft()
        if y == ey and x == ex:
            return level
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 4 and 0 <= nx < 5:
                if Map[ny][nx] == 1: continue
                if used[ny][nx] == 1: continue
                used[ny][nx] = 1
                q.append([ny, nx, level+1])

cnt = 0
cnt += bfs(0, 0, 3, 0)
cnt += bfs(3, 0, 3, 4)

print(cnt)