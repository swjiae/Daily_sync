from collections import deque

# 입력받기
'''
S = 시골쥐
D = 도시쥐
C = 치즈
갈 수 있는 길 = .
벽 = x
'''
N, M = map(int, input().split())
Map = [list(input().split()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if Map[i][j] == 'S':
            ys, xs = i, j
        if Map[i][j] == 'D':
            yd, xd = i, j
        if Map[i][j] == 'C':
            yc, xc = i, j

# 최소 이동 시간 구하기
def bfs(sy, sx, ey, ex):
    used = [[0]*M for _ in range(N)]
    q = deque()
    q.append([sy, sx, 0])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    while q:
        y, x, level = q.popleft()
        used[y][x] = 1
        if y == ey and x == ex: break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if Map[ny][nx] == 'x': continue
                if used[ny][nx] == 1: continue
                used[ny][nx] = 1
                q.append([ny, nx, level+1])
    return level

# 출력하기
result = 0
result += bfs(ys, xs, yc, xc)
result += bfs(yc, xc, yd, xd)
print(result)