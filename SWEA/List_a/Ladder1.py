TC = 10
for _ in range(10):
    T = int(input())
    n = 100
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [[1]*n for _ in range(n)]

    def Start(y, x):
        directy = [-1, 0, 0]  # 상,좌,우
        directx = [0, -1, 1]
        while y >= 0:
            if y == 0:
                return x
            visit[y][x] = 0
            # 좌측에 1이 있을 때
            dy = y + directy[1]
            dx = x + directx[1]
            if 0 <= dy < n and 0 <= dx < n and arr[dy][dx] == 1 and visit[dy][dx]:
                y, x = dy, dx
                continue
            # 우측에 1이 있을 때
            dy = y + directy[2]
            dx = x + directx[2]
            if 0 <= dy < n and 0 <= dx < n and arr[dy][dx] == 1 and visit[dy][dx]:
                y, x = dy, dx
                continue
            # 둘 다 아닐 때
            dy = y + directy[0]
            dx = x + directx[0]
            y, x = dy, dx

    y = n-1
    x = arr[y].index(2)
    print(f'#{T}', Start(y, x))


