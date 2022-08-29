arr = [[0]*30 for _ in range(30)]
n = int(input())
for _ in range(n):
    x, y, d = map(int, input().split())
    print(x, y)
    x, y = x+15, y+15
    print(x, y)
    arr[y-1][x-1] = 'H'
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    for i in range(4):
        for j in range(1, d+1):
            ny = y + dy[i]*j
            nx = x + dx[i]*j
            arr[ny][nx] += 1
print(arr)
'''
2
-2 0 1
1 3 2
'''