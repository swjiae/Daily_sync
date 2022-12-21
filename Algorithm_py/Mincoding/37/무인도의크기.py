from collections import deque

# 입력받기
Map = [list(map(int, input().split())) for _ in range(4)]

# 육지의 크기 구하기
q = deque()
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
result = []
for i in range(4):
    for j in range(4):
        if Map[i][j] == 1:
            q.append([i, j])
            Map[i][j] = 0
            cnt = 1
            while q:
                y, x = q.popleft()
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < 4 and 0 <= nx < 4:
                        if Map[ny][nx] == 1:
                            Map[ny][nx] = 0
                            cnt += 1
                            q.append([ny, nx])
            result.append(cnt)

# 가장 큰 육지의 크기 출력하기
print(max(result))