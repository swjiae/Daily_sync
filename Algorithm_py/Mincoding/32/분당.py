arr = [[[]]*3 for _ in range(3)]
N = int(input()) # 4

for _ in range(N):
    a, b, c = input().split()
    arr[int(a)][int(b)] = list(map(int, list(c)))

K = int(input()) # 2
krr = list(map(int, input().split())) # 4, 2
'''
[[[8, 5, 2], [], [5, 1]],
[[], [5], []],
[[3], [], []]]
'''

for i in range(3):
    for j in range(3):
        if arr[i][j]:
            for k in range(K):
                if arr[i][j]:
                    if arr[i][j][-1] > krr[k]: # 4, 2
                        arr[i][j][-1] -= krr[k]
                    else:
                        arr[i][j].pop()
cnt = 0
for i in range(3):
    for j in range(3):
        if arr[i][j]:
            cnt += len(arr[i][j])

print(cnt)