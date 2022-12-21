TC = int(input())
for T in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Min = 21e8
    used = [[0]*N for _ in range(N)]
    path = [0]*N
    def dfs(level, sum):
        global Min
        if sum >= Min:
            return
        if level == N:
            Min = min(sum, Min)
            return
        for i in range(N):
            if path[i] == 1 or used[level][i] == 1: continue
            path[i] = 1
            used[level][i] = 1
            dfs(level+1, sum+arr[level][i])
            used[level][i] = 0
            path[i] = 0

    dfs(0, 0)
    print(f'#{T}', Min)