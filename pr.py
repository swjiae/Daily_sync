from collections import deque

N, M = map(int, input().split())
arr = [[0]*N for _ in range(N)]
for i in range(M):
    p, s = map(int, input().split())
    arr[p-1][s-1] += 1

'''
[[0, 0, 1], 
 [0, 0, 1], 
 [0, 0, 0]]
'''

acc = [0]*N # [0, 0, 2]
used = [0]*N
for i in range(N):
    for j in range(N):
        if arr[j][i] == 1:
            acc[i] += 1

q = deque()
for i in range(N):
    if acc[i] == 0:
        used[i] = 1
        q.append(i)

result = []
while q:
    now = q.popleft()
    result.append(now+1)
    for i in range(N):
        if arr[now][i] == 1 and used[i] == 0:
            if acc[i] == 1:
                acc[i] -= 1
                q.append(i)
                used[i] = 1
            else:
                acc[i] -= 1

print(*result)