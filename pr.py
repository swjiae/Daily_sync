power = [50, 40, 99, 5, 25, 6, 37]
used = [0]*7
Min = 21e8

def dfs(level, start, sum):
    global Min
    against = 0
    for i in range(7):
        if used[i] == 0:
            against += power[i]
    gap = abs(sum-against)
    Min = min(Min, gap)
    if level == 6:
        return
    for i in range(start, 7):
        used[i] = 1
        dfs(level+1, i+1, sum+power[i])
        used[i] = 0

dfs(0, 0, 0)
print(Min)