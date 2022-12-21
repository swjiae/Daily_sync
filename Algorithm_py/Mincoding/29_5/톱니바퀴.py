arr = [
    [3, 2, 5, 3],
    [7, 6, 1, 6],
    [4, 9, 2, 7]
]
wheel = list(map(int, input().split()))

result = [[0] * 4 for _ in range(3)]
for j in range(4):
    for i in range(3):
        row = (i + wheel[j]) % 3
        result[row][j] = arr[i][j]
for i in range(3):
    print(*result[i], sep='')