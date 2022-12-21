TC = int(input())
for T in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    used = [[0]*N for _ in range(N)]
    flag = 0

    def dfs(y, x):
        global flag
        if arr[y][x] == 3:
            flag = 1
            return
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if used[ny][nx] == 1: continue
                if arr[ny][nx] == 1: continue
                used[ny][nx] = 1
                dfs(ny, nx)
                used[ny][nx] = 0


    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:
                used[y][x] = 1
                dfs(y, x)

    print(f'#{T} {flag}')