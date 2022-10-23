from copy import deepcopy

N = int(input())
arr = [[0] * N for _ in range(N)]


def visit(y, x):
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(8):
        for j in range(1, N):
            ny = y + dy[i] * j
            nx = x + dx[i] * j
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] == 1: continue
                arr[ny][nx] = 1

cnt = 0
def dfs(level):
    global cnt, arr
    if level == N:
        cnt += 1
        return
    for x in range(N): # for문으로 열만 돌리기
        if arr[level][x] == 1: continue # level을 행으로 활용하기
        backup = deepcopy(arr)
        arr[level][x] = 1
        visit(level, x)
        dfs(level + 1)
        arr = deepcopy(backup)

dfs(0)
print(cnt)
