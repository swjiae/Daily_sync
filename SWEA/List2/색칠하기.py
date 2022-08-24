TC = int(input())
for T in range(1, TC+1):
    N = int(input()) # 칠할 영역 개수
    grid = [[0] * 10 for _ in range(10)]
    def painting(sy, sx, ey, ex, color):
        for i in range(sy, ey+1):
            for j in range(sx, ex+1):
                grid[i][j] += color

    for i in range(N):
        sy, sx, ey, ex, color = map(int, input().split())
        painting(sy, sx, ey, ex, color)

    total = 0
    for y in range(10):
        for x in range(10):
            if grid[y][x] == 3:
                total += 1

    print(f'#{T} {total}')