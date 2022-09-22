from collections import deque
# 입력받기
N, M = map(int, input().split())

Map = [list(map(int, input().split())) for _ in range(N)]


# 섬 개수 구하기
q = deque()
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cnt = 0
for i in range(N):
    for j in range(M):
        if Map[i][j] == 1:
            Map[i][j] = 0
            q.append([i, j])
            while q:
                y, x = q.popleft()
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if 0 <= ny < N and 0 <= nx < M:
                        if Map[ny][nx] == 1:
                            Map[ny][nx] = 0
                            q.append([ny, nx])
            cnt += 1
# 출력하기
print(cnt)