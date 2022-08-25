N = int(input())
arr = list(map(int, input().split()))
i = 0
while i <= len(arr)-3: # pop을 사용하여 arr이 계속 바뀌기 때문에 len(arr)-3 사용
    if arr[i] == arr[i+1] == arr[i+2]:
        for _ in range(3):
            arr.pop(i)
    else:
        i += 1

arr.sort()

print(*arr)