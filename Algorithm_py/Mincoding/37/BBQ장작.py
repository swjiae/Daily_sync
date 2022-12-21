from collections import deque

# 입력받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
y, x = map(int, input().split())

# cnt 구하기
q = deque()
q.append([y, x, 0])
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
while q:
    y, x, level = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if arr[ny][nx] == 0:
                arr[ny][nx] = 1
                q.append([ny, nx, level+1])

# 출력하기
print(level)