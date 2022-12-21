from copy import deepcopy

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
path = [0]*M
Min = 21e8
def recur(level, start, multi):
    global Min, result
    if level == M:
        if multi < Min:
            Min = multi
            result = deepcopy(path)
        return
    for i in range(start, N):
        path[level] = arr[i]
        recur(level+1, i+1, multi*arr[i])

recur(0, 0, 1)
print(*result)
