from collections import deque
# 입력받기
N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]

# bfs로 시작점과 끝점 최소거리 찾기
def bfs(y, x, target):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    # used = [[0]*M for _ in range(N)]
    q = deque()
    q.append([y, x, 0])
    # used[y][x] = 1
    while q:
        y, x, level = q.popleft()
        if Map[y][x] == target:
            return y, x, level
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if Map[ny][nx] == '#': continue
                # if used[ny][nx] == 1: continue
                # used[ny][nx] = 1
                q.append([ny, nx, level+1])


# 배달지 위치 좌표 찾기
a, b = 0, 0
cnt = 0
for i in range(1, 5):
    va, vb, level = bfs(a, b, str(i)) # 도착좌표(va,vb), 최소거리(level)
    a, b = va, vb
    cnt += level

# 결과 출력하기
print(cnt)

'''
3 5
30002
##4##
01024
'''