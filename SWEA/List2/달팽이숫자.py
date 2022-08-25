TC = int(input())
for T in range(1, TC+1):
    N = int(input()) # 배열 길이
    arr = [[0]*N for _ in range(N)]
    visited = [[1]*N for _ in range(N)]
    y, x, idx = 0, 0, 0
    directy = [0, 1, 0, -1] # 좌하우상
    directx = [1, 0, -1, 0]
    for i in range(1, N**2+1):
        arr[y][x] = i
        visited[y][x] = 0
        dy = y + directy[idx]
        dx = x + directx[idx]
        if 0 <= dy < N and 0 <= dx < N and visited[dy][dx]:
            y, x = dy, dx
            continue
        idx = (idx+1) % 4
        dy = y + directy[idx]
        dx = x + directx[idx]
        y, x = dy, dx

    print(f'#{T}')
    for i in range(N):
        print(*arr[i])