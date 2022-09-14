TC = int(input())
for T in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    Min = 21e8

    def dfs(level, sum):
        global Min
        if sum > Min:
            return
        if level == N:
            if sum < Min:
                Min = sum
            return
        for i in range(N):
            if used[i] == 1: continue
            used[i] = 1
            dfs(level+1, sum+arr[level][i])
            used[i] = 0

    dfs(0, 0)
    print(f'#{T} {Min}')