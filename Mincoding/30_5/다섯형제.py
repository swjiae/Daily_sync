# level = 0
# brunch = 5
arr = sorted(list(map(int, input().split())))
path = [0] * 5
cnt = 0

def abc(level, sum):
    global cnt
    if 10 <= sum <= 20:
        cnt += 1
    if level == 5:
        return
    for i in range(5):
        if level > 0 and path[level-1] >= arr[i]: continue
        path[level] = arr[i]
        abc(level+1, sum+arr[i])


abc(0, 0)
print(cnt)