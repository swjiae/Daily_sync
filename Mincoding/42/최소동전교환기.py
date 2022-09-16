change = int(input())
Min = 21e8
coin = [10, 40, 60]

def dfs(level, sum):
    global Min
    if sum == change:
        Min = min(Min, level)
        return
    if sum > change:
        return
    for i in range(3):
        dfs(level+1, sum+coin[i])


dfs(0, 0)
print(Min)