arr = list(map(int, input().split()))
i = 3
while 1:
    if i >= 12:
        break
    Max = 0
    a = i-2
    b = i-3
    if i % 2 == 0:
        c = arr[i//2]
        Max = max(arr[a], arr[b], arr[c])
    else:
        Max = max(arr[a], arr[b])
    arr[i] += Max
    i += 1

print(max(arr))