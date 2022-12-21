arr = list(map(int, input().split()))
path = [0]*5
used = [0]*5
Max = 0
Min = 21e8
def dfs(level):
    global Max, Min
    if level == 5:
        result = (path[0]*path[1])-(path[2]*path[3])+path[4]
        Max = max(Max, result)
        Min = min(Min, result)
        return
    for i in range(5):
        if used[i] == 1: continue
        path[level] = arr[i]
        used[i] = 1
        dfs(level+1)
        used[i] = 0
dfs(0)
print(Max)
print(Min)