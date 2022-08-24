TC = 10
for T in range(1, TC + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    total = 0
    for y in range(N):
        for x in range(N):
            for k in range(4):
                dy = y + directy[k]
                dx = x + directx[k]
                if 0 <= dy < N and 0 <= dx < N:
                    if arr[dy][dx] > arr[y][x]:
                        total += arr[dy][dx] - arr[y][x]
                    elif arr[dy][dx] < arr[y][x]:
                        total += arr[y][x] - arr[dy][dx]

    print(f'#{T} {total}')