N, M = map(int, input().split())
inf = 21e8
arr = [[inf] * N for _ in range(N)]

for _ in range(M):
    y, x = map(int, input().split())
    arr[y-1][x-1] = 1
    arr[x-1][y-1] = 1

'''
[[2100000000.0, 2100000000.0, 1, 1, 2100000000.0], 
[2100000000.0, 2100000000.0, 1, 2100000000.0, 2100000000.0], 
[1, 1, 2100000000.0, 1, 2100000000.0], 
[1, 2100000000.0, 1, 2100000000.0, 1], 
[2100000000.0, 2100000000.0, 2100000000.0, 1, 2100000000.0]]
'''

for start in range(N):
    for via in range(N):
        for end in range(N):
            if arr[start][end] > arr[start][via] + arr[via][end]:
                arr[start][end] = arr[start][via] + arr[via][end]
            if arr[end][start] > arr[end][via] + arr[via][start]:
                arr[end][start] = arr[end][via] + arr[via][start]

Min = 21e8
for i in range(N):
    if Min > sum(arr[i]):
        Min = sum(arr[i])
        result = i+1
print(arr)
print(result)