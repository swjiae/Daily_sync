arr = list(map(int, input().split()))
n = len(arr)
result = [1]*n

for i in range(1, n):
    for j in range(0, i):
        if arr[i] > arr[j]:
            result[i] = max(result[j]+1, result[i])

print(result)