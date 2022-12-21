from collections import deque

# 입력받기
Map = [list(map(int, input().split())) for _ in range(4)]

# 치킨 총 몇마리 먹을 수 있는지 구하기
q = deque()
q.append([0, 0])
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cnt = 0
while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < 4 and 0 <= nx < 6:
            if Map[ny][nx] == 1: continue
            if Map[ny][nx] == 2:
                cnt += 1
            Map[ny][nx] = 1
            q.append([ny, nx])
# 출력하기
print(cnt)
