N, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
result = [[0]*N for _ in range(N)]
for i in range(N): # 고정
    for j in range(N): # 변화
        if K % 4 == 0:
            result[i][j] = arr[i][j]
        if K % 4 == 1:
            result[j][N-i-1] = arr[i][j]
        if K % 4 == 2:
            result[N-i-1][N-j-1] = arr[i][j]
        if K % 4 == 3:
            result[N-j-1][N-i-1] = arr[i][j]

for i in range(N):
    print(*result[i])