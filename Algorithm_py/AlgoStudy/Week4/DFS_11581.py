N = int(input())
inf = 21e8
arr = [[inf]*N for _ in range(N)]

for i in range(N-1):
    branch = int(input())
    next = list(map(int, input().split()))
    for j in range(branch):
        arr[i][next[j]-1] = 1

'''
[[inf, 1, 1], 
[inf, inf, 1], 
[inf, inf, inf]]
'''

for start in range(N):
    for end in range(N):
        for via in range(N):
            if arr[start][end] > arr[start][via] + arr[via][end]:
                arr[start][end] = arr[start][via] + arr[via][end]

flag = 1
for i in range(N):
    if arr[i][i] != inf and arr[0][i] != inf:
        flag = 0
        break

print('NO CYCLE' if flag else 'CYCLE')