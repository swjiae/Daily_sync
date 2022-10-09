from collections import deque

# 입력받기
N = int(input())
Map = [list(input()) for _ in range(N)]
sy, sx = map(int, input().split())

for i in range(N):
    for j in range(N):
        if Map[i][j] == '$':
            fy, fx = i, j

# 최소 이동 횟수 구하기
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def bfs(sy, sx, ey, ex):
    global flag
    used = [[0] * N for _ in range(N)]
    q = deque()
    q.append([sy, sx, 0])
    used[sy][sx] = 1
    while q:
        y, x, level = q.popleft()
        if y == ey and x == ex: break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if Map[ny][nx] == '#': continue
                if Map[ny][nx] == '$' and flag == 1: continue
                used[ny][nx] = 1
                q.append([ny, nx, level+1])
    return level

# 출력하기
tmp = []
for i in range(N):
    for j in range(N):
        if Map[i][j] == 'A':
            result = 0
            flag = 1
            result += bfs(sy, sx, i, j)
            flag = 0
            result += bfs(i, j, fy, fx)
            tmp.append(result)
print(min(tmp))

'''
8
________
____A___
####____
__A#____
___#__A_
_#______
__###___
_$______
4 4
'''