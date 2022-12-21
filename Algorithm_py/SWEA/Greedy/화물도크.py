TC = int(input())
for T in range(1, TC+1):
    arr = []
    N = int(input())
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    arr = sorted(arr, key= lambda x: x[1])

    b_time = -1
    cnt = 0
    for i in range(N):
        if b_time <= arr[i][0]:
            cnt += 1
            b_time = arr[i][1]

    print(f'#{T} {cnt}')