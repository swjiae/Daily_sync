N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
group = [0]*(N+1)

def findboss(M):
    if group[M] == 0:
        return M
    boss = findboss(group[M])
    group[M] = boss
    return boss

def union(a, b):
    global flag
    aboss = findboss(a)
    bboss = findboss(b)
    if aboss == bboss:
        return 1
    group[bboss] = aboss

flag = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            arr[j][i] = 0
            flag = union(i+1, j+1)
            if flag:
                break

print('cycle 발견' if flag else '미발견')