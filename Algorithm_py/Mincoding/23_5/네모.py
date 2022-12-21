arr = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
    ]

brr = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        arr[i][j] = brr[i][j]

# 행의 합
max_r = 21e-8
for y in range(3):
    total_r = 0
    for x in range(3):
        total_r += arr[y][x]
    if total_r > max_r:
        max_r = total_r
    arr[y][3] = max_r
    max_r = 21e-8

# 열의 합
max_c = 21e-8
for x in range(3):
    total_c = 0
    for y in range(3):
        total_c += arr[y][x]
    if total_c > max_c:
        max_c = total_c
    arr[3][x] = max_c
    max_c = 21e-8

# 대각선의 합
max_d = 0
total_d = 0
for i in range(3):
    total_d += arr[i][i]
arr[3][3] = total_d

for i in range(4):
    print(*arr[i])



