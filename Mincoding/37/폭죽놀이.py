from collections import deque
# 입력받기
Map = [list(map(int, input().split())) for _ in range(4)]

# 카운트 세기
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
q = deque()
for i in range(4):
    for j in range(5):
        if Map[i][j] == 1:
            q.append([i, j, 0])

while q:
    y, x, level = q.popleft()
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < 4 and 0 <= nx < 5:
            if Map[ny][nx] == 0:
                Map[ny][nx] = 1
                q.append([ny, nx, level+1])

# 출력하기
print(level)