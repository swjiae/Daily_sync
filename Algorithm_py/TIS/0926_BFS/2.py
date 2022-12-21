from collections import deque

arr = [
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 0],
]

name = input().split()
used = [0]*4
result = []
def bfs(top):
    q = deque()
    q.append(top)
    while q:
        now = q.popleft()
        result.append(name[now])
        for i in range(4):
            if arr[now][i] == 1:
                if used[i] == 1: continue
                used[i] = 1
                q.append(i)

used[0] = 1
bfs(0)
print(*result)
