import sys
input = sys.stdin.readline

from collections import deque


N, M = map(int, input().split())

arr = [[0]*N for _ in range(N)]
used = [0]*N

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    arr[a][b], arr[b][a] = 1, 1

def bfs(i):
    q = deque([i])
    while q:
        i = q.popleft()
        used[i] = 1
        for j in range(N):
            if arr[i][j] == 1:
                q.append(j)
                arr[i][j], arr[j][i] = 0, 0

cnt = 0
for i in range(N):
    if 1 in arr[i]:
        bfs(i)
        cnt += 1

for i in range(N):
    if used[i] == 0:
        cnt += 1

print(cnt)