def bfs(sy, sx):
    global arr
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    queue = [(sy, sx)]
    arr[sy][sx] = 0
    while queue:
        sy, sx = queue.pop(0)
        for i in range(4):
            ny = sy + dy[i]
            nx = sx + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if arr[ny][nx] == 1:
                    arr[ny][nx] = 0
                    queue.append((ny, nx))

T = int(input())

for t in range(T):
    M, N, K = map(int, input().split())

    arr = [[0]*M for _ in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    cnt = 0
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 1:
                cnt += 1
                bfs(y, x)

    print(cnt)