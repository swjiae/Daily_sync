n = int(input())
arr = []
cnt = 0
for _ in range(n):
    cnt += 1
    if cnt >= 3:
        cnt = 3
    a, b = input().split()
    tmp = [int(b), a]
    arr.append(tmp)
    arr.sort(reverse=True)
    for i in range(cnt):
        print(arr[i][1], end=' ')
    print()