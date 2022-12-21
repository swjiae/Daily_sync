arr = [
    [3, 5, 4, 1],
    [1, 1, 2, 3],
    [6, 7, 1, 2]
]
brr = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
numbers = list(map(int, input().split()))

for i in range(3):
    for j in range(4):
        flag = 1
        if arr[i][j] == numbers[-1]:
            brr[i][j] = numbers[0]
            continue
        for n in range(3):
            if arr[i][j] == numbers[n]:
                brr[i][j] = numbers[n+1]
                flag = 0
                break
        if flag:
            brr[i][j] = arr[i][j]
for i in range(3):
    print(*brr[i])