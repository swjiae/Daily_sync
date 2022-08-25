arr = [list(map(int, input())) for _ in range(5)]
idx = list(map(int, input().split()))

for i in idx:
    arr[i].sort()

for i in range(5):
    print(arr[i][0], end=' ')