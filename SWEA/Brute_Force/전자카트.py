'''
3
0 18 34
48 0 55
18 7 0
'''
from collections import deque

# 입력받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    used = [[0] * N for _ in range(N)]
    q = deque()
    q.append([y, x])
    used[y][x] = 1
    Sum = arr[y][x]
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if used[ny][nx] == 1: continue
                if arr[ny][nx] == 0: continue
                q.append([ny, nx])
                Sum += arr[ny][nx]
    return Sum
size = []
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            size.append(bfs(i, j))

print(min(size))