arr = [
    [0, 0, 1, 0, 1, 1],
    [1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

a, b = map(int, input().split())
a, b = a-1, b-1

# a에서 b까지 최소이동횟수
used = [[0]*len(arr) for _ in range(len(arr))]
flag = 0
Min = 21e8
def dfs(now, cnt):
    global flag, Min
    if now == b:
        Min = min(Min, cnt)
        flag = 1
    for i in range(len(arr)):
        if arr[now][i] == 1:
            if used[now][i] == 1: continue
            used[now][i] = 1
            dfs(i, cnt+1)
            used[now][i] = 0
dfs(a, 0)

print(Min if flag else 0)