def Sum(y, x):
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    sum = 0
    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]
        if 0 <= dy < N and 0 <= dx < N:
            sum += abs(arr[dy][dx] - arr[y][x])
    return sum

TC = 10
for T in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    for y in range(N):
        for x in range(N):
            total += Sum(y, x)
    print(f'#{T} {total}')