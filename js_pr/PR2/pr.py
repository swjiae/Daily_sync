dy = [-1, -1, 1, 1]
dx = [-1, 1, -1, 1]
used = [[0]*4 for _ in range(4)]
def dfs(level):
    if level == 4:
        return
    for i in range(4):
        for j in range(4):
            if used[i][j] == 1: continue
            used[i][j] = 1
            dfs(level+1)
            used[i][j] = 0
