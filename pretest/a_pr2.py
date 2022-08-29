TC = int(input())
for T in range(1, TC+1):
    arr = [[0]*15 for _ in range(15)]
    n = int(input())
    for _ in range(n):
        dy = [1, -1, 0, 0]
        dx = [0, 0, -1, 1]
        x, y, d = map(int, input().split())
        print(x, y, d)
        x, y = x+15, y+15
        arr[y-1][x-1] = 'H'
        for i in range(4):
            for j in range(1, d+1):
                ny = y + dy[i]*j
                nx = x + dx[i]*j
                arr[ny][nx] += 1


